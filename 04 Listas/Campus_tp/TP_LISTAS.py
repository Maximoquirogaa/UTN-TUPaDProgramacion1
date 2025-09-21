#Trabajo práctico LISTAS

#Máximo Quiroga
#Comisión 4

#Ejercicio 1
print("----------Ejercicio 1----------")
multiplo_cuatro = []
for i in range(0,101,4):
    multiplo_cuatro.append(i)
print(multiplo_cuatro)
#Ejercicio 2
print("----------Ejercicio 2----------")
videojuegos_lista = ["minecraft","red dead","call of duty","fifa","csgo"]
penultimo_elemento = videojuegos_lista[-2]
print(penultimo_elemento)

#Ejercicio 3
print("----------Ejercicio 3----------")
lista_vacia = []
for i in range(3):
    elemento = input(f"Ingrese el elemento nº{i+1}: " )
    lista_vacia.append(elemento)
print(lista_vacia)

#Ejercicio 4
print("----------Ejercicio 4----------")
animales = ["perro","gato","conejo","pez"]
segundo_elemento = input("Ingrese el reemplazo del segundo animal: ")
ultimo_elemento = input("Ingrese el reemplazo del ultimo animal: ")
animales[2] = segundo_elemento
animales[-1] = ultimo_elemento
print(animales)
#Ejercicio 5

#El max(numeros) identifica el numero mas alto dentro de la lista "numeros" 
# y el remove elimina el valor de la lista.

#Ejercicio 6
print("----------Ejercicio 6----------")
sexta_lista = []
for i in range(10,31,5):
    sexta_lista.append(i)
print(f"{sexta_lista[1]} y {sexta_lista[2]}")

#Ejercicio 7
print("----------Ejercicio 7----------")
autos = ["sedan","polo","suran","gol"]
autos[1:3] = ["virtus","vento"]
print (autos)

#Ejercicio 8
print("----------Ejercicio 8----------")
dobles = []
for i in range(1,16):
    if i in (5,10,15):
       dobles.append(i*2)
print(dobles)

#Ejercicio 9
print("----------Ejercicio 9----------")
compras = [["pan", "leche"], ["arroz", "fideos", "salsa"],
["agua"]]
compras[2].append("jugo")
compras[1][1] = "Tallarines"
compras[0].remove("pan")
print(compras)

#Ejercicio 10
print("----------Ejercicio 10----------")
lista_anidada = [[15], [True], [25.5,57.9,30.06],[False]]
print(lista_anidada)