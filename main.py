from src.ejercicio1 import consultar_metadatos
from src.ejercicio2 import cambiar_permisos
from src.ejercicio3 import inventariar_directorio


def menu():
    while True:
        print('\n' + '=' * 62)
        print('  EJERCICIOS DE MANEJO DE ARCHIVOS - PYTHON')
        print('=' * 62)
        print('1. Consultar metadatos de un archivo')
        print('2. Consultar y cambiar permisos (Linux / POSIX)')
        print('3. Inventario y reporte de archivos')
        print('0. Salir')
        opcion = input('Seleccione una opcion: ').strip()
        if opcion == '1':
            consultar_metadatos()
        elif opcion == '2':
            cambiar_permisos()
        elif opcion == '3':
            inventariar_directorio()
        elif opcion == '0':
            print('Programa finalizado.')
            break
        else:
            print('Opcion no valida. Intente nuevamente.')
        input('\nPresione Enter para continuar...')


if __name__ == '__main__':
    menu()
