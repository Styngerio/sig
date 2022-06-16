from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import conect
class NewProduct(Frame):
    def __init__(self, master=None):
        super().__init__(master,width=400, height=450, bg="#F3ADB7")
        self.master = master
        self.pack()

        inicio = Frame(self,bg="#F6BC94")
        inicio.place(relx=0.0,rely=0.0,relwidth=1, relheight=1)

        Label(inicio,text="Registro de productos", justify="center",font=("",20),height=0).pack()

        Label(inicio,text="Producto:",font=("",14),height=0).place(x=30, y= 48)
        self.nameP=Entry(inicio,width=40)
        self.nameP.place(x=30, y= 70)

        Label(inicio, text="Precio:",font=("",14),height=0).place(x=30, y= 98)
        self.priceP = Entry(inicio,width=40)
        self.priceP.place(x=30, y= 120)

        Label(inicio,text="Proveedor",font=("",14),height=0).place(x=30,y=148)
        self.proveedor = ttk.Combobox(inicio,state="readonly")
        self.proveedor.bind("<<ComboboxSelected>>",self.selected_Proveedor)
        self.proveedor.place(x=30,y=170)

        Label(inicio,text="Detalle:",font=("",14),height=0).place(x=30, y=203)
        self.detailP = Text(inicio,height=5,width=40)
        self.detailP.place(x=30 ,y=230)

        self.saved = Button(inicio,text="Añadir producto",bg="green", fg="#ffffff", width=46, command=self.create).place(x=0,y=330)
        self.PROVEEDOR = int()
        self.uploadProveedor()

    def selected_Proveedor(self,event):
        indiceProveedor= self.Nproveedor.index(self.proveedor.get())
        self.PROVEEDOR = self.ItemProveedor[indiceProveedor]
        print(self.PROVEEDOR)



    def uploadProveedor(self):#carga los proveedores de la bg
        conn= conect.get_conection()
        cur = conn.cursor()
        cur.execute("SELECT * FROM proveedor")
        data = cur.fetchall()
        self.Nproveedor =[]#nombre de los proveedores
        self.ItemProveedor = []
        for nombre in data:
            self.Nproveedor.append(nombre[1])
            self.ItemProveedor.append(nombre[0])
        self.proveedor.config(values=self.Nproveedor)
        conn.close()


    def validate(self):
        print(self.nameP.get())
        print(self.priceP.get())
        print(self.proveedor.get())
        print(self.detailP.get(1.0, END+"-1c"))
        return len(str(self.PROVEEDOR))!=0 and len(self.nameP.get())!=0 and len(self.priceP.get())!=0 and len(self.detailP.get(1.0, END+"-1c")) and len(self.proveedor.get())!=0


    def create(self):
        if self.validate():
            print(self.proveedor.get(),self.PROVEEDOR, self.priceP.get(),self.detailP.get(1.0, END+"-1c"))
            conn= conect.get_conection()
            cur = conn.cursor()
            data=(self.nameP.get(),self.priceP.get(),str(self.detailP.get(1.0, END+"-1c")),self.PROVEEDOR)
            sql="INSERT INTO insumo(nombre, precio, detalle, proveedor) VALUES (%s, %s, %s, %s)"
            cur.execute(sql,data)
            conn.commit()
            self.nameP.delete(0,END)
            self.priceP.delete(0,END)
            self.detailP.delete(1.0,END)
            messagebox.showinfo(message=f"{self.nameP.get()}\nGuardado exitosamente", title="Ingreso de datos")
            print("Create new product !!")
        else:
            messagebox.showwarning(message="Debe llenar todos los campos para poder continuar", title="Ingreso de datos")
            print("No create product!")