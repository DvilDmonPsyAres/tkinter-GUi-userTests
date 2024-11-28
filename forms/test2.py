import tkinter as tk
from tkinter import messagebox
import json

# Abrir y cargar archivo JSON
def cargar_test():
    with open('json/test2.JSON', 'r', encoding='utf-8') as file:
        return json.load(file)

# Función para desplegar la encuesta
def mostrar_test2():
    test = cargar_test()

    # Crear ventana tkinter
    ven = tk.Toplevel()
    ven.title('Test-02')

    # Almacenar los resultados para todas las preguntas
    resultados = []

    for idx, pregunta in enumerate(test):
        # Crear un marco para cada pregunta
        pregunta_frame = tk.Frame(ven)
        pregunta_frame.pack(fill="x", pady=10, padx=10)

        # Mostrar la pregunta
        tk.Label(pregunta_frame, text=f"{idx + 1}. {pregunta['pregunta']}").pack(anchor="w")

        # Crear variables y listas específicas de la pregunta
        opciones_var = [tk.StringVar(value="") for _ in pregunta["respuestas"]]
        radios_mas = []
        radios_menos = []

        # Encapsular funciones para evitar conflictos entre preguntas
        def crear_opciones(pregunta, opciones_var, radios_mas, radios_menos):
            def actualizar_respuestas():
                """ Habilitar/deshabilitar opciones basado en selección """
                seleccionados = [var.get() for var in opciones_var]
                mas_count = seleccionados.count("+")
                menos_count = seleccionados.count("-")

                if mas_count + menos_count > 2:
                    # Resetear si hay más de dos selecciones
                    for var in opciones_var:
                        var.set("")
                    messagebox.showwarning("Advertencia", f"Debe seleccionar solo un '+' y un '-' en la pregunta: {pregunta['pregunta']}")
                    return

                for i, var in enumerate(opciones_var):
                    if var.get() == "":
                        # Si hay espacio para más selecciones, habilitar
                        if mas_count >= 1 and menos_count >= 1:
                            radios_mas[i].config(state="disabled")
                            radios_menos[i].config(state="disabled")
                        else:
                            radios_mas[i].config(state="normal")
                            radios_menos[i].config(state="normal")
                    else:
                        # Mantener habilitado el botón seleccionado
                        radios_mas[i].config(state="normal")
                        radios_menos[i].config(state="normal")

            # Crear botones de opción
            for i, respuesta in enumerate(pregunta["respuestas"]):
                frame = tk.Frame(pregunta_frame)
                frame.pack(anchor="w", padx=10)

                # Crear botones de "+" y "-"
                radio_mas = tk.Radiobutton(frame, text=f"+ {respuesta}", variable=opciones_var[i], value="+", command=actualizar_respuestas)
                radio_mas.pack(side="left")
                radios_mas.append(radio_mas)

                radio_menos = tk.Radiobutton(frame, text=f"- {respuesta}", variable=opciones_var[i], value="-", command=actualizar_respuestas)
                radio_menos.pack(side="left")
                radios_menos.append(radio_menos)

        # Crear opciones para la pregunta actual
        crear_opciones(pregunta, opciones_var, radios_mas, radios_menos)

        # Agregar datos de la pregunta al resultado general
        resultados.append({
            "pregunta": pregunta["pregunta"],
            "variables": opciones_var
        })

    # Botón para enviar respuestas
    def enviar_respuestas():
        respuestas_completas = []
        for idx, resultado in enumerate(resultados):
            seleccionados = [var.get() for var in resultado["variables"]]
            if seleccionados.count("+") != 1 or seleccionados.count("-") != 1:
                tk.messagebox.showerror("Error", f"Debe seleccionar exactamente un '+' y un '-' en la pregunta: {resultado['pregunta']}")
                return
            respuestas_completas.append({
                "pregunta": resultado["pregunta"],
                "respuestas": seleccionados
            })
        print("Resultados finales:", respuestas_completas)
        ven.quit()

    tk.Button(ven, text="Enviar", command=enviar_respuestas).pack(pady=10)