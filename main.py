## importacion de la libreria
from tkinter import *
from tkinter import ttk
import tkinter as tk
from functools import partial
from tkinter import messagebox as MessageBox


class Ventana:

    
    def ingresoDatos(self, nec1, nec2, comp, hab1, hab2, raiz):
            matriz=[[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
            porcentajes=[0,0,0,0,0,0]
            if (nec1 == "x"):
                matriz[4][0]=3
                matriz[5][0]=3
            if (nec1 == "y"):
                matriz[0][0]=3
                matriz[1][0]=3
                matriz[3][0]=3
                matriz[2][0]=3
            if (nec2 == "afiliacion"):
                matriz[1][1]=1
                matriz[2][1]=1
                matriz[3][1]=1
                matriz[5][1]=1
            if (nec2 == "poder"):
                matriz[0][1]=1
            if (nec2 == "identidad de la actividad"):
                matriz[4][1]=1
            if (comp == "orden y seguridad"):
                matriz[0][2]=5
                matriz[1][2]=5
            if (comp == "intelectual"):
                matriz[2][2]=5
            if (comp == "comportamiento"):
                matriz[3][2]=5
            if (comp == "tecnicas"):
                matriz[4][2]=5
            if (comp == "basicas"):
                matriz[5][2]=5
            if (hab1 or hab2 == "competitivo"):
                matriz[0][3]=1
                matriz[1][3]=1
            if (hab1 or hab2 == "emprendedor"):
                matriz[2][3]=1
            if (hab1 or hab2 == "comunicador"):
                matriz[3][3]=1
                matriz[0][4]=1
            if (hab1 or hab2 == "diciplinado"):
                matriz[4][3]=1
            if (hab1 or hab2 == "flexible"):
                matriz[5][3]=1
            if (hab1 or hab2 == "armonico"):
                matriz[1][4]=1
            if (hab1 or hab2 == "responsable"):
                matriz[2][4]=1
            if (hab1 or hab2 == "desarrollador"):
                matriz[3][4]=1
            if (hab1 or hab2 == "analitico"):
                matriz[4][4]=1
            if (hab1 or hab2 == "empatico"):
                matriz[5][4]=1
            for i in range(0,len(matriz)):
                cont=0
                for j in range(0,len(matriz[i])):
                    cont+=matriz[i][j]
                porcentajes[i]=(cont/11)*100

            print(porcentajes)
            maximo = max(porcentajes)
            roles=[]
            if(porcentajes[0]==maximo):
                roles.append("Gerente General")

            if(porcentajes[1]==maximo):
                roles.append("Sub Gerente General")
            if(porcentajes[2]==maximo):
                roles.append("Gerente de operaciones")
            if(porcentajes[3]==maximo):
                roles.append("Jefe de proyecto")
            if(porcentajes[4]==maximo):
                roles.append("Tecnico")
            if(porcentajes[5]==maximo):
                roles.append("Atencion al cliente")
            print(roles)

            resultado = tk.Text(raiz)
            resultado.pack()
            resultado.place(x=250,y=150)
            resultado.config(width=42, height=5, font=("Consolas",12))

            text=""
            if(len(roles)>1):
                text="Los roles indicados para esta persona son: "
                for i in range(0, len(roles)):
                    text+=roles[i] + ", "
            else:
                text="El rol mas indicado para esta persona es: "
                text+=roles[0]
            print (text)
            
            MessageBox.showinfo("Resultados", text)

            resultado.insert(tk.INSERT, text)
            resultado.config(state="disable")
    def __init__(self, raiz):
        raiz.title("Sistema Experto")
        raiz.resizable(1,0)
        raiz.config(bg="lightblue",bd=5,relief="groove")
        raiz.geometry("250x400")
        raiz.iconbitmap("images.ico")
        
        raiz.config(bg="lightblue",bd=5,relief="groove")
        # necesidad 1
        necesidad1 = Label(raiz, text="Necesidad 1",bg="lightblue")
        necesidad1.pack()
        necesidad1.place(x=50,y=10)
        combonecesidad = ttk.Combobox(raiz, state="readonly")
        combonecesidad.pack()
        combonecesidad.place(x=50,y=40)
        combonecesidad['values'] = ['x','y']
        #necesidad 2
        necesidad2 = Label(raiz, text="Necesidad 2",bg="lightblue")
        necesidad2.pack()
        necesidad2.place(x=50,y=70)
        combonecesidad2= ttk.Combobox(raiz, state="readonly")
        combonecesidad2.pack()
        combonecesidad2.place(x=50,y=100)
        combonecesidad2['values'] = ['poder','afiliacion','identidad de la actividad']
        #Competencia
        competencia = Label(raiz, text="Competencia",bg="lightblue")
        competencia.pack()
        competencia.place(x=50,y=130)
        combocompetencia = ttk.Combobox(raiz, state="readonly")
        combocompetencia.pack()
        combocompetencia.place(x=50,y=160)
        combocompetencia['values'] = ['orden y seguridad','intelectual','comportamiento','tecnicas','basicas']
        #habilidad 1
        habilidad1 = Label(raiz, text="Habilidad 1",bg="lightblue")
        habilidad1.pack()
        habilidad1.place(x=50,y=200)
        comboboxhabilidad1= ttk.Combobox(raiz, state="readonly")
        comboboxhabilidad1.pack()
        comboboxhabilidad1.place(x=50,y=230)
        comboboxhabilidad1['values'] = ['competitivo','emprendedor','comunicador','diciplinado','flexible']
        #habilidad 2
        habilidad1 = Label(raiz, text="Habilidad 2",bg="lightblue")
        habilidad1.pack()
        habilidad1.place(x=50,y=270)
        comboboxhabilidad2= ttk.Combobox(raiz, state="readonly")
        comboboxhabilidad2.pack()
        comboboxhabilidad2.place(x=50,y=300)
        comboboxhabilidad2['values'] = ['comunicador','armonico','responsable','desarrollador','analitico','empatico']
        #boton
        enviar = Button(raiz, text="Enviar", foreground="lightcyan",bg="deepskyblue4",
                 font=("Arial",10),command = lambda: self.ingresoDatos(combonecesidad.get(),combonecesidad2.get(),combocompetencia.get(),comboboxhabilidad1.get(),comboboxhabilidad2.get(), raiz)) 
        enviar.pack()
        enviar.place(x=92,y=340)
        
        

class Ventana2:

        def __init__(self, raiz):
            raiz.title("Sistema Experto")
            raiz.resizable(1,0)
            raiz.config(bg="lightblue",bd=5,relief="groove")
            raiz.geometry("250x400")
            raiz.iconbitmap("images.ico")
            raiz.resizable(0,0)
            raiz.config(bg="lightblue",bd=5,relief="groove")
            
            
            '''
            label1=Label(raiz,text="Roles", 
                 foreground="dodgerblue4",bg="lightblue",
                 font=("Arial Black",15))
            label1.place(x=70, y=10)
            '''
            #Estrategico
            Estrategico1 = Label(raiz, text="Estrategico",bg="lightblue",font=("Arial"))
            Estrategico1.pack()
            Estrategico1.place(x=30,y=30)
            enviar1 = Button(raiz, text="Gerente General", foreground="lightcyan",bg="deepskyblue4",
                     font=("Arial",10),command=partial(Mostrar,Rol[0],Necesidad[1],Necesidad[2],Habilidad[11],Habilidad[0],Competencia[1]))
            enviar1.place(x=50,y=60)
            enviar1 = Button(raiz, text="Sub Gerente", foreground="lightcyan",bg="deepskyblue4",
                     font=("Arial",10),command=partial(Mostrar,Rol[1],Necesidad[1],Necesidad[3],Habilidad[6],Habilidad[0],Competencia[2]) )
            enviar1.place(x=50,y=90)
            
            #Tactico
            Tactico1 = Label(raiz, text="Tactico",bg="lightblue",font=("Arial"))
            Tactico1.pack()
            Tactico1.place(x=30,y=140)
            enviar2 = Button(raiz, text="Jefe de Proyecto", foreground="lightcyan",bg="deepskyblue4",
                     font=("Arial",10),command=partial(Mostrar,Rol[2],Necesidad[1],Necesidad[3],Habilidad[2],Habilidad[8],Competencia[1]))
            enviar2.pack()
            enviar2.place(x=50,y=170)
            enviar2 = Button(raiz, text="Gerente de Operaciones", foreground="lightcyan",bg="deepskyblue4",
                     font=("Arial",10),command=partial(Mostrar,Rol[3],Necesidad[1],Necesidad[3],Habilidad[1],Habilidad[7],Competencia[2]))
            enviar2.pack()
            enviar2.place(x=50,y=200)
            
            #Operacional
            Operacional1 = Label(raiz, text="Operacional",bg="lightblue",font=("Arial"))
            Operacional1.pack()
            Operacional1.place(x=30,y=250)
            enviar3 = Button(raiz, text="Tecnico", foreground="lightcyan",bg="deepskyblue4",
                     font=("Arial",10),command=partial(Mostrar,Rol[4],Necesidad[0],Necesidad[4],Habilidad[3],Habilidad[9],Competencia[3]))
            enviar3.pack()
            enviar3.place(x=50,y=280)
            enviar3 = Button(raiz, text="Atención al Cliente", foreground="lightcyan",bg="deepskyblue4",
                     font=("Arial",10),command=partial(Mostrar,Rol[5],Necesidad[0],Necesidad[3],Habilidad[4],Habilidad[10],Competencia[4]))
            enviar3.pack()
            enviar3.place(x=50,y=310)
         
Rol=["Gerente General","Sub Gerente","Jefe de Proyecto","Gerente de Operaciones","Tecnico","Atención al Cliente"]            

Necesidad=["X","Y",'poder','afiliacion','identidad de la actividad']

Habilidad=['competitivo','emprendedor','comunicador','diciplinado','flexible','comunicador','armonico','responsable','desarrollador','analitico','empatico',"mandatario"]      

Competencia= ['orden y seguridad','intelectual','comportamiento','tecnicas','basicas']

def Mostrar(rol,nec1,nec2,hab1,hab2,com):
    raiz=Tk()
    raiz.resizable(1,0)
    raiz.config(bg="lightblue",bd=5,relief="groove")
    raiz.geometry("250x400")
    raiz.iconbitmap("images.ico")
    raiz.resizable(0,0)
    raiz.config(bg="lightblue",bd=5,relief="groove")
            
            
    frame=Frame(raiz,width=180,height=260)
    frame.place(x=30,y=70)
    frame.config(bd=5,relief="groove")
    #titulo
    label1=Label(raiz,text=rol, 
                 foreground="dodgerblue4",bg="lightblue",
                 font=("Arial Black",15))
    label1.place(x=30, y=10)
    
    label1=Label(raiz,text="Necesidades")
    label1.place(x=40, y=80)
    label1=Label(raiz,text=nec1)
    label1.place(x=60, y=100)
    label1=Label(raiz,text=nec2)
    label1.place(x=60, y=120)
    
    label1=Label(raiz,text="Habilidades")
    label1.place(x=40, y=160)
    label1=Label(raiz,text=hab1)
    label1.place(x=60, y=180)
    label1=Label(raiz,text=hab2)
    label1.place(x=60, y=200)
    
    label1=Label(raiz,text="Competencia")
    label1.place(x=40, y=240)
    label1=Label(raiz,text=com)
    label1.place(x=60, y=260)
    
 
    raiz.mainloop()