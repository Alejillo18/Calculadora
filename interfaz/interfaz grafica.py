import tkinter as tk
from tkinter import messagebox
import math

# === Funciones ===

def agregar(valor):
    entrada_actual = entrada.get()
    entrada.delete(0, tk.END)
    entrada.insert(0, entrada_actual + valor)

def calcular():
    try:
        resultado = eval(entrada.get())
        entrada.delete(0, tk.END)
        entrada.insert(0, str(resultado))
    except Exception:
        messagebox.showerror("Error", "Expresión inválida")

def limpiar():
    entrada.delete(0, tk.END)

def aplicar_func(funcion):
    try:
        valor = float(entrada.get())
        if funcion == 'sqrt':
            resultado = math.sqrt(valor)
        elif funcion == 'sin':
            resultado = math.sin(math.radians(valor))
        elif funcion == 'cos':
            resultado = math.cos(math.radians(valor))
        elif funcion == 'tan':
            resultado = math.tan(math.radians(valor))
        entrada.delete(0, tk.END)
        entrada.insert(0, str(resultado))
    except Exception:
        messagebox.showerror("Error", "Entrada inválida")

# === Ventana principal ===

ventana = tk.Tk()
ventana.title("Calculadora")
ventana.configure(bg="#f0f0f0")

# === Entrada ===

entrada = tk.Entry(ventana, font=("Arial", 20), bd=8, relief="sunken", justify="right", width=24)
entrada.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# === Botones numéricos y operadores ===

botones_basicos = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('C', 4, 2), ('+', 4, 3),
    ('=', 5, 0, 4),
]

for boton in botones_basicos:
    texto = boton[0]
    fila = boton[1]
    columna = boton[2]
    colspan = boton[3] if len(boton) > 3 else 1
    accion = lambda x=texto: agregar(x) if x not in ['=', 'C'] else (calcular() if x == '=' else limpiar())
    tk.Button(
        ventana, text=texto, font=("Arial", 16), width=6, height=2,
        bg="#ffffff", command=accion
    ).grid(row=fila, column=columna, columnspan=colspan, padx=3, pady=3)

# === Botones científicos ===

funciones = [
    ('√', 'sqrt'), ('sin', 'sin'), ('cos', 'cos'), ('tan', 'tan')
]

for i, (texto, func) in enumerate(funciones):
    tk.Button(
        ventana, text=texto, font=("Arial", 14), width=6, height=2,
        bg="#d0e0ff", command=lambda f=func: aplicar_func(f)
    ).grid(row=6, column=i, padx=3, pady=3)

# === Iniciar loop ===

ventana.mainloop()
