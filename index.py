#HOMEWORK NUMERO 2

"""
Realizar un programa que almacene en una variable si el numero actual es un numero par en un rango del 1 al 10000, utilizando solamente lo visto hasta el momento. 
#Puede que el operador modulo (%) te ayude

numero_actual = 0
while (condicion):
    verificar si numero_actual es par…

"""  

numero_actual= 50
while(numero_actual < 10000):
    if(numero_actual % 2 == 0):
        esPar= numero_actual
        print(esPar) 
    else: print(False)


"""
Realizar un programa que almacene en una variable el numero actual si es un numero primo, es decir, que solamente sean divisibles por si mismos y por uno sin que quede residuo (ejemplos: 2, 3, 5, 7 ,11 13, 17, 19, 23), en un rango del 1 al 10000. #Posiblemente tengas que anidar dos ciclos while.

"""    

numeroActual= 13
while(numeroActual < 10000):
    while(numeroActual % 2 == 0):
        print(False)
    else: esPrimo= numeroActual
    print(esPrimo)

#-----------------------------------------------------------------------------------------------


#HOMEWORK NUMERO 3

"""
Realizar un programa que almacene en una variable si el numero actual esta en una posicion par utilizando un bucle “for” #Se puede realizar con solamente las cosas que hemos visto hasta el momento


#Lorem tiene posición par, dolor tiene posición par, amet tiene posición par, adipiscing tiene posición par
elementos = ["Lorem", "ipsum", "dolor", "sit,", "amet", "consectetur", "adipiscing", "elit"]
for …:
    if…:        actual = …

"""
elementos = ["Lorem", "ipsum", "dolor", "sit,", "amet", "consectetur", "adipiscing", "elit"]

for i in elementos[0:8:2]:
    actual= i
    print(actual)
     
#------------------------------------------------------------------------------------------------    