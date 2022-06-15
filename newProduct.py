from tkinter import *
from tkinter import ttk
class NewProduct(Frame):
    def __init__(self, master=None):
        super().__init__(master,width=400, height=450, bg="#F3ADB7")
        self.master = master
        self.pack()

        inicio = Frame(self,bg="#F6BC94")
        inicio.place(relx=0.0,rely=0.0,relwidth=1, relheight=1)
        Label(inicio,text="Registro de productos", justify="center",font=("",20),height=0).pack()
        Label(inicio,text="Producto:",font=("",14),height=0).place(x=30, y= 48)
        self.nameP = Entry(inicio,width=40).place(x=30, y= 70)
        Label(inicio, text="Precio:",font=("",14),height=0).place(x=30, y= 98)
        self.priceP = Entry(inicio,width=40).place(x=30, y= 120)
        Label(inicio,text="Proveedor",font=("",14),height=0).place(x=30,y=148)
        self.proveedor = ttk.Combobox(inicio,state="readonly")
        self.proveedor.bind("<<ComboboxSelected>>")
        self.proveedor.place(x=30,y=170)
        Label(inicio,text="Detalle:",font=("",14),height=0).place(x=30, y=203)
        self.detailP = Text(inicio,height=5,width=40).place(x=30 ,y=230)
        self.saved = Button(inicio,text="Añadir producto",bg="green", fg="#ffffff", width=46).place(x=0,y=330)
        #self.create_widgets()
        #connexio=conect.get_conection()
        #cur = connexio.cursor()
        ##si hace la insersion
        #sql="INSERT INTO proveedor (ruc, nombre, direccion) VALUES(%s,%s,%s)"
        #data= (precio,producto,cantidad) 
        #cur.execute(sql,data)
        #connexio.commit()
        #self.uploadProveedor()