import tkinter as tk
import json

# Abrir y cargar archivo JSON
def cargar_test():
    with open('json/test2.JSON', 'r', encoding='utf-8') as file:
        return json.load(file)

# Guardar los resultados en un archivo JSON
def guardar_resultados(resultados):
    print("Resultados, resultados")
    ven.quit()

def checkbox():
    test = cargar_test()

    # Crear ventana tkinter
    ven = tk.Toplevel()
    ven.title('Checkbox Window')

    # Crear un Frame en el Toplevel para contener los widgets desplazables
    frame = tk.Frame(ven)
    frame.pack(fill=tk.BOTH, expand=True)

    # Crear un Canvas en el Frame para permitir el desplazamiento
    canvas = tk.Canvas(frame)
    canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    # Crear un Scrollbar y asociarlo al Canvas
    scrollbar = tk.Scrollbar(frame, orient="vertical", command=canvas.yview)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    # Configurar el Canvas para que responda al Scrollbar
    canvas.config(yscrollcommand=scrollbar.set)

    # Crear un Frame dentro del Canvas para agregar contenido desplazable
    content_frame = tk.Frame(canvas)

    # Agregar el Frame al Canvas
    canvas.create_window((0, 0), window=content_frame, anchor="nw")

    # Almacenar los resultados
    resultados = []

    # Iterar sobre cada pregunta del JSON
    for idx, pregunta in enumerate(test):
        # Crear un Frame para cada pregunta
        pregunta_frame = tk.Frame(content_frame)
        pregunta_frame.pack(fill="x", pady=10, padx=10)

        # Mostrar la pregunta
        tk.Label(pregunta_frame, text=f"{idx + 1}. {pregunta['pregunta']}").pack(anchor="w")

        # Variables para los checkboxes de la pregunta actual
        me_gusta_vars = [tk.IntVar() for _ in pregunta['respuestas']]
        no_me_gusta_vars = [tk.IntVar() for _ in pregunta['respuestas']]

        # Función para manejar "Me gusta"
        def manejar_me_gusta(seleccionada):
            for i, var in enumerate(me_gusta_vars):
                if i != seleccionada:
                    var.set(0)  # Desactivar otras opciones de "Me gusta"
            no_me_gusta_vars[seleccionada].set(0)  # Desactivar "No me gusta" de la misma opción

        # Función para manejar "No me gusta"
        def manejar_no_me_gusta(seleccionada):
            for i, var in enumerate(no_me_gusta_vars):
                if i != seleccionada:
                    var.set(0)  # Desactivar otras opciones de "No me gusta"
            me_gusta_vars[seleccionada].set(0)  # Desactivar "Me gusta" de la misma opción

        # Crear las opciones para la pregunta
        for i, respuesta in enumerate(pregunta['respuestas']):
            respuesta_frame = tk.Frame(pregunta_frame)
            respuesta_frame.pack(pady=5, anchor="w")

            # Etiqueta para la respuesta
            tk.Label(respuesta_frame, text=respuesta).pack(side="left", padx=5)

            # Checkbox "Me gusta"
            tk.Checkbutton(
                respuesta_frame,
                text="Me gusta",
                variable=me_gusta_vars[i],
                command=lambda i=i: manejar_me_gusta(i)
            ).pack(side="left", padx=5)

            # Checkbox "No me gusta"
            tk.Checkbutton(
                respuesta_frame,
                text="No me gusta",
                variable=no_me_gusta_vars[i],
                command=lambda i=i: manejar_no_me_gusta(i)
            ).pack(side="left", padx=5)

        # Agregar las variables de cada pregunta a los resultados
        resultados.append({
            "pregunta": pregunta["pregunta"],
            "respuestas": pregunta["respuestas"],
            "estado": ["" for _ in pregunta['respuestas']]  # Inicializar con cadenas vacías
        })

        # Actualizar los estados al marcar un checkbox
        def actualizar_estado():
            for i in range(len(pregunta['respuestas'])):
                if me_gusta_vars[i].get() == 1:
                    resultados[idx]["estado"][i] = "+"
                elif no_me_gusta_vars[i].get() == 1:
                    resultados[idx]["estado"][i] = "-"
                else:
                    resultados[idx]["estado"][i] = ""

        # Asociar la función a cada cambio en las variables
        for i in range(len(pregunta['respuestas'])):
            me_gusta_vars[i].trace_add("write", lambda *_: actualizar_estado())
            no_me_gusta_vars[i].trace_add("write", lambda *_: actualizar_estado())

    # Botón para guardar resultados
    tk.Button(
        ven,
        text="Guardar resultados",
        command=lambda: guardar_resultados(resultados)
    ).pack(pady=10)

    # Actualizar la región desplazable del Canvas después de agregar las preguntas
    content_frame.update_idletasks()
    canvas.config(scrollregion=canvas.bbox("all"))

    tk.Button(ven, text="Enviar", command=guardar_resultados).pack(pady=10)