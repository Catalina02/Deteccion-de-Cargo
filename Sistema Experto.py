# -*- coding: utf-8 -*-
"""
Created on Sat Dec 12 00:07:55 2020

@author: 
"""
from tkinter import *
from main import *
from tkinter import messagebox as MessageBox
def ExaminarRoles():
    main_window = tk.Tk()
    app = Ventana2(main_window)
            
            


def Menu():
    root=Tk()
    root.title("Sistema Experto")
    root.iconbitmap("images.ico")
    root.resizable(0,0)
    #cuadro
    frame=Frame(root,width=300,height=300)
    frame.pack()
    frame.config(bg="lightblue",bd=5,relief="groove")
    #titulo
    label1=Label(root,text="Sistema Experto", 
                 foreground="dodgerblue4",bg="lightblue",
                 font=("Arial Black",15))
    label1.place(x=55, y=10)
    
    #botones
    button1=Button(root,text="Ingresar Empleado", 
                 foreground="lightcyan",bg="deepskyblue4",
                 font=("Arial",10),command=IngresarEmpleado)
    button1.place(x=20, y=100)
    
    button2=Button(root,text=" Examinar  Roles ", 
                 foreground="lightcyan",bg="deepskyblue4",
                 font=("Arial",10),command=ExaminarRoles)
    button2.place(x=170, y=100)
    
    #imagenes
    imagen1=PhotoImage(file="roles.png")
    im1=Label(root,image=imagen1)
    im1.place(x=17, y=150)
    
    imagen2=PhotoImage(file="persoana.png")
    im2=Label(root,image=imagen2)
    im2.place(x=165, y=150)

    root.mainloop()
    
def IngresarEmpleado():
    main_window = tk.Tk()
    app = Ventana(main_window)
    

Menu()