import os
from pathlib import Path
from .utilidades import solicitar_ruta, fecha_legible, permisos_octal


def inventariar_directorio():
    print('\n--- EJERCICIO 3: INVENTARIO Y REPORTE DE ARCHIVOS ---')
    carpeta = solicitar_ruta('Ingrese la ruta de la carpeta: ')
    if carpeta is None or not carpeta.is_dir():
        print('Error: la carpeta no existe o la ruta no es un directorio.')
        return

    lineas = [
        '=' * 75,
        'REPORTE DE INVENTARIO DE ARCHIVOS',
        f'Directorio analizado: {carpeta.resolve()}',
        'Alcance: archivos directamente contenidos (sin subcarpetas)',
        '=' * 75,
    ]
    cantidad = 0
    total_bytes = 0
    errores = 0
    try:
        with os.scandir(carpeta) as elementos:
            for elemento in elementos:
                try:
                    if not elemento.is_file(follow_symlinks=False):
                        continue
                    datos = elemento.stat(follow_symlinks=False)
                    cantidad += 1
                    total_bytes += datos.st_size
                    lineas.extend([
                        f'Archivo #{cantidad}: {elemento.name}',
                        f'  Tamano: {datos.st_size} bytes',
                        f'  Ultima modificacion: {fecha_legible(datos.st_mtime)}',
                        f'  Permisos: {permisos_octal(datos.st_mode)}',
                        '-' * 75,
                    ])
                except (OSError, OverflowError, ValueError) as error:
                    errores += 1
                    lineas.append(f'ERROR al leer {elemento.name}: {error}')
    except OSError as error:
        print(f'Error al acceder al directorio: {error}')
        return

    lineas.extend([
        'RESUMEN GLOBAL',
        f'Cantidad total de archivos: {cantidad}',
        f'Tamano total acumulado: {total_bytes} bytes',
        f'Archivos con error de lectura: {errores}',
        '=' * 75,
    ])
    reporte = '\n'.join(lineas) + '\n'
    print('\n' + reporte)
    # Se guarda fuera de la carpeta analizada para no alterar el inventario.
    destino = Path(__file__).resolve().parent.parent / 'reportes' / 'reporte_archivos.txt'
    try:
        destino.parent.mkdir(parents=True, exist_ok=True)
        destino.write_text(reporte, encoding='utf-8')
        print(f'Reporte guardado correctamente en: {destino}')
    except OSError as error:
        print(f'No se pudo guardar el reporte: {error}')
