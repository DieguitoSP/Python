#!/usr/bin/python3
from tkinter import *
from tkinter import ttk

class Application(ttk.Frame):
    def __init__(self, main_window):
        super().__init__(main_window)
        main_window.title("Posicionar elementos en Tcl/Tk")
        
        self.entry = ttk.Entry(self)
        self.entry.pack()
        
        self.button = ttk.Button(self, text="Hola, mundo!")
        self.button.pack()
        self.pack()
