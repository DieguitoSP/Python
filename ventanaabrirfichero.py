import tkinter
from tkinter import  filedialog

raiz= tkinter.Tk()
raiz.title('Logicalis')

def abrirfichero():
    rutafichero=filedialog.askopenfile(title='Abrir fichero')
    print(rutafichero)

boton = tkinter.Button(raiz, text='Pulsa para empezar', command=abrirfichero)
boton.pack()

raiz.mainloop()

