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

def abrir_interpolacion():
    tabla_valores = [(0, 10), (50, 20), (100, 40), (150, 60), (200, 90)]

    def interpolar(x, x0, x1, y0, y1):
        return y0 + ((y1 - y0) / (x1 - x0)) * (x - x0)

    def calcular_distancia_frenado():
        tiempos_deseados = [55, 125, 175]
        resultado_str = "Tiempo de Reacción\tDistancia de Frenado\n"
        for tiempo in tiempos_deseados:
            for i in range(len(tabla_valores) - 1):
                if tabla_valores[i][0] <= tiempo < tabla_valores[i + 1][0]:
                    x0, y0 = tabla_valores[i]
                    x1, y1 = tabla_valores[i + 1]
                    distancia = interpolar(tiempo, x0, x1, y0, y1)
                    resultado_str += f"{tiempo}\t\t\t{distancia}\n"
                    break
        resultado_label.config(text=resultado_str)

    interpolacion_window = Toplevel(root)
    interpolacion_window.title("Calculadora de Distancia de Frenado (Interpolación Lineal)")
    calcular_button = tk.Button(interpolacion_window, text="Calcular Distancia de Frenado", command=calcular_distancia_frenado)
    calcular_button.pack()
    resultado_label = tk.Label(interpolacion_window, text="")
    resultado_label.pack()

def abrir_secante():
    def funcion(x):
        return 4 * x**3 - 3.8 * x**2 - 2 * x

    def calcular_raiz():
        x0 = float(entry_x.get())
        x1 = float(entry_x1.get())
        error_porcentual = float(entry_error.get()) / 100
        error_aceptado = error_porcentual * 100
        resultados = []
        while True:
            x_next = x1 - (funcion(x1) * (x1 - x0)) / (funcion(x1) - funcion(x0))
            error = abs((x_next - x1) / x_next) * 100
            resultados.append((x0, x1, x_next, funcion(x0), funcion(x1), funcion(x_next), error))
            if error < error_aceptado:
                break
            x0 = x1
            x1 = x_next
        mostrar_resultados(resultados)

    def mostrar_resultados(resultados):
        resultado_str = "Iteración \t xi-1\t\t xi\t\t xi+1\t\t f(xi-1)\t\t f(xi)\t\t f(xi+1)\t\t Error (%)\n"
        for i, (x0, x1, x_next, f_x0, f_x1, f_x_next, error) in enumerate(resultados):
            resultado_str += f"{i}\t\t {x0:.6f}\t {x1:.6f}\t {x_next:.6f}\t {f_x0:.6f}\t {f_x1:.6f}\t {f_x_next:.6f}\t {error:.6f}\n"
        resultado_label.config(text=resultado_str)

    secante_window = Toplevel(root)
    secante_window.title("Calculadora de Método de la Secante")
    label_x0 = tk.Label(secante_window, text="Valor inicial (xi-1):")
    label_x0.grid(row=0, column=0, sticky='e')
    entry_x = tk.Entry(secante_window)
    entry_x.grid(row=0, column=1)
    label_x1 = tk.Label(secante_window, text="Valor inicial (xi):")
    label_x1.grid(row=1, column=0, sticky='e')
    entry_x1 = tk.Entry(secante_window)
    entry_x1.grid(row=1, column=1)
    label_error = tk.Label(secante_window, text="Error porcentual (%):")
    label_error.grid(row=2, column=0, sticky='e')
    entry_error = tk.Entry(secante_window)
    entry_error.grid(row=2, column=1)
    calcular_button = tk.Button(secante_window, text="Calcular Raíz", command=calcular_raiz)
    calcular_button.grid(row=3, columnspan=2)
    resultado_label = tk.Label(secante_window, text="")
    resultado_label.grid(row=4, columnspan=2)
    entry_x.insert(0, "2")
    entry_x1.insert(0, "3")
    entry_error.insert(0, "1")

def abrir_punto_fijo():
    import math

    def funcion(x):
        return math.sqrt(math.exp(x) / 3)

    def calcular_punto_fijo():
        x0 = float(entry_x.get())
        error_porcentual = float(entry_error.get()) / 100
        error_aceptado = error_porcentual * 100
        resultados = []
        while True:
            x_next = funcion(x0)
            error = abs((x_next - x0) / x_next) * 100
            resultados.append((x0, x_next, error))
            if error < error_aceptado:
                break
            x0 = x_next
        mostrar_resultados(resultados)

    def mostrar_resultados(resultados):
        resultado_str = "Iteración\t x0\t\t xi+1\t\tError (%)\n"
        for i, (x0, x_next, error) in enumerate(resultados):
            resultado_str += f"{i}\t\t {x0:.6f}\t {x_next:.6f}\t {error:.6f}\n"
        resultado_label.config(text=resultado_str)

    punto_fijo_window = Toplevel(root)
    punto_fijo_window.title("Calculadora de Punto Fijo")
    label_x = tk.Label(punto_fijo_window, text="Valor inicial (x0):")
    label_x.grid(row=0, column=0, sticky='e')
    entry_x = tk.Entry(punto_fijo_window)
    entry_x.grid(row=0, column=1)
    label_error = tk.Label(punto_fijo_window, text="Error porcentual (%):")
    label_error.grid(row=1, column=0, sticky='e')
    entry_error = tk.Entry(punto_fijo_window)
    entry_error.grid(row=1, column=1)
    calcular_button = tk.Button(punto_fijo_window, text="Calcular Punto Fijo", command=calcular_punto_fijo)
    calcular_button.grid(row=2, columnspan=2)
    resultado_label = tk.Label(punto_fijo_window, text="")
    resultado_label.grid(row=3, columnspan=2)
    entry_x.insert(0, "0")
    entry_error.insert(0, "1")

# Crear la ventana principal
root = tk.Tk()
root.title("Métodos Numéricos")

# Botones para abrir cada método
btn_newton_raphson = tk.Button(root, text="Newton-Raphson", command=abrir_newton_raphson)
btn_newton_raphson.pack(fill=tk.X)

btn_newton_raphson_mejorado = tk.Button(root, text="Newton-Raphson Mejorado", command=abrir_newton_raphson_mejorado)
btn_newton_raphson_mejorado.pack(fill=tk.X)

btn_interpolacion = tk.Button(root, text="Interpolación", command=abrir_interpolacion)
btn_interpolacion.pack(fill=tk.X)

btn_secante = tk.Button(root, text="Método Secante", command=abrir_secante)
btn_secante.pack(fill=tk.X)

btn_punto_fijo = tk.Button(root, text="Método Punto Fijo", command=abrir_punto_fijo)
btn_punto_fijo.pack(fill=tk.X)

# Ejecutar el bucle principal de la interfaz gráfica
root.mainloop()
