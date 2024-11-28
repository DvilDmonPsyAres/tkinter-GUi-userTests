import tkinter as tk
from tkinter import messagebox
import sqlite3
import json
        

#abrir y cargar archivo json
def cargar_test():
    with open('json/test2.JSON', 'r', encoding='utf-8') as file:
        return json.load(file)

# Función para desplegar la encuesta
def mostrar_test2():

    test = cargar_test()

    # Crear ventana tkinter
    ven = tk.Toplevel()
    ven.title('Test-02')

    #Almacenar resultados
    resultados = []

    # Crear preguntas y respuestas
    for idx, pregunta in enumerate(test):

        #crear un marco por cada pregunta
        pregunta_frame = tk.Frame(ven)
        pregunta_frame.pack(fill="x", pady=10, padx=10)

        #Mostrar la pregunta
        tk.Label(pregunta_frame, text=f"{idx + 1}. {pregunta['pregunta']}").pack(anchor="w")

        # Crear variables para las opciones de la pregunta
        opciones_var = [tk.StringVar(value="") for _ in pregunta["respuestas"]]

        # Almacena los botones para habilitarlos/deshabilitarlos

        radios_mas = []
        radios_menos = []

        def actualizar_respuestas(*args):
            """ Habilitar/deshabilitar opciones basado en selección """
            seleccionados = [var.get() for var in opciones_var]
            #testting
            print("seleccionados antes de counts:", seleccionados)
            mas_count = seleccionados.count("+")
            menos_count = seleccionados.count("-")

            #testing
            #if seleccionados[0] != "" and seleccionados[1] != "" and seleccionados[2] != "":
            #    print("works")
            
            if mas_count + menos_count > 2:
                # Resetear si hay más de dos selecciones
                for var in opciones_var:
                    var.set("")
                messagebox.showwarning("Advertencia", "Debe seleccionar solo un '+' y un '-'")
                return

            for i, var in enumerate(opciones_var):
                if var.get()=="":
                # Si ya hay dos símbolos seleccionados, deshabilitar las opciones no seleccionadas
                    if mas_count >= 1 and menos_count >= 1:
                        radios_mas[i].config(state="disabled")
                        radios_menos[i].config(state="disabled")
                    else:
                        radios_mas[i].config(state="normal")
                        radios_menos[i].config(state="normal")
                else:
                    # Mantener habilitados los seleccionados
                    radios_mas[i].config(state="normal")
                    radios_menos[i].config(state="normal")

        for i, respuesta in enumerate(pregunta["respuestas"]):
            frame = tk.Frame(pregunta_frame)
            frame.pack(anchor="w", padx=10)
            #testing
            print("creating butons num:", i)
            
            # Crear botones de "+" y "-"
            radio_mas = tk.Radiobutton(frame, text=f"+ {respuesta}", variable=opciones_var[i], value="+", command=actualizar_respuestas)
            radio_mas.pack(side="left")
            radios_mas.append(radio_mas)

            radio_menos = tk.Radiobutton(frame, text=f"- {respuesta}", variable=opciones_var[i], value="-", command=actualizar_respuestas)
            radio_menos.pack(side="left")
            radios_menos.append(radio_menos)
        


        # Llamar a la función de actualización inicial
        #testing
        print("antes del primer actualizar respuestas")
        actualizar_respuestas()
        print("despues del primer actualizar respuestas")

        # Agregar datos de la pregunta al resultado general
        resultados.append({
            "pregunta": pregunta["pregunta"],
            "variables": opciones_var
        })

    # Botón para enviar respuestas
    def enviar_respuestas():
        respuestas_completas = []
        for idx, pregunta in enumerate(test):
            seleccionados = [var.get() for var in opciones_var]
            if seleccionados.count("+") != 1 or seleccionados.count("-") != 1:
                tk.messagebox.showerror("Error", f"Debe seleccionar exactamente un '+' y un '-' en la pregunta: {pregunta['pregunta']}")
                return
            respuestas_completas.append({
                "pregunta": pregunta["pregunta"],
                "respuestas": seleccionados
            })
        print("Resultados finales:", respuestas_completas)
        ven.quit()

    tk.Button(ven, text="Enviar", command=enviar_respuestas).pack(pady=10)