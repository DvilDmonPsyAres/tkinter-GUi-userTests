import tkinter as tk
from tkinter import messagebox
import sqlite3
import json

#abrir y cargar archivo JSON
def cargar_test():
    with open('json/test1.JSON', 'r', encoding='utf-8') as file:
        return json.load(file)

# funcion para desplegar la encuesta
def mostrar_test1():
    test = cargar_test()

    #crear ventana tkinter
    ven = tk.Toplevel()
    ven.title('Test-01')

    #var para almacenar respuestas
    respuestas=[]

    #crear preguntas y respuestas
    for idx, pregunta in enumerate(test):
        tk.Label(ven, text=pregunta["pregunta"]).pack(padx=10,pady=5)

        #variables para las opciones de radio
        var = tk.StringVar()
        var.set(None) #respuesta por defecto

        #crear los botones de opcion
        #for respuesta in pregunta["respuestas"]:
            #tk.Radiobutton(ven, text=respuesta, variable=var, value=respuesta).pack(anchor="w")
        
        #Asignar una letra a cada respuesta (a,b,c,d,e)
        opciones = ['a','b','c','d','e']
        for i, respuesta in enumerate(pregunta["respuestas"]):
            tk.Radiobutton(ven, text=respuesta, variable=var, value=opciones[i]).pack(anchor="w")
            
        #guardar variable de respuesta en cada pregunta
        print(var)
        respuestas.append(var)

        # Boton Enviar
        def enviar_respuestas():
            #for idx, var in enumerate(respuestas):
            #    print(f"Pregunta {idx+1}: {var.get()}")
            #ven.quit()
            
            #contar las respuestas por inciso(a.b.c.d.e)
            resultados={'a':0,'b':0,'c':0,'d':0,'e':0}
            
            for var in respuestas:
                respuesta=var.get()
                if respuesta:
                    resultados[respuesta] += 1

            #MOstrar los resultados
            resultados_str = "\n".join([f"Inciso {inciso.upper()}: {count} respuestas" for inciso, count in resultados.items()])

            #mostrar los resultados en un messagebox
            messagebox.showinfo("Resultados", f"Resultados de la encuesta:\n\n{resultados_str}")

            ven.quit() #cerrar ventana

    tk.Button(ven, text="Enviar", command=enviar_respuestas).pack(pady=10)

