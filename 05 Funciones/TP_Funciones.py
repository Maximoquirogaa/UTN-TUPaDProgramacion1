#FUNCIONES
#Trabajo práctico CAMPUS
#Máximo Quiroga

from math import pi
import statistics

def imprimir_hola_mundo():
    print("Hola mundo!")

def saludar_usuario(nombre):
    print(f"Hola {nombre}!")

def informacion_personal(nombre,apellido,edad,residencia):
    print(f" “Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}”")

def calcular_area_circulo(radio):
    area = pi*(radio**2)
    return area

def calcular_perimetro_circulo(radio):
    area = 2*pi*radio
    return area

def segundos_a_horas (segundos):
    horas = segundos/3600
    return horas

def tabla_de_multiplicar(num):
    for i in range(1,11):
        print(f"{i} x {num} = {(i*num)}")

def operaciones_basicas(a,b):
    tupla_operaciones = (a+b,a-b,a*b,a/b)
    return tupla_operaciones

def calcular_imc(peso,altura):
    imc = peso/altura**2
    return imc

def celsius_a_fahrenheit(celsius):
    fahrenheit = (celsius*1.8)+32
    return fahrenheit

def calcular_promedio(a,b,c):
    lista_numeros = [a,b,c]
    promedio = statistics.mean(lista_numeros)
    return promedio

#Main
print("------Ejercicio 1------")
imprimir_hola_mundo()

print("------Ejercicio 2------")
nombre = input("Ingrese su nombre: ")
saludar_usuario(nombre)

print("------Ejercicio 3------")
nombre,apellido,edad,residencia = input("Ingrese sus datos separados por comas: ").split(",")
informacion_personal(nombre,apellido,edad,residencia)

print("------Ejercicio 4------")
radio = int(input("Ingrese el radio del círculo: "))
print(f"El area es: {calcular_area_circulo(radio):.2f} cm")
print(f"El perímetro es: {calcular_perimetro_circulo(radio):.2f} cm")

print("------Ejercicio 5------")
segundos = int(input("Ingrese los segundos que quiere transformar: "))
print(f"Son {segundos_a_horas(segundos)} horas.")

print("------Ejercicio 6------")
tabla = int(input("Ingrese la tabla de multiplicar que desea: "))
tabla_de_multiplicar(tabla)

print("------Ejercicio 7------")
num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))

print(operaciones_basicas(num1,num2))

print("------Ejercicio 8------")
altura = float(input("Ingrese su altura (por ejemplo: 1.80): "))
peso = int(input("Ingrese su peso: "))

print(f"Tu IMC: {calcular_imc(peso,altura):.2f}")
      
print("------Ejercicio 9------")
grados = int(input("Ingrese su temperatura en celsius: "))
print(f"{grados}º celcis en fahrenheit es: {celsius_a_fahrenheit(grados):.2f}")

print("------Ejercicio 10------")
a = int(input("Ingrese el primer número: "))
b = int(input("Ingrese el segundo número: "))
c = int(input("Ingrese el tercer número: "))

print(f"El promedio es: {calcular_promedio(a,b,c):.2f}")