import tkinter as tk
from tkinter import Toplevel

# Funciones para las ventanas de cada método
def abrir_newton_raphson():
    def funcion(x):
        return 19*x**7 - 6*x**2 - 19

    def derivada(x):
        return 133*x**6 - 12*x

    def calcular_raiz():
        x_inicial = float(entry_x.get())
        error_porcentual = float(entry_error.get()) / 100
        error_aceptado = abs(funcion(x_inicial)) * error_porcentual
        resultados = []
        for iteracion in range(10):
            x_siguiente = x_inicial - funcion(x_inicial) / derivada(x_inicial)
            error_aproximado = abs((x_siguiente - x_inicial) / x_siguiente) * 100
            resultados.append((iteracion, x_siguiente, error_aproximado))
            x_inicial = x_siguiente
        resultado_str = "Iteración\tRaíz\tError Aproximado%\n"
        for iter_num, raiz, error in resultados:
            resultado_str += f"{iter_num}\t\t{raiz:.6f}\t\t{error:.2f}%\n"
        resultado_label.config(text=resultado_str)

    newton_raphson_window = Toplevel(root)
    newton_raphson_window.title("Calculadora de Newton-Raphson")
    label_x = tk.Label(newton_raphson_window, text="Valor inicial (x):")
    label_x.grid(row=0, column=0)
    entry_x = tk.Entry(newton_raphson_window)
    entry_x.grid(row=0, column=1)
    label_error = tk.Label(newton_raphson_window, text="Error porcentual (%):")
    label_error.grid(row=1, column=0)
    entry_error = tk.Entry(newton_raphson_window)
    entry_error.grid(row=1, column=1)
    calcular_button = tk.Button(newton_raphson_window, text="Calcular Raíz", command=calcular_raiz)
    calcular_button.grid(row=2, columnspan=2)
    resultado_label = tk.Label(newton_raphson_window, text="")
    resultado_label.grid(row=3, columnspan=2)
    entry_x.insert(0, "3")
    entry_error.insert(0, "1")
    
def abrir_newton_raphson_mejorado():
    def funcion(x):
        return 5*x**4 - 2*x**2 - 11
    
    def derivada(x):
        return 20*x**3 - 4*x
    
    def calcular_raiz():
        x_inicial = float(entry_x.get())
        error_porcentual = float(entry_error.get()) / 100
        error_aceptado = abs(funcion(x_inicial)) * error_porcentual
        resultados = []
        iteracion = 0
        while True:
            f_x = funcion(x_inicial)
            f_prima_x = derivada(x_inicial)
            x_siguiente = x_inicial - f_x / f_prima_x
            error_aproximado = abs((x_siguiente - x_inicial) / x_siguiente) * 100
            resultados.append((iteracion, x_siguiente, error_aproximado))
            if abs(f_x) < error_aceptado:
                break
            x_inicial = x_siguiente
            iteracion += 1
        resultado_str = "Iteración\tRaíz\t\tError Aproximado%\n"
        for iter_num, raiz, error in resultados:
            resultado_str += f"{iter_num}\t\t{raiz:.6f}\t\t{error:.2f}%\n"
        resultado_label.config(text=resultado_str)

    newton_raphson_mejorado_window = Toplevel(root)
    newton_raphson_mejorado_window.title("Calculadora de Newton-Raphson Mejorado")
    label_x = tk.Label(newton_raphson_mejorado_window, text="Valor inicial (x):")
    label_x.grid(row=0, column=0)
    entry_x = tk.Entry(newton_raphson_mejorado_window)
    entry_x.grid(row=0, column=1)
    label_error = tk.Label(newton_raphson_mejorado_window, text="Error porcentual (%):")
    label_error.grid(row=1, column=0)
    entry_error = tk.Entry(newton_raphson_mejorado_window)
    entry_error.grid(row=1, column=1)
    calcular_button = tk.Button(newton_raphson_mejorado_window, text="Calcular Raíz", command=calcular_raiz)
    calcular_button.grid(row=2, columnspan=2)
    resultado_label = tk.Label(newton_raphson_mejorado_window, text="")
    resultado_label.grid(row=3, columnspan=2)
    entry_x.insert(0, "2")
    entry_error.insert(0, "1")


root = tk.Tk()
root.title("Métodos Numéricos")

btn_newton_raphson = tk.Button(root, text="Newton-Raphson", command=abrir_newton_raphson)
btn_newton_raphson.pack(fill=tk.X)

btn_newton_raphson_mejorado = tk.Button(root, text="Newton-Raphson Mejorado", command=abrir_newton_raphson_mejorado)
btn_newton_raphson_mejorado.pack(fill=tk.X)

root.mainloop()
