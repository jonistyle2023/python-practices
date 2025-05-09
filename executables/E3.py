# Crear un prgrama que permita mediante
# Estructuras de control selectivas de cascada

# Bloque de Instrucciones
#Inicializacion de variables
Er1=0
Er2=5
Er3=11
Er4=17
Er5=26
Er6=60

M1="Primera Infancia"
M2="Infancia"
M3="Adolecente"
M4="Juventud"
M5="Adulto"
M6="Adulto mayor"
M7=""

print("***************************")
print("*** EDAD DE UNA PERSONA ***")
print("***************************")
Ed=float(input("Ingrese la Edad: "))

#Proceso y Salida de datos
if (Ed>=Er1 and Ed<= Er2):
    print("",M1)
elif (Ed>=Er2 and Ed<= Er3):
    print("",M2)
elif (Ed>=Er3 and Ed<= Er4):
    print("",M3)
elif (Ed>=Er4 and Ed<= Er5):
    print("",M4)
elif (Ed>=Er5 and Ed<= Er6):
    print("",M5)
elif (Ed>=Er6):
    print("",M6)
else:
    print("",M7)