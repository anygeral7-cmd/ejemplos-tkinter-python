import tkinter as tk

ventana = tk.Tk()
ventana.title("Ejemplo de etiquetas")
ventana.geometry("400x250")

tk.Label(ventana, text="Nombre:").pack(pady=10)

tk.Label(
    ventana,
    text="Ejemplo de Tkinter",
    font=("Arial", 16)
).pack()

ventana.mainloop()