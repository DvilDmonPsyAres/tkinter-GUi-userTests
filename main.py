import tkinter
from forms.registro import abrir_formulario


mainVentana = tkinter.Tk()
#ancho x alto
mainVentana.geometry("650x500")
mainVentana.title("psychoTests")

#Opciones botones registrar y encuesta
btnRegistro = tkinter.Button(mainVentana, text="Registrar Paciente", command=abrir_formulario)
btnRegistro.pack()

btnTest01 = tkinter.Button(mainVentana, text="Prueba1")
btnTest01.pack()
#correr funcion principal
mainVentana.mainloop()