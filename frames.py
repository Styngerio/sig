from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from solicitud import *
from venta import *
from menu import*
from compra import *

class Frames(Frame):

    def __init__(self, master=None):
        super().__init__(master,width=1280, height=720, bg="#F41033")
        self.master = master
        self.pack()
        self.flag=""
        
        container = Frame(self, bg="#7FF410")
        container.place(relx=0.2,rely=0,relwidth=1, relheight=1)
        self.frames = {}
        for F in (Solicitud, Venta, Menu, Compra):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.place(x=0,y=0)
        Menu.showMenu(self,controller=self)
        self.show_frame("Menu")
    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()
            
        
    #probando mensajes
    def message(self):
        r = messagebox.askyesno(message="¿Desea continuar?", title="Título")
        if  r == True:
            if self.flag=="formsolicitud":
                print()


    


