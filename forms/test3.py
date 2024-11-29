import tkinter as tk
from tkinter import ttk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import json
import matplotlib.pyplot as plt

def cargar_resultado():
    with open('json/graficos.JSON', 'r', encoding='utf-8') as results:
        return json.load(results)

def read_results():
    categorias=[]
    resultados=[]
    results = cargar_resultado()

    for item in results:
        categorias.append(item["categoria"])
        resultados.append(item["resultado"])

    return categorias, resultados

def mostrar_grafico():
    # Crear ventana principal
    ventana = tk.Toplevel()
    ventana.title("Gráficos en Tkinter")

    # Datos ficticios para mostrar resultados
    categorias = read_results()[0]
    resultados = read_results()[1]

    # Función para actualizar el gráfico
    def grafico_de_barras():

        # Crear figura para Matplotlib
        fig = Figure(figsize=(6, 4), dpi=100)
        ax = fig.add_subplot(111)  # Subgráfico 1x1

        # Lienzo para integrar el gráfico en Tkinter
        canvas = FigureCanvasTkAgg(fig, master=ventana)
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        # Limpia el gráfico anterior
        ax.clear()
        
        # Crear gráfico de barras
        ax.bar(categorias, resultados, color='skyblue')
        ax.set_title("Resultados por Categoría")
        ax.set_ylabel("Puntajes")
        ax.set_xlabel("Categorías")
        
        # Actualizar el lienzo
        canvas.draw()

    def linea_base_50():
        #linea base
        linea_base = 50

        # Crear listas para las barras positivas y negativas
        barras_arriba = [resultado - linea_base if resultado >= linea_base else 0 for resultado in resultados]
        barras_abajo = [resultado - linea_base if resultado < linea_base else 0 for resultado in resultados]

        # Configurar el gráfico
        plt.figure(figsize=(12, 6))

        # Graficar barras
        plt.bar(categorias, barras_arriba, color='skyblue', label='Por encima de 50')
        plt.bar(categorias, barras_abajo, color='lightcoral', label='Por debajo de 50')

        # Agregar una línea horizontal que represente la base en 50
        plt.axhline(0, color='black', linewidth=1, linestyle='--', label="Base (50)")

        # Configurar límites y ticks del eje Y para que muestren 0 a 100
        plt.ylim(-50, 50)
        plt.yticks(range(-50, 51, 10), [f"{50 + y}" for y in range(-50, 51, 10)])  # Etiquetas ajustadas para escala 0-100

        # Configurar título y etiquetas
        plt.title("Resultados de Categorías (Base en 50)", fontsize=14)
        plt.xlabel("Categorías", fontsize=12)
        plt.ylabel("Puntajes (Escala 0-100)", fontsize=12)
        plt.xticks(rotation=45, ha='right')
        plt.legend()


        #mostrar el grafico
        plt.tight_layout()
        plt.show()

    # Botón para actualizar el gráfico
    btn_actualizar = ttk.Button(ventana, text="grafico de Barras", command=grafico_de_barras)
    btn_actualizar.pack(side=tk.BOTTOM)

    #grafics console tes
    btn_transfigurar_resultado= ttk.Button(ventana, text="KUDER C", command=linea_base_50).pack(pady=20)
