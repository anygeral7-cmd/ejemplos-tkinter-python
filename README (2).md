# Ejemplos de Tkinter con Python

## Descripción
Este repositorio contiene seis programas sencillos que muestran funciones básicas de **Tkinter**, la biblioteca incluida con muchas instalaciones de Python que permite crear interfaces gráficas de escritorio.

El proyecto está pensado para estudiantes y principiantes. Cada archivo es independiente y se puede ejecutar por separado.

## Objetivos
- Conocer la estructura básica de una ventana de Tkinter.
- Crear etiquetas, botones y campos de entrada.
- Capturar información escrita por el usuario.
- Utilizar casillas de selección.
- Realizar operaciones matemáticas mediante una interfaz gráfica.
- Crear menús y cuadros de diálogo.

## Contenido de los archivos

| Archivo | Funcionalidad |
|---|---|
| `01_ventana.py` | Crea una ventana con título, tamaño, color de fondo y etiquetas (`Label`). Sirve para conocer `Tk()`, `geometry()`, `title()` y `mainloop()`. |
| `02_botones.py` | Incluye un campo para escribir el nombre y botones para saludar o cerrar la ventana. Usa `Button`, `Entry`, `command` y cuadros de diálogo de `messagebox`. |
| `03_entradas.py` | Permite escribir texto y mostrarlo en pantalla al pulsar un botón. Demuestra cómo leer el contenido de un `Entry` y actualizar un `Label`. |
| `04_checkboxes.py` | Presenta casillas para seleccionar Python, Tkinter y GitHub. Usa `Checkbutton` y variables `BooleanVar` para conocer las opciones marcadas. |
| `05_calculadora.py` | Realiza suma, resta, multiplicación y división. Valida que los datos sean números y evita la división entre cero. |
| `06_menu.py` | Crea una barra de menú con las opciones “Acerca de” y “Salir”. Demuestra `Menu`, `add_command`, `add_cascade` y cuadros de confirmación. |

## Requisitos
- Python 3.
- Tkinter disponible en la instalación de Python.
- Un entorno de escritorio que pueda abrir ventanas gráficas.

No se requieren paquetes externos para estos ejemplos.

## Cómo ejecutar los programas

1. Descarga o clona este repositorio.
2. Abre una terminal en la carpeta del proyecto.
3. Ejecuta el archivo que quieras probar. Por ejemplo:

```bash
python 01_ventana.py
```

En algunas instalaciones de Windows también puedes utilizar:

```bash
py 01_ventana.py
```

Cambia `01_ventana.py` por el nombre del programa que quieras ejecutar. Ejecuta **un archivo a la vez**.

## Comprobar Tkinter
Si quieres comprobar que Tkinter está disponible, ejecuta:

```bash
python -m tkinter
```

Si aparece una ventana de prueba, Tkinter está funcionando. Si aparece un error, revisa la instalación de Python y que incluya Tcl/Tk.

## Conceptos utilizados
- **`Tk()`**: crea la ventana principal.
- **`Label`**: muestra texto.
- **`Button`**: ejecuta una acción al pulsarlo.
- **`Entry`**: permite introducir texto.
- **`Checkbutton`**: permite marcar o desmarcar opciones.
- **`Frame`**: agrupa otros elementos.
- **`Menu`**: crea menús.
- **`messagebox`**: muestra mensajes, advertencias, errores y confirmaciones.
- **`mainloop()`**: mantiene abierta la interfaz y procesa las interacciones.

## Estructura del repositorio

```text
Ejemplos-Tkinter-Python/
├── README.md
├── 01_ventana.py
├── 02_botones.py
├── 03_entradas.py
├── 04_checkboxes.py
├── 05_calculadora.py
└── 06_menu.py
```

## Autor
Proyecto educativo para practicar interfaces gráficas con Python y Tkinter.

## Licencia
Material educativo de ejemplo. Puedes adaptarlo para tus prácticas y ejercicios.
