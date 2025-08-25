print ("Ejercicio 1:")
print()
print ("Hola mundo!")
print()


print("Ejercicio 2")
nombre=input("Ingrese su nombre: ")
print (f"Hola {nombre}!")
print()


print("Ejercicio 3")
print()
#Tambien podria usar una lista o hacer varios input :3
#Estoy probando funciones 
nombre,apellido,edad,pais=input("Ingrese su nombre,apellido,edad y pais separado por espacios: ").split()
print()
print(f"Soy {nombre} {apellido} tengo {edad} y actualmente vivo en {pais}")
print()

#nota para la proxima:usar import math.pi
print("Ejercicio 4:")
print("----Calculador de perimetro----")
print()

radio=float(input("Ingrese el radio de su círculo: "))
pi=3.1416
perimetro=2*pi*radio

print("El perímetro de su círculo es ",perimetro)
print()


print("Ejercicio 5: ")
print()
#Si tambien hay que poner minutos, hay que sacar un resto y dividirlo por 60(lo mismo con segundos)
segundos=int(input("Ingrese la cantidad de segundos: "))
horas=segundos//3600

print("Sus segundos equivalen a",horas,"horas")
print()


print("Ejercicio  6: ")
print()
print("----Tabla de multiplicar----")

numero_tabla=int(input("Ingrese la tabla que desea: "))

print(f"{numero_tabla} x 1 = ",numero_tabla*1)
print(f"{numero_tabla} x 2 = ",numero_tabla*2)
print(f"{numero_tabla} x 3 = ",numero_tabla*3)
print(f"{numero_tabla} x 4 = ",numero_tabla*4)
print(f"{numero_tabla} x 5 = ",numero_tabla*5)
print(f"{numero_tabla} x 6 = ",numero_tabla*6)
print(f"{numero_tabla} x 7 = ",numero_tabla*7)
print(f"{numero_tabla} x 8 = ",numero_tabla*8)
print(f"{numero_tabla} x 9 = ",numero_tabla*9)
print(f"{numero_tabla} x 10 =",numero_tabla*10)
print()

print("Ejercicio 7: ")
print()
numero1=int(input("Ingrese el primer número: "))
numero2=int(input("Ingrese el segundo número"))

suma=numero1+numero2
resta=numero1-numero2
multi=numero1*numero2
div=numero1/numero2

print(f"La suma entre ellos es {suma},la resta es {resta}, la multiplicación es {multi}, y la division es {div}")
print()


print("----Ejercicio 8----")
print()
print("----Calculador de IMC----")
print()

peso=float(input("Ingrese su peso en KG: "))
altura=float(input("Ingrese su altura en centímetros (Ejemplo: 1.80)"))
imc=peso/altura**2
print()

print(f"Su IMC (índice de masa corporal) es de {imc:.2f}")#Nota: el ".2f" me redonde las ultimas 2 decimales
print()


print("Ejercicio 9: ")
print("----Convertidor de grados CELCIUS----")
print()
grados_celcius=float(input("Ingrese los grados celcius: "))
grados_faren=9/5*grados_celcius+32

print(f"{grados_celcius}º equivalen a {grados_faren:.2f}º farenheit")
print()

print("Ejercicio 10: ")
numeros=[]
numeros.append(float(input("Ingrese el primer número: ")))
numeros.append(float(input("Ingrese el segundo número: ")))
numeros.append(float(input("Ingrese el tercer número: ")))
#La funciona append agrega un elemento al final de la lista;
#Sum suma los numero de la listas y len devuelve la cntidad de elementos que hay en la lista;
promedio=sum(numeros)/len(numeros)

print()
print(f"El promedio de los tres números es:{promedio:.2f}")