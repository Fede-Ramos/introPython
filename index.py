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

#--------------------------------------------------------------------------------------------------------------------


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

     
#--------------------------------------------------------------------------------------------------------------------


#HOMEWORK NUMERO 5


#Investigar el metodo con el que se deben de realizar los sig enunciados: 
#1) Agregar el contenido de una lista en otra lista

l1 = [1, 2, 3]
l2 = [100, 200, 300]
l1.append(l2[0])
l1.append(l2[1])
l1.append(l2[2])
print(l1)
#Resultado esperado:
# l1 = [1, 2, 3, 100, 200, 300]

#2) Juntar los caracteres de una lista en una sola cadena de caracteres

l3 = ["h","o","l","a"] 
concat= ''.join(l3)
print(concat)
#nuevaLista= l3[0] + l3[1] + l3[2] + l3[3]
#print(nuevaLista)
#Resultado esperado:
#l3 = “hola”

#3) Convertir La Pimer Letra De Cada Palabra En Mayuscula

l3 = "este es un texto de pruebas"
mayus= l3.title()
print(mayus)
#Resultado esperado:
#l3 = "Este Es Un Texto De Pruebas"

#4) Remplazar las letras a, e, i, o, u por @, 3, 1, 0 , ~ respectivamente

l4 = "murcielago"
change= l4.replace('u', '~').replace('i', '1').replace('e', '3').replace('a', '@').replace('o', '0')
print(change)
#Resultado esperado:
# l4 = "m~rc13l@g0"

# s = "Naze"
# l = list(s)
# l[2] = 'm'
# s = "".join(l)
# print(s)

# s = "Naze"
# new_s = s.replace('z','m')
# print(new_s)

#5) Con un metodo, sumarle un valor a la variable

l5 = 24
lista= []
lista.append(l5)
suma= sum(lista, 25)
print(suma)
#Resultado esperado:
# l5 = 49

#--------------------------------------------------------------------------------------------------------------------

#HOMEWORK NUMERO 6

#Para esta actividad les dare un codigo con multiples errores que realize. Su tarea es corregirlo

class Automovil:

    

    velocidad = 100
    llantas = 4
    puertas = 4
    asientos = 4
    seguro = False
    encendido = False
    
    def __encender(self):
        self.encendido = True
        print('El vehiculo esta ON')

    def ejecutar_encender(self):
        self.__encender()    

    
    def acelerar(self):
        for rapidez in range(0, 100, 5):
         print('El vehiculo esta moviendose a ', rapidez ,'km/h')
            
         
    def frenar(self):
        while (self.velocidad > 0):
            print('Velocidad:', self.velocidad)
            self.velocidad -= 10
        print('El vehiculo esta deteniendose')
        
    
    def __apagar(self):
        self.encendido = False
        print('El vehiculo esta OFF')

    def ejecutar_apagar(self):
        self.__apagar()    

    
    def modificar_estado(self):
        if (self.encendido == False):
         self.encendido = True
         print('Se modifico el estado del vehiculo a ON')
        else: print('El vehiculo ya esta encendido')   
        


nuevoAuto = Automovil()

nuevoAuto.ejecutar_encender()
nuevoAuto.ejecutar_apagar()
nuevoAuto.modificar_estado()
nuevoAuto.acelerar()
nuevoAuto.frenar()



