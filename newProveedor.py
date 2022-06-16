from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import conect
class NewProveedor(Frame):
    def __init__(self, master=None):
        super().__init__(master,width=400, height=300, bg="#F3ADB7")
        self.master = master
        self.pack()

        inicio = Frame(self,bg="#F6BC94")
        inicio.place(relx=0.0,rely=0.0,relwidth=1, relheight=1)
        Label(inicio,text="Registro de proveedores", justify="center",font=("",20),height=0).pack()
        Label(inicio,text="RUC:",font=("",14),height=0).place(x=30, y= 48)
        self.RUC = Entry(inicio,width=40)
        self.RUC.place(x=30, y= 70)

        Label(inicio, text="Nombre:",font=("",14),height=0).place(x=30, y= 98)
        self.NOMBRE = Entry(inicio,width=40)
        self.NOMBRE.place(x=30, y= 120)

        Label(inicio,text="Direccion",font=("",14),height=0).place(x=30,y=148)
        self.DIRECCION = Entry(inicio,width=40)
        self.DIRECCION.place(x=30, y= 170)

        self.saved = Button(inicio,text="Añadir proveedor",bg="green", fg="#ffffff", width=46, command=self.create)
        self.saved.place(x=0,y=203)
        

    def validate(self):
        return len(self.RUC.get())!=0 and len(self.NOMBRE.get())!=0 and len(self.DIRECCION.get())!=0

    def create(self):
        if self.validate():
            data = (self.RUC.get(),self.NOMBRE.get(),self.DIRECCION.get())
            conn= conect.get_conection()
            cur = conn.cursor()
            sql="INSERT INTO proveedor(ruc, nombre, direccion) VALUES (%s, %s, %s)"
            cur.execute(sql,data)
            conn.commit()
            messagebox.showinfo(title="Registro de proveedor", message=f"{self.NOMBRE.get()} fue añadido exitosamente")
            print("New suplier!!")
            self.RUC.delete(0,END)
            self.NOMBRE.delete(0,END)
            self.DIRECCION.delete(0, END)
        else:
            messagebox.showwarning(title="Registro de proveedor", message="Complete todos los campos!")