import tkinter as tk

def mostrar():
    etiqueta.config(text="Hola, " + entrada.get())

ventana = tk.Tk()
ventana.title("Campo de texto")
ventana.geometry("400x250")

entrada = tk.Entry(ventana)
entrada.pack(pady=15)

tk.Button(
    ventana,
    text="Aceptar",
    command=mostrar
).pack()

etiqueta = tk.Label(ventana, text="")
etiqueta.pack(pady=15)

ventana.mainloop()