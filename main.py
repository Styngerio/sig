from frames import Frames
from newsuplier import Newsuplier
from login import Login
from tkinter import *

def donothing():
   x = 0

#abre ventana secundaria
def new():
    root = Tk()
    root.wm_title("Registrar Proveerdor")
    app= Newsuplier(root)
    app.mainloop()
#ventana menu principal
def main():
    root = Tk()
    root.wm_title("Menu principal")
    app= Frames(root)
    #menubar 
    menubar= Menu(root)
    filemenu = Menu(menubar, tearoff=0)
    filemenu.add_command(label="New", command=new)
    filemenu.add_command(label="Open", command=donothing)
    filemenu.add_command(label="Save", command=donothing)
    filemenu.add_separator()
    filemenu.add_command(label="Exit", command=root.quit)
    menubar.add_cascade(label="File", menu=filemenu)

    helpmenu = Menu(menubar, tearoff=0)
    helpmenu.add_command(label="Help Index", command=donothing)
    helpmenu.add_command(label="About...", command=donothing)
    menubar.add_cascade(label="Help", menu=helpmenu)

    root.config(menu=menubar)
    app.mainloop()


def login():
    start=Tk()
    start.wm_title("Inicio de sesión")
    start.resizable(0,0)
    app = Login(start)
    app.mainloop()


if __name__=="__main__":
    #login()
    main()
    