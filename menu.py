from tkinter import *
class Menu(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self,parent, controller)
        self.controller = controller
        print(__name__)
        
    def showMenu(self,controller):
        print("tesssssss")
        framemain = Frame(self,bg="#1060F4")
        framemain.place(x=0,rely=0.0, relwidth=0.2, relheight=1)
        
        self.solicitud = Button(framemain, text="Solicitud de compra", command=lambda:controller.show_frame("Solicitud"), bg="green", fg="#ffffff")
        self.solicitud.place(relx=0, y=30, height=30, relwidth=1)

        self.create = Button(framemain, text="Registrar compras", command=lambda:controller.show_frame("Compra"), bg="green", fg="#ffffff")
        self.create.place(relx=0, y=70, height=30, relwidth=1)

        self.sale = Button(framemain, text="Registrar Venta", command=lambda:controller.show_frame("Venta"), bg="green", fg="#ffffff")
        self.sale.place(relx=0, y=110, height=30, relwidth=1)