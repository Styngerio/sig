from tkinter import *
from tkinter import ttk
class NewProveedor(Frame):
    def __init__(self, master=None):
        super().__init__(master,width=400, height=300, bg="#F3ADB7")
        self.master = master
        self.pack()

        inicio = Frame(self,bg="#F6BC94")
        inicio.place(relx=0.0,rely=0.0,relwidth=1, relheight=1)
        Label(inicio,text="Registro de proveedores", justify="center",font=("",20),height=0).pack()
        Label(inicio,text="RUC:",font=("",14),height=0).place(x=30, y= 48)
        self.RUC = Entry(inicio,width=40).place(x=30, y= 70)
        Label(inicio, text="Nombre:",font=("",14),height=0).place(x=30, y= 98)
        self.NOMBRE = Entry(inicio,width=40).place(x=30, y= 120)
        Label(inicio,text="Direccion",font=("",14),height=0).place(x=30,y=148)
        self.DIRECCION = Entry(inicio,width=40).place(x=30, y= 120)
        self.saved = Button(inicio,text="Añadir proveedor",bg="green", fg="#ffffff", width=46).place(x=0,y=203)
        #self.create_widgets()
        #connexio=conect.get_conection()
        #cur = connexio.cursor()
        ##si hace la insersion
        #sql="INSERT INTO proveedor (ruc, nombre, direccion) VALUES(%s,%s,%s)"
        #data= (precio,producto,cantidad) 
        #cur.execute(sql,data)
        #connexio.commit()
        #self.uploadProveedor()