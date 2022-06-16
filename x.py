from frames import Frames
from newProveedor import NewProveedor
from newProduct import NewProduct
from tkinter import *

def donothing():
   x = 0

#abre ventanas secundarias
def insumo():
    insumo = Tk()
    insumo.wm_title("Registro de  Productos")
    Insumo= NewProduct(insumo)
    Insumo.mainloop()

def proveedor():
    prov = Tk()
    prov.wm_title("Registro de  Proveedores")
    Prov= NewProveedor(prov)
    Prov.mainloop()
#ventana menu principal
def main():
    root = Tk()
    root.wm_title("Menu principal")
    app= Frames(root)
    #menubar 
    menubar= Menu(root)
    filemenu = Menu(menubar, tearoff=0)
    filemenu.add_command(label="Añadir Insumo", command=insumo)
    filemenu.add_command(label="Añadir Proveedor", command=proveedor)
    filemenu.add_command(label="Save", command=donothing)
    filemenu.add_separator()
    filemenu.add_command(label="Exit", command=root.quit)
    menubar.add_cascade(label="Nuevo", menu=filemenu)

    helpmenu = Menu(menubar, tearoff=0)
    helpmenu.add_command(label="Help Index", command=donothing)
    helpmenu.add_command(label="About...", command=donothing)
    menubar.add_cascade(label="Help", menu=helpmenu)

    root.config(menu=menubar)
    app.mainloop()




if __name__=="__main__":
    main()
    