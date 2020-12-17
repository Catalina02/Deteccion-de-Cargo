from main import*
# lista de roles

gerenteGeneral=["y","poder","orden y seguridad","competitivo","comunicador"]
subGerenteGeneral=["y","afiliacion","orden y seguridad","competitivo","armonico"]
gereteOperaciones=["y","afiliacion","intelectual","emprendedor", "responsable"]
jefeProyecto=["y","afliacion","comportamiento","comunicador","desarrollador"]
tecnico=["x","identidad de la actividad","tecnicas","diciplinado","analitico"]
atencionCliente=["x","afiliacion","basicas","flexible","empatico"]

# aplicacion
app = tk.Tk()
window = Ventana(app)
app.mainloop()


matriz=[[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
def ingresoDatos():
    porcentajes=[0,0,0,0,0,0]

    necesidad1=input("Ingrese X/Y: ")
    necesidad2=input("ingrese necesidad 2: ")
    competencia=input("Ingrese competencia: ")
    habilidad1=input("ingrese habilidad 1: ")
    habilidad2=input("ingrese habilidad 2: ")
    if (necesidad1 == "x"):
        matriz[4][0]=5
        matriz[5][0]=5
    if (necesidad1 == "y"):
        matriz[0][0]=5
        matriz[1][0]=5
        matriz[3][0]=5
        matriz[2][0]=5
    if (necesidad2 == "afiliacion"):
        matriz[1][1]=2
        matriz[2][1]=2
        matriz[3][1]=2
        matriz[5][1]=2
    if (necesidad2 == "poder"):
        matriz[0][1]=2
    if (necesidad2 == "identidad de la actividad"):
        matriz[4][1]=2
    if (competencia == "orden y seguridad"):
        matriz[0][2]=2
        matriz[1][2]=2
    if (competencia == "intelectual"):
        matriz[2][2]=2
    if (competencia == "comportamiento"):
        matriz[3][2]=2
    if (competencia == "tecnicas"):
        matriz[4][2]=2
    if (competencia == "basicas"):
        matriz[5][2]=2
    if (habilidad1 or habilidad2 == "competitivo"):
        matriz[0][3]=2
        matriz[1][3]=2
    if (habilidad1 or habilidad2 == "emprendedor"):
        matriz[2][3]=2
    if (habilidad1 or habilidad2 == "comunicador"):
        matriz[3][3]=2
        matriz[0][4]=2
    if (habilidad1 or habilidad2 == "diciplinado"):
        matriz[4][3]=2
    if (habilidad1 or habilidad2 == "flexible"):
        matriz[5][3]=2
    if (habilidad1 or habilidad2 == "armonico"):
        matriz[1][4]=2
    if (habilidad1 or habilidad2 == "responsable"):
        matriz[2][4]=2
    if (habilidad1 or habilidad2 == "desarrollador"):
        matriz[3][4]=2
    if (habilidad1 or habilidad2 == "analitico"):
        matriz[4][4]=2
    if (habilidad1 or habilidad2 == "empatico"):
        matriz[5][4]=2
    for i in range(0,len(matriz)):
        cont=0
        for j in range(0,len(matriz[i])):
            cont+=matriz[i][j]
        porcentajes[i]=(cont/14)*100
    return porcentajes

