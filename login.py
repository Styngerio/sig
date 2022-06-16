from tkinter import *
import x

class Login (Frame):
    def __init__(self, master=None):
        super().__init__(master,width=300, height=350, bg="#F41033")
        #Frame.__init__(self)
        self.pack()
        self.master = master
        print("login")
        inicio = Frame(self,bg="#F6BC94")
        inicio.place(x=0,y=0,relwidth=1, relheight=1)
        Label(inicio,text="Iniciar sesion", justify="center",font=("",20),height=0).pack()

        Label(inicio,text="Usuario", disabledforeground="").pack()
        self.user = Entry(inicio,width=20)
        self.user.pack()
        self.user.focus()

        Label(inicio,text="Contraseña").pack()
        self.password = Entry(inicio, show="*",width=20)
        self.password.pack()
        self.view= Button(inicio,text="Mostrar", command=self.view)
        self.view.pack(after=self.password)


        self.iniciar = Button(inicio, text="Iniciar", command=lambda: self.valida(self.user.get(),self.password.get()))
        self.iniciar.pack()
        if self.valida(self.user.get(),self.password.get()):
            return self.user.get()
    
    
    def valida(self, user, password):
        print(user,password)
        if password=="admin" and user=="admin":
           #return user,password
           Frame.quit
           x.main()
        else:
            print("Please try again!")
       
    def view(self):
        self.password.config(show="")