import tkinter
from tkinter import messagebox

raiz = tkinter.Tk()
raiz.title("Logicalis")

def avisar():
    tkinter.messagebox.Showinfo('BOTON')
    boton=tkinter.Button(raiz, text = 'Pulsa', command = avisar)
    boton.pack()
raiz.mainloop()
