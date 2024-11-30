import tkinter
from forms.registro import abrir_formulario
from forms.test1 import mostrar_test1
from forms.kuder import mostrar_test2
from forms.graficos import mostrar_grafico
from forms.respuestas import testPrinting

mainVentana = tkinter.Tk()
#ancho x alto
mainVentana.geometry("650x500")
mainVentana.title("psychoTests")

#Opciones botones registrar y encuesta
btnRegistro = tkinter.Button(mainVentana, text="Registrar Paciente", command=abrir_formulario)
btnRegistro.pack()

btnTest01 = tkinter.Button(mainVentana, text="Prueba1-opcionMultiple", command=mostrar_test1)
btnTest01.pack()

btnTest02 = tkinter.Button(mainVentana, text="Kuder", command=mostrar_test2)
btnTest02.pack()

btnTest_results = tkinter.Button(mainVentana, text="test GRAFICOS", command=mostrar_grafico)
btnTest_results.pack()

test_BTN = tkinter.Button(mainVentana, text="test respuestas completas", command=testPrinting)
test_BTN.pack()

#correr funcion principal
mainVentana.mainloop()