import os
os.system("cls")
import random

lista=[]

def precio_cert():
    while True:
        try:
            precio1=int(input("Ingrese el precio del certificado de nacimiento (entre 1500 y 3000) : "))
        except:
            precio1=0
        
        if precio1 <1500 or precio1> 3000:
            print("Precio Ingresado incorrecto")
        else:
            break
    
    while True:
        try:    
            precio2=int(input("Ingrese el precio del certificado de estado conyugal (entre 1500 y 3000) : "))
        except:
            precio2=0
        
        if precio1 <1500 or precio1> 3000:
            print("Precio Ingresado incorrecto")
        else:
            break
    
    while True:    
        try:    
            precio3=int(input("Ingrese el precio de pertenencia a la union europea  (entre 1500 y 3000) : "))
        except:
            precio3=0
        
        if precio1 <1500 or precio1> 3000:
            print("Precio Ingresado incorrecto")
        else:
            break
            
    

def grabar_persona():
    print("Rigistrar")
    while True:
        nif=input("Ingrese Numero De Identificacion Fiscal (Tienen que ser 8 numeros y 3 letras en MAYUSCULAS ejemplo: 00000000-XXX) : ")
        validacion=nif.replace(" ","")
        if len (validacion) <12:
            print("NIF invalido, faltan numeros o letras")
        else:
            break
    
    while True:
        nombre=input("Ingrese Nombre : ")
        validacionnom=nombre.replace(" ","")
        if len (validacionnom) <8:
            print("Nombre Invalido, tiene que ser mas largo")
        else:
            break
    
    while True:
        try:
            edad=int(input("Ingrese edad "))
        except:
            edad=-1
            
        if edad<0:
            print("Edad invalida")
        else:
            break
    
    persona={
        'NIF' : nif,
        'Nombre' : nombre,
        'Edad' : edad
    }            

    lista.append(persona)
    
def buscar_persona():
    print("Buscar persona")
    while True:
        nif=input("Ingrese NIF de la persona registrada : ")
        if "SP" not in nif:
            print("Pertenece a la Union Europea")
        else:
            print("Pertenece a España")
            
        for persona in lista:
            if persona['NIF']==nif:
                print(persona)
                return
            break
        
        print("NIF ingresado no valido")
    
    
    
def imprimir_certificados():
    print("Imprimir Certificados")
    while True:
        nif=input("Ingrese NIF de la persona registrada : ")
        for persona in lista:
            if persona['NIF']==nif:
                return
            break
                
                
                
        print("NIF ingresado no valido")
                
    
def salir():
    print("Chao")
    print("Salir...")
    


precio_cert()
    
while True:
    print("\t Menu")
    print("1-Rigitrar datos")
    print("2-Buscar persona")
    print("3-Imprimir Certificados")
    print("4-Salir")
    
    try:
        op=int(input("Seleccione una opcion : "))
    except:
        op=0
        
    if op==1:
        grabar_persona()
    elif op==2:
        buscar_persona()
    elif op==3:
        imprimir_certificados()
    elif op==4:
        salir()
        break
    else:
        print("Opcion no valida")