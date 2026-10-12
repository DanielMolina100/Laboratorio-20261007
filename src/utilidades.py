import os
from datetime import datetime
from pathlib import Path
import stat


def solicitar_ruta(mensaje):
    entrada = input(mensaje).strip().strip('"').strip("'")
    return Path(entrada).expanduser() if entrada else None


def fecha_legible(timestamp):
    return datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')


def permisos_octal(modo):
    return format(stat.S_IMODE(modo), '03o')


def verificar_archivo(ruta):
    if ruta is None:
        print('Error: debe ingresar una ruta.')
        return False
    if not ruta.exists():
        print('Error: archivo no encontrado.')
        return False
    if not ruta.is_file():
        print('Error: la ruta no corresponde a un archivo.')
        return False
    return True
