from tkinter import *
class Venta(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self,parent, controller)
        self.controller = controller
        self.flag="venta"
        print(self.flag)
        print("este solo funciona hasta aqui")
        framesecond = Frame(self,bg="#d6fC95")
        framesecond.place(relx=0.0,rely=0.0,relwidth=1, relheight=1)


        Label(framesecond,text="Registro de Venta", justify="center",font=("",20),height=0).place(relx=0.30, y=30)
        self.sale = Button(framesecond, text="Registrar compras", command=lambda:controller.show_frame("Solicitud"), bg="green", fg="#ffffff")
        self.sale.place(y=140, x=300)
        