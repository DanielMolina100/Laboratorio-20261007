import os
from .utilidades import solicitar_ruta, verificar_archivo, permisos_octal


PERMISOS = {
    '1': ('644', 0o644, 'Propietario: lectura/escritura; grupo y otros: lectura'),
    '2': ('600', 0o600, 'Propietario: lectura/escritura; grupo y otros: sin acceso'),
    '3': ('755', 0o755, 'Propietario: lectura/escritura/ejecucion; grupo y otros: lectura/ejecucion'),
}


def cambiar_permisos():
    print('\n--- EJERCICIO 2: PERMISOS DE ARCHIVOS EN LINUX ---')
    if os.name != 'posix':
        print('Este ejercicio requiere Linux o un entorno POSIX (por ejemplo, WSL).')
        print('En Windows abra la carpeta con VS Code usando WSL y ejecute python3 main.py.')
        return
    ruta = solicitar_ruta('Ingrese la ruta del archivo: ')
    if not verificar_archivo(ruta):
        return
    try:
        anterior = permisos_octal(os.stat(ruta).st_mode)
        print(f'Permisos actuales: {anterior}')
        for clave, (codigo, _, descripcion) in PERMISOS.items():
            print(f'{clave}. {codigo} - {descripcion}')
        seleccion = input('Seleccione una configuracion (1-3): ').strip()
        if seleccion not in PERMISOS:
            print('Error: seleccion no valida. No se realizaron cambios.')
            return
        codigo, modo, _ = PERMISOS[seleccion]
        os.chmod(ruta, modo)
        nuevo = permisos_octal(os.stat(ruta).st_mode)
        print('\nCOMPARACION DE PERMISOS')
        print(f'Archivo:            {ruta.resolve()}')
        print(f'Permisos anteriores: {anterior}')
        print(f'Permisos solicitados: {codigo}')
        print(f'Permisos finales:   {nuevo}')
        print('Cambio aplicado correctamente.' if int(nuevo, 8) == modo else 'Aviso: verifique los permisos finales.')
    except (OSError, ValueError) as error:
        print(f'Error de acceso o modificacion de permisos: {error}')
