#Trabajo práctico ESTRUCTURAS REPETITIVAS
#Máximo Quiroga
#Comisión 4


#Ejercicio 1
#Range para el rango; si ponemos principio y fin incluye el primero pero el limite es -1(y si ponemos range (100) imprime desde el cero)

for num in range (1,101): 
    print(num)

print("----------------------------")

#Ejercicio 2

numero_usuario = input("Ingrese un número entero:   ")

print(f"Su numero contiene", len(numero_usuario) , "dígitos.")
print("----------------------------")

#Ejercicio 3

numero_1 = int(input("Ingrese el primer número:    "))
numero_2 = int(input("Ingrese el segundo número:    "))
resultado = 0

for num_compren in range((numero_1+1),numero_2):
    resultado = resultado + num_compren

print(f"El resultado de los números comprendidos es {resultado}.")
print("----------------------------")

#Ejercicio 4

salida = 1
suma_secuencia = 0 #Las defino afuera porque las uso de contenedores

while salida != 0: #While para el pedido y suma de numeros
    num_usuario = int(input("Ingrese un número! ('0' para salir) : "))
    salida = num_usuario
    suma_secuencia = suma_secuencia + num_usuario
    print(f"La suma de los anteriores es {suma_secuencia}")

print("----------------------------")

#Ejercicio 5

import random
intentos = 0
adivino = False
print("Bienvenido al juego 'ADIVINADOR'")

while adivino == False:
    compu_numero = random.randint(0,9)
    jugador_numero = int(input("Ingrese el número que cree que es:  "))
    
    if compu_numero == jugador_numero: #Compara; si los dos son iguales ganó si no vuelve arriba por que la condicion sigue en false
        print("Felicidades, GANASTE!")
        adivino = True
    else:
        print("Intenta de nuevo!")
        intentos = intentos + 1

print(f"Sus intentos fueron {intentos}")
print("----------------------------")

#Ejercicio 6

for num in range(99,1,-1):
    if num % 2 == 0:
        print(num)

print("----------------------------")

#Ejercicio 7

numero_usuario7 = int(input("Ingrese un numero positivo:    "))
resultado = 0
if numero_usuario7 > 0:
    for num in range (1,numero_usuario7):

        resultado = resultado + num
    
    print(f"El resultado de los números comprendidos es {resultado}.")
    print("----------------------------")

#Ejercicio 8
positivos = 0
negativos = 0
pares = 0
impares = 0


for i in range(1,5+1): #Solo cambiar el numero en range y poner 100
    numeritos = int(input(f"Ingrese el número #{i}: "))
    
    if numeritos > 0:
        positivos = positivos + 1
    else:
        negativos = negativos + 1
    #Podria hacer todo en un solo IF

    if numeritos % 2 == 0:
        pares = pares + 1
    else:
        impares = impares + 1

#Con tres comillas puedo escribir saltando lineas en vez del \n
print(f"""
    Positivos: {positivos}
    Negativos: {negativos}
    Pares: {pares}
    Impares: {impares}
      """)
print("----------------------------")

#Ejercicio 9 
import statistics
numeros_lista = []

for i in range (5):
    numero_del_usuario = int(input(f"Ingrese el número #{i+1}"))
    numeros_lista.append(numero_del_usuario) #Con el append le añado numeros a la lista, en este caso los que me da el usuario

print(f"La media de los números es {statistics.mean(numeros_lista)}") #El mean es para sacar la media de un grupo de numeros, por eso hice la lista
print("----------------------------")
#Ejercicio 10
digitos_usuario = int(input("Ingresa el numero a dar vuelta:    "))

voltear = int(str(digitos_usuario)[::-1])
#Use metodo slicing que lo pasa a string que extrae o corta partes de una cadena
#Tambien podria usar como haciamos en pseint con el metodo burbuja creo
#Seria muy tedioso
print(f"El número dado vuelta es: {voltear}")