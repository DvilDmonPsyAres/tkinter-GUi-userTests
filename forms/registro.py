import tkinter as tk
from tkinter import messagebox
from tkcalendar import Calendar
import sqlite3 

def abrir_formulario():
    #crear nueva ventana
    ventanaRegistro = tk.Toplevel()
    ventanaRegistro.title("Formulario de Registro de Pacientes")

    #Etiquetas y campos de Entrada para formularios
    tk.Label(ventanaRegistro, text="Nombre:").grid(row=0, column=0, padx=10, pady=10)
    entry_nombre=tk.Entry(ventanaRegistro)
    entry_nombre.grid(row=0,column=1,padx=10,pady=10)

    tk.Label(ventanaRegistro, text="Apellidos:").grid(row=1, column=0, padx=10, pady=10)
    entry_apellidos=tk.Entry(ventanaRegistro)
    entry_apellidos.grid(row=1,column=1,padx=10,pady=10)

    tk.Label(ventanaRegistro, text="Fecha de Nacimiento:").grid(row=2, column=0, padx=10, pady=10)
    calendar = Calendar(ventanaRegistro, date_pattern='yyyy-mm-dd')
    calendar.grid(row=2, column=1, padx=10,pady=10)

    tk.Label(ventanaRegistro, text="Genero:").grid(row=3, column=0, padx=10, pady=10)
    #Lista de Opciones para el Genero
    opciones_genero = ["Masculino", "Femenino","Otros"]
    selected_genero = tk.StringVar(ventanaRegistro)
    selected_genero.set(opciones_genero[0]) #valor por defecto
    #crear el menu con las opciones de genero
    genero_menu = tk.OptionMenu(ventanaRegistro, selected_genero, *opciones_genero)
    genero_menu.grid(row=3,column=1,padx=10,pady=10)

    #Boton para guardar datos
    def guardar_datos():
        nombre=entry_nombre.get()
        apellidos=entry_apellidos.get()
        fecha_de_nacimiento=calendar.get_date() #obtener fecha seleccionada
        genero = selected_genero.get() #obtener genero seleccionado 

        #probar el guardado de datos atravez de esta alerta
        messagebox.showinfo("Datos guardados", f"Paciente: {nombre}\nApellidos: {apellidos}\nFecha de Nacimiento: {fecha_de_nacimiento}\nGenero: {genero}")

    tk.Button(ventanaRegistro, text="Guardar", command=guardar_datos).grid(row=5,column=1,padx=10,pady=20)

#funcion para guardar los datos en la base de datos
    def guardar_datos_en_db():

        nombre=entry_nombre.get()
        apellidos=entry_apellidos.get()
        fecha_de_nacimiento=calendar.get_date() #obtener fecha seleccionada
        genero = selected_genero.get() #obtener genero seleccionado 

        #conectar con la base de datos
        conn = sqlite3.connect('pacientes.db')
        c = conn.cursor()

        #insetar los datos
        c.execute("INSERT INTO pacientes (nombre, apellidos, fecha_de_nacimiento, genero) VALUES (?, ?, ?, ?)", (nombre, apellidos, fecha_de_nacimiento, genero))

        #confirmar cambios y cerrar la conexion
        conn.commit()
        conn.close()

    tk.Button(ventanaRegistro, text="Guardar en Base de Datos", command=guardar_datos_en_db).grid(row=5,column=2,padx=10,pady=20)