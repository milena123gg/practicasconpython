#ARGUMENTOS POR VALOR Y POR REFERENCIA

#POR VALOR

# def triplicarNum(numero):
#     num = numero * 3
#     return num 


# num1 = 10 

# print(triplicarNum(num1)) #imprime 30

# print(num1) #imprime 10

#tupla

# def tuplaXlista(tupla):
#     return list(tupla)

# tup1 = (2,1)

# print( type(tuplaXlista(tup1))) #list

# print( type(tup1) ) #tuple


#POR REFERENCIA: DICCIONARIOS Y LISTAS

# def duplicarElementos(arreglo):
#     for numero in range(len(arreglo)):
#         arreglo[numero] *= 2
        
    

# listaNumerica = [1,2,3,4,5]

# duplicarElementos(listaNumerica) 


# print( listaNumerica ) #[2,4,6,8,10]


#SCOPE DE VARIABLES

# def saludarComision():
#     comision = 23417 #scope local
#     return f"Buenas tardess comision {comision}"



# print(saludarComision())

# print(comision)

#scope global

# comision = 23417 #scope global

# def saludarComision():    
#     return f"Buenas tardess comision {comision}"



# print(comision)

# print(saludarComision())

# CUANDO DOS IDENTIFICADORES COINCIDEN EN DISTINTOS AMBITOS



# def saludarComision():
#     comision = 7777   
#     print( id(comision) ) #7777
    
# comision = 23417
# saludarComision() #7777
#  #scope global
# print( id(comision) ) #23417



###GLOBAL

# comision = 23417 #scope global

# def saludarComision():
#     global comision
#     comision = 7777   #scope global
#     print( comision ) #7777

# saludarComision()

# print( comision ) #7777


# #ejemplo de una funcion

def convertirPesos(montoPesos, moneda):
    euro = 150
    dolar = 200
    pchileno = 180
    
    match moneda:
        case "euros":
            resultado = montoPesos / euro
        case "dolares":
            resultado = montoPesos / dolar
        case "chilenos":
            resultado = montoPesos / pchileno
        case _:
            resultado = "moneda ingresada invalida"
            
    return resultado


########## PROGRAMA PRINCIPAL



while True:
    print("###Bienvenido al CONVERSOR DE MONEDA###")
    pesosIngresados = float(input("Ingrese su monto en pesos:"))
    monedaIngresada = input("A que moneda desea convertir el monto?(euros/dolares/chilenos): ")
    
    print("Resultado:", convertirPesos(pesosIngresados,monedaIngresada) )
    
    continuar = input("Desea realizar otra conversion?(si/no)")
    
    if continuar == "no":
        break
    
print("Fin del programa")