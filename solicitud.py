from asyncio import protocols
from pydoc import visiblename
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import tkinter
from turtle import st
import conect 
from datetime import datetime
class Solicitud(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self,parent, controller)
        self.controller = controller
        self.flag="solicitud"
        print("este este tambien")
        print(self.flag)
        self.unitprice = 0#sumador de precios
        
        framesecond = Frame(self,bg="#F6BC94")
        framesecond.place(relx=0.0,rely=0.0,relwidth=1, relheight=1)

        #self.deslis=Scrollbar(self,Frame)
        #self.deslis.pack(side="right", fill="y")
        
        frameemploye = Frame(self, bg="#9E94F6")
        frameemploye.place(relx=0.0,rely=0.0,relwidth=1, relheight=0.3)
        Label(frameemploye,text="Solicitud de compra", justify="center",font=("",20),height=0).place(relx=0.30, y=30)
        #selecciona proveedor
        Label(frameemploye,text="Proveedor").place(y=80,x=20)
        self.proveedor = ttk.Combobox(frameemploye,state="readonly")
        self.proveedor.place(x=20, y=100)

        #selecciona insmo
        Label(frameemploye,text="Insumo").place(y=120,x=20)
        #self.producto = Entry(frameemploye,width=20)
        #self.producto.place(y=140, x=20)
        self.insumo = ttk.Combobox(frameemploye,state="readonly")
        self.insumo.place(y=140, x=20)
        
        #inserta cantidad
        Label(frameemploye,text="Cantidad").place(y=120,x=200)
        self.cantidad = Entry(frameemploye,width=12)
        self.cantidad.place(y=140, x=200)
        self.cantidad.focus()
        #ingresa precio
        Label(frameemploye,text="Precio").place(y=120,x=310)
        self.precio = Entry(frameemploye,width=20)
        self.precio.place(y=140, x=310)

        #total
        self.TOTAL = Entry(framesecond,textvariable=StringVar(value="0"),state="readonly")
        self.TOTAL.place(x=500, y=580, height=25, width=100)
        #Entry(self.edit wind,textvariable=StringVar(self.edit_wind,value=name),state='readonly').grid

        #buttons  to add
        self.add = Button(frameemploye, text="Añadir", command=self.add, bg="green", fg="#ffffff")
        self.add.place(x=490, y=140, height=25, width=100)

        self.edit = Button(framesecond, text="Editar", command=lambda:controller.show_frame("Menu"), bg="green", fg="#ffffff")
        self.edit.place(x=740, y=580, height=25, width=100)

        self.deleter = Button(framesecond, text="Eliminar", command=self.deleter, bg="red", fg="#ffffff")
        self.deleter.place(x=850, y=580, height=25, width=100)

        self.send = Button(framesecond, text="Enviar", command=self.submit, bg="green", fg="#ffffff")
        self.send.place(x=740, y=620, height=25, width=230)

        self.grid= ttk.Treeview(framesecond, columns=("count","price"))
        self.grid.place(relx=0.02,rely=0.3,relwidth=0.90, relheight=0.5)
        self.grid.columnconfigure("0",weight=5)

        self.grid.column("#0",width=300, stretch=NO)        
        self.grid.column("count",width=300, stretch=NO)
        self.grid.column("price",width=300, stretch=NO)
        


        self.grid.heading("#0", text="Insumo", anchor=CENTER)
        self.grid.heading("count", text="Cantidad", anchor=CENTER)
        self.grid.heading("price", text="Precio", anchor=CENTER)
        #cargar los datos proveedores e insumos
        self.uploadProveedor()
        self.uploadInsumo()

    def add(self):
        if self.validation():
            try:
                indice = self.itemI.index(self.insumo.get()) #asigno el indice del elemento seleccionado
                self.grid.insert("",END,text=self.insumo.get(), values=(self.cantidad.get(),self.precio.get()),iid=self.idI[indice])
                nuevo = self.precio.get()
                self.cantidad.delete(0,END)
                self.precio.delete(0,END)
                self.total(nuevo)

            except :
                messagebox.showinfo(message="Este insumo ya fue seleccionado", title="Ingreso de datos")
                self.cantidad.delete(0,END)
                self.precio.delete(0,END)
                print("dont not")

        else :
            messagebox.showinfo(message="Debe llenar todos los campos para poder continuar", title="Ingreso de datos")
            print("dont not")

    def uploadInsumo(self):#cargar los insumos de la bd
        #se esta intentado crear funcion que carge datos en el tree view nada funcional
        conn= conect.get_conection()
        cur = conn.cursor()
        cur.execute("SELECT * FROM insumo")
        data = cur.fetchall()
        self.itemI =[]
        self.idI=[]
        for nombre in data:
            self.idI.append(nombre[0])
            self.itemI.append(nombre[1])
        self.insumo.config(values=self.itemI)
            #self.grid.insert("",END,text=li[0], values=(li[1],li[2],self.cantidad.get()))
    def uploadProveedor(self):#carga los proveedores de la bg
        #se esta intentado crear funcion que carge datos en el tree view nada funcional
        conn= conect.get_conection()
        cur = conn.cursor()
        cur.execute("SELECT * FROM proveedor")
        data = cur.fetchall()
        item =[]
        for nombre in data:
            item.append(nombre[1])
        self.proveedor.config(values=item)
            #self.grid.insert("",END,text=li[0], values=(li[1],li[2],self.cantidad.get()))

    def total(self,nuevo):
        
        self.unitprice+=int(nuevo)
        self.TOTAL.config(textvariable=StringVar(value=str(self.unitprice)))

        print(self.unitprice)
        
    def confirm(self):
        self.r = messagebox.askyesno(message="¿Desea eliminar ítem?", title="Título")
        if self.r == True:
            print(self.r)
            return self.r


    def deleter(self):
        print(self.confirm,"fg")
        if self.confirm():
            restar =self.grid.item(self.grid.selection())['values'][1]
            restar="-"+str(restar)
            print(type(restar))
            self.total(restar)
            self.select_item = self.grid.selection()
            print(self.select_item)
            self.grid.delete(self.select_item)


    def submit(self):
        self.date= datetime.today()

        print(self.grid.get_children())
        print(self.TOTAL.get())
        print("sending...",self.date)


    
    def validation(self):
        return len(self.insumo.get())!=0 and len(self.precio.get())!=0 and len(self.cantidad.get())!=0
