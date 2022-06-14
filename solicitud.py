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
        self.proveedor.bind("<<ComboboxSelected>>",self.selected_Proveedor)
        self.proveedor.place(x=20, y=100)

        #selecciona insmo
        Label(frameemploye,text="Insumo").place(y=120,x=20)
        self.insumo = ttk.Combobox(frameemploye,state="readonly")
        self.insumo.bind("<<ComboboxSelected>>", self.selection_changed)
        self.insumo.place(y=140, x=20)
        
        #inserta cantidad
        Label(frameemploye,text="Cantidad").place(y=120,x=200)
        self.cantidad = Entry(frameemploye,width=12)
        self.cantidad.place(y=140, x=200)
        self.cantidad.focus()
        #ingresa precio
        Label(frameemploye,text="Precio").place(y=120,x=310)
        self.precio = Entry(frameemploye,width=20,state="readonly")
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

        self.grid= ttk.Treeview(framesecond, columns=("count","price","subtotal"))
        self.grid.place(relx=0.02,rely=0.3,relwidth=0.75, relheight=0.48)
        self.grid.columnconfigure("0",weight=5)

        self.grid.column("#0",width=300, stretch=NO)        
        self.grid.column("count",width=100, stretch=NO)
        self.grid.column("price",width=200, stretch=NO)
        self.grid.column("subtotal",width=300, stretch=NO)
        


        self.grid.heading("#0", text="Insumo", anchor=CENTER)
        self.grid.heading("count", text="Cantidad", anchor=CENTER)
        self.grid.heading("price", text="Precio", anchor=CENTER)
        self.grid.heading("subtotal", text="Sub Total", anchor=CENTER)
        #cargar los datos proveedores e insumos
        self.uploadProveedor()
        self.uploadInsumo()
    def selected_Proveedor(self,event):
        indiceProveedor= self.Nproveedor.index(self.proveedor.get())
        self.PROVEEDOR = self.ItemProveedor[indiceProveedor]

    def selection_changed(self,event):
        Indiceprice= self.itemI.index(self.insumo.get())
        self.precio.config(textvariable=StringVar(value=str(self.ItemPrecio[Indiceprice])))


    def add(self):
        if self.validation():
            try:
                indice = self.itemI.index(self.insumo.get()) #asigno el indice del elemento seleccionado
                subtotal= round(float(self.cantidad.get())*float(self.precio.get()),2)
                self.grid.insert("",END,text=self.insumo.get(), values=(self.cantidad.get(),self.precio.get(),subtotal),iid=self.idI[indice])
                nuevo = self.precio.get()
                self.cantidad.delete(0,END)
                self.precio.delete(0,END)
                self.total(subtotal)

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
        self.ItemPrecio = []
        for nombre in data:
            self.idI.append(nombre[0])
            self.itemI.append(nombre[1])
            self.ItemPrecio.append(nombre[2])
        self.insumo.config(values=self.itemI)
            #self.grid.insert("",END,text=li[0], values=(li[1],li[2],self.cantidad.get()))
    def uploadProveedor(self):#carga los proveedores de la bg
        #se esta intentado crear funcion que carge datos en el tree view nada funcional
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
            #self.grid.insert("",END,text=li[0], values=(li[1],li[2],self.cantidad.get()))

    def total(self,nuevo):
        
        self.unitprice+=round(float(nuevo),2)
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
            restar =self.grid.item(self.grid.selection())['values'][2]
            restar="-"+str(restar)
            print(type(restar))
            self.total(restar) 
            self.select_item = self.grid.selection()
            print(self.select_item)
            self.grid.delete(self.select_item)


    def submit(self):
        print(self.PROVEEDOR,"proveedor")
        if len(str(self.PROVEEDOR))!=0:
            self.date= datetime.today()
            data=(str(self.TOTAL.get()),1726257825,self.PROVEEDOR,str(self.date))
            sql="INSERT INTO compra (total,usuario, proveedor,fechacompra)VALUES(%s, %s, %s, %s)"
            conn= conect.get_conection()
            cur = conn.cursor()
            cur.execute(sql,data)
            conn.commit()
            conn.close()
            print(sql,data)
            conn= conect.get_conection()
            data2=(str(self.TOTAL.get()),1726257825,self.PROVEEDOR)
            cur = conn.cursor()
            cur.execute("SELECT id_compra FROM compra WHERE (total=%s AND usuario=%s AND proveedor=%s)",data2)
            response = cur.fetchall()
            conn.close()
            compra = response[-1][0]
            messagebox.showinfo(message="INsert correct", title="Ingreso de datos")
            InsertP=self.grid.get_children()
            conn= conect.get_conection()
            cur = conn.cursor()
            for insumo in InsertP:#aun falta corregir
                data3 =(insumo,compra)
                sql="INSERT INTO detalleCompra (id_insumo,id_compra)VALUES(%s, %s)"
                cur.execute(sql,data3)
                conn.commit()
            
            print("sending...",self.date)


    
    def validation(self):
        return len(self.insumo.get())!=0 and len(self.precio.get())!=0 and len(self.cantidad.get())!=0 and len(self.proveedor.get())!=0
