import os
from .utilidades import solicitar_ruta, verificar_archivo, fecha_legible, permisos_octal


def consultar_metadatos():
    print('\n--- EJERCICIO 1: METADATOS DE ARCHIVOS ---')
    ruta = solicitar_ruta('Ingrese nombre o ruta del archivo: ')
    if not verificar_archivo(ruta):
        return
    try:
        datos = os.stat(ruta)
        print('\n' + '-' * 55)
        print('REPORTE DE METADATOS')
        print('-' * 55)
        print(f'Nombre:              {ruta.name}')
        print(f'Ruta:                {ruta.resolve()}')
        print(f'Tamano en bytes:     {datos.st_size}')
        print(f'Ultima modificacion: {fecha_legible(datos.st_mtime)}')
        print(f'Ultimo acceso:       {fecha_legible(datos.st_atime)}')
        print(f'Permisos (octal):    {permisos_octal(datos.st_mode)}')
        print('-' * 55)
    except (OSError, OverflowError, ValueError) as error:
        print(f'Error al consultar metadatos: {error}')
