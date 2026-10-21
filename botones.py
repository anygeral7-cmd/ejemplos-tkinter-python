import tkinter as tk

def saludar():
    etiqueta.config(text="¡Hola! Presionaste el botón")

ventana = tk.Tk()
ventana.title("Ejemplo de botones")
ventana.geometry("400x250")

etiqueta = tk.Label(ventana, text="Presiona el botón")
etiqueta.pack(pady=20)

boton = tk.Button(ventana, text="Saludar", command=saludar)
boton.pack()

ventana.mainloop()