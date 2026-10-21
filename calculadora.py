import tkinter as tk

def sumar():
    try:
        n1 = float(numero1.get())
        n2 = float(numero2.get())
        resultado.config(text=f"Resultado: {n1 + n2}")
    except ValueError:
        resultado.config(text="Escribe dos números válidos")

ventana = tk.Tk()
ventana.title("Calculadora")
ventana.geometry("400x300")

tk.Label(ventana, text="Primer número").pack()
numero1 = tk.Entry(ventana)
numero1.pack()

tk.Label(ventana, text="Segundo número").pack()
numero2 = tk.Entry(ventana)
numero2.pack()

tk.Button(ventana, text="Sumar", command=sumar).pack(pady=10)

resultado = tk.Label(ventana, text="Resultado:")
resultado.pack()

ventana.mainloop()