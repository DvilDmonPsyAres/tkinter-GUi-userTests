import tkinter as tk
import json

# Abrir y cargar archivo JSON
def cargar_test():
    with open('json/test2.JSON', 'r', encoding='utf-8') as file:
        return json.load(file)

def checkbox():
    test = cargar_test()

    # Crear ventana tkinter
    ven = tk.Toplevel()
    ven.title('checkbox window')

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

    # Actualizar la región del Canvas para permitir el desplazamiento
    content_frame.update_idletasks()
    canvas.config(scrollregion=canvas.bbox("all"))

    # Almacenar los resultados para todas las preguntas
    resultados = []

    for idx, pregunta in enumerate(test):

        def manejar_me_gusta(seleccionada):
            for i, var in enumerate(me_gusta_vars):
                if i != seleccionada:  # Si no es la seleccionada, desactívala
                    var.set(0)

        # Función para manejar la lógica de "No me gusta"
        def manejar_no_me_gusta(seleccionada):
            for i, var in enumerate(no_me_gusta_vars):
                if i != seleccionada:  # Si no es la seleccionada, desactívala
                    var.set(0)


        # Crear un marco para cada pregunta
        pregunta_frame = tk.Frame(content_frame)
        pregunta_frame.pack(fill="x", pady=10, padx=10)

        # Mostrar la pregunta
        tk.Label(pregunta_frame, text=f"{idx + 1}. {pregunta['pregunta']}").pack(anchor="w")

        # Crear las propuestas y sus checkboxes
        for i in range(3):

            #Variables para los checkboxes
            me_gusta_vars = [tk.IntVar() for _ in range(3)]
            no_me_gusta_vars = [tk.IntVar() for _ in range(3)]
            
            frame = tk.Frame(pregunta_frame)
            frame.pack(pady=5, anchor="w")

            propuesta_label = tk.Label(frame, text=f"Propuesta {i + 1}:")
            propuesta_label.pack(side="left", padx=5)       

            me_gusta_cb = tk.Checkbutton(
                frame,
                text="Me gusta",
                variable=me_gusta_vars[i],
                command=lambda i=i: manejar_me_gusta(i),
            )
            me_gusta_cb.pack(side="left", padx=5)

            no_me_gusta_cb = tk.Checkbutton(
                frame,
                text="No me gusta",
                variable=no_me_gusta_vars[i],
                command=lambda i=i: manejar_no_me_gusta(i),
            )
            no_me_gusta_cb.pack(side="left", padx=5)

        # Función para mostrar el resultado
        def mostrar_resultado():
            me_gusta = next((f"Propuesta {i + 1}" for i, var in enumerate(me_gusta_vars) if var.get()), "Ninguna")
            no_me_gusta = next((f"Propuesta {i + 1}" for i, var in enumerate(no_me_gusta_vars) if var.get()), "Ninguna")
            estado_label.config(text=f"Me gusta: {me_gusta}\nNo me gusta: {no_me_gusta}")

    # Actualizar la región desplazable del Canvas después de agregar todas las preguntas
    content_frame.update_idletasks()
    canvas.config(scrollregion=canvas.bbox("all"))

    tk.Button(ven, text="Enviar", command=mostrar_resultado).pack(pady=10)