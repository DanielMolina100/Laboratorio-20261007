# Proyecto: Ejercicios de manejo de archivos con Python

Incluye los tres ejercicios del documento **20261007 - Ejercicios.pdf**, integrados en un menu.

## Requisitos
- Python 3.10 o superior.
- Visual Studio Code.
- No se requieren librerias externas.
- **Ejercicio 2:** Linux o entorno POSIX, por ejemplo Ubuntu en WSL. No se ejecuta en Windows nativo porque la consigna exige Linux/POSIX.

## Estructura
```text
Proyecto_Ejercicios_20261007/
|-- main.py
|-- src/
|   |-- __init__.py
|   |-- utilidades.py
|   |-- ejercicio1.py
|   |-- ejercicio2.py
|   `-- ejercicio3.py
|-- archivos_prueba/
|   |-- clientes.txt
|   |-- productos.txt
|   `-- inventario.txt
|-- reportes/
|   `-- (aqui se crea reporte_archivos.txt)
`-- README.md
```

## Ejecucion en VS Code (Windows)
1. Descomprima el ZIP.
2. Abra la carpeta `Proyecto_Ejercicios_20261007` en VS Code.
3. Abra **Terminal > Nueva terminal**.
4. Ejecute `py main.py` (o `python main.py`).
5. Seleccione una opcion del menu.

## Pruebas sugeridas
- **Opcion 1:** escriba `archivos_prueba/clientes.txt` para ver sus metadatos. Pruebe tambien `no_existe.txt` para validar el error.
- **Opcion 2 (Linux/WSL):** escriba `archivos_prueba/inventario.txt` y seleccione 1 (644), 2 (600) o 3 (755). Compare los permisos anteriores y finales.
- **Opcion 3:** escriba `archivos_prueba` para inventariar los tres archivos de ejemplo. El reporte se muestra en consola y se guarda en `reportes/reporte_archivos.txt`.

## Como ejecutar el ejercicio 2 en Windows con WSL
Instale y configure WSL con una distribucion Linux si aun no la tiene. Abra la carpeta desde VS Code en modo WSL y ejecute `python3 main.py`. Los permisos Linux se aplican segun el sistema de archivos y el montaje; para pruebas fiables use una carpeta dentro del sistema de archivos Linux (por ejemplo, en su directorio personal de Ubuntu).

## Notas
- El ejercicio 3 analiza solamente archivos del directorio indicado, **no** recorre subcarpetas, tal como indica la consigna.
- Los errores individuales de lectura no detienen el inventario.
- Las fechas de ultimo acceso pueden variar por configuracion del sistema de archivos.
