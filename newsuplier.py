from tkinter import *
from tkinter import ttk
class Newsuplier(Frame):
    def __init__(self, master=None):
        super().__init__(master,width=800, height=500, bg="#F3ADB7")
        self.master = master
        self.pack()

        inicio = Frame(self,bg="#F6BC94")
        inicio.place(relx=0.0,rely=0.0,relwidth=1, relheight=1)
        Label(inicio,text="Iniciar sesion", justify="center",font=("",20),height=0).place(x=15,y=5)
        
        #self.create_widgets()
        #connexio=conect.get_conection()
        #cur = connexio.cursor()
        ##si hace la insersion
        #sql="INSERT INTO proveedor (ruc, nombre, direccion) VALUES(%s,%s,%s)"
        #data= (precio,producto,cantidad) 
        #cur.execute(sql,data)
        #connexio.commit()
        #self.uploadProveedor()