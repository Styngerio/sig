#import tkinter as tk
#
#class Scrollbar_Example:
#    def __init__(self):
#        self.window = tk.Tk()
#
#        self.scrollbar = tk.Scrollbar(self.window)
#        self.scrollbar.pack(side="right", fill="y")
#
#        self.listbox = tk.Listbox(self.window, yscrollcommand=self.scrollbar.set)
#        for i in range(100):
#            self.listbox.insert("end", str(i))
#        self.listbox.pack(side="left", fill="both")
#
#        self.scrollbar.config(command=self.listbox.yview)
#
#        self.window.mainloop()
#
#
#if __name__ == '__main__':
#    app = Scrollbar_Example()  

#from datetime import date
#from datetime import datetime
#
##Día actual
#today = date.today()
#
##Fecha actual
#now = datetime.now()
#
#print(today)
#print(now)

#-------------------------------------------------------------------------------
# Name:        Ejemplos Tkinter - Combos
# Copyright:   (c) David Trillo Montero 2014 - Manejando datos
##-------------------------------------------------------------------------------
# 
#import tkinter as tk
#from tkinter import ttk
#class Application(ttk.Frame):
#    
#    def __init__(self, main_window):
#        super().__init__(main_window)
#        main_window.title("Vista de árbol en Tkinter")
#        self.treeview = ttk.Treeview(self)
#        self.my_iid = "id_unico"  # Cualquier cadena es aceptable.
#        self.treeview.insert("", tk.END, text="Elemento 1", iid=self.my_iid)
#        print(self.treeview.get_children())
#        self.treeview.pack()
#        self.pack()
#main_window = tk.Tk()
#app = Application(main_window)
