import tkinter as tk
from tkinter import messagebox
import sqlite3
import json

#abrir y cargar archivo json
def cargar_test():
    with open('json/test2.JSON', 'r', encoding='utf-8') as file:
        return json.load(file)

# Función para validar que solo se ingrese un carácter válido (+ o -)
def validar_entrada(P):
    return P in ['+', '-'] or P == ''  # Solo permite '+' o '-' o vacío

# Función para inhabilitar las respuestas en la misma sección
def inhabilitar_respuestas(entries, seccion_idx, entry_idx):
    for i, entry in enumerate(entries[seccion_idx]):
        if i != entry_idx:
            entry.config(state='disabled')

# Función para enviar las respuestas (por ahora solo muestra las respuestas)
def enviar_respuestas(entries):
    respuestas = {}
    for seccion_idx, seccion_entries in enumerate(entries):
        respuestas[f"Sección {seccion_idx + 1}"] = []
        for entry in seccion_entries:
            respuestas[f"Sección {seccion_idx + 1}"].append(entry.get())
    
    # Mostrar las respuestas en un mensaje (puedes guardarlas en una base de datos o archivo)
    print("Respuestas:", respuestas)
    messagebox.showinfo("Respuestas Enviadas", json.dumps(respuestas, indent=2))
    ven.quit()


def mostrar_test2():
    test = cargar_test()

    # Crear ventana tkinter
    ven = tk.Toplevel()
    ven.title('Test-02')

    # Lista para almacenar las entradas de cada sección
    entries = []

    # Crear preguntas y respuestas
    for idx, seccion in enumerate(test):
        # Mostrar la pregunta
        tk.Label(ven, text=seccion["seccion"]).pack(padx=10, pady=5)

        # Lista para almacenar las entradas de esta sección
        seccion_entries = []

        # Desplegar las preguntas y permitir solo '+' o '-'
        for pregunta_idx, pregunta in enumerate(seccion["preguntas"]):
            tk.Label(ven, text=pregunta).pack(anchor="w", padx=10)

            # Campo de texto que solo permite un carácter '+' o '-'
            vcmd = (ven.register(validar_entrada), '%P')
            entry = tk.Entry(ven, validate='key', validatecommand=vcmd)
            entry.pack(pady=5, padx=10, fill='x')

            # Deshabilitar la otra entrada cuando se selecciona una respuesta
            entry.bind("<KeyRelease>", lambda e, seccion_idx=idx, entry_idx=pregunta_idx: inhabilitar_respuestas(entries, seccion_idx, entry_idx))

            # Añadir la entrada a la lista de la sección
            seccion_entries.append(entry)

        # Añadir la lista de entradas de esta sección a la lista general
        entries.append(seccion_entries)

    # Botón para enviar las respuestas
    tk.Button(ven, text="Enviar", command=lambda: enviar_respuestas(entries)).pack(pady=10)
    