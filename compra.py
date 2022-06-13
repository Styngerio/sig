from tkinter import Frame, Label
class Compra(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self,parent, controller)
        self.controller = controller
        self.compra(parent, controller)
        self.flag="compra"
        print(self.flag)
        print("este si funciona")

        


    def compra(self, parent, controller):
        self.flag="formcreate"
        print(self.flag)
        framesecond = Frame(self,bg="#F6AC93")
        framesecond.place(relx=0.0,rely=0.0,relwidth=1, relheight=1)
        Label(framesecond,text="Registro de compra", justify="center",font=("",20),height=0).place(relx=0.30, y=30)