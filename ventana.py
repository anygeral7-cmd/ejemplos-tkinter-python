import tkinter as tk

ventana = tk.Tk()
ventana.title("Mi primera ventana")
ventana.geometry("400x300")

etiqueta = tk.Label(ventana, text="Hola, Tkinter")
etiqueta.pack(pady=30)

ventana.mainloop()