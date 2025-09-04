#Trabajo práctico nº1 
#Máximo Quiroga

#Ejercicio 1

print("Desea saber si es mayor de edad?")
edad_1  =   int(input("Ingrese su edad: "))

if edad_1 >= 18:
    print("Usted es mayor de edad!")
else:
    print("Usted es menor de edad, lo lamento!")

#Ejercicio 2

print("APROBADO O DESAPROBADO")
nota_1  =   int(input("Ingrese su nota: "))

if nota_1 >= 6:
    print("Aprobado!")
else:
    print("Desaprobado!")

#Ejercicio 3

numero = int(input("Ingrese un número:  "))

if numero%2 == 0:
    print("El numero ingresado es par!")
else:
    print("Por favor ingrese un número par!")

#Ejercicio 4
edad_4 = int(input("Ingrese su edad:    "))
print("Pertenece a la categoría:    ")

if edad_4 >= 12 and edad_4 < 18:
    print("Adolecente")
elif edad_4 >=18 and edad_4 < 30:
    print("Adulto/a joven")
elif edad_4 >= 30:
    print("Adulto/a mayor")
else:
    print("Niño/a")

#Ejercicio 5
contraseña = input("Ingrese una contraseña (mínimo 8  y máximo 14 caracteres)  :")
longitud = len(contraseña)

if 8 <= longitud <= 14:
    print("Ha ingresado una contraseña correcta!")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")

#Ejercicio 6
import random
from statistics import median, mode, mean

numeros_randoms = [random.randint(1,100) for i in range(50)]
moda = mode(numeros_randoms)
media = mean(numeros_randoms)
mediana = median(numeros_randoms)
#Logs
#print(media)
#print(mediana) 
#print(moda)

if media > mediana > moda:
    print("Sesgo positivo")
elif media < mediana < moda:
    print("Sesgo negativo")
else:
    print("Sin sesgo")

#Ejercicio 7
palabra = input("Ingrese una palabra: ")

ultima_letra = palabra[-1]  #Ultima letra de la palabra ingresada

if ultima_letra in "aeiou":#Si esta en ese string la ultima_letra pone el signo
    print(f"{palabra}!")
else:
    print(palabra)

#Ejercicio 8

nombre_8 = input("Ingrese su nombre: ")
opcion_8 = int(input("Ingrese '1' si desea su nombre en mayúsculas\nIngrese '2' si desea su nombre en minúsculas\nIngrese '3' si desea su nombre con la primera letra mayúscula."))

if opcion_8 not in (1,2,3): #If sobre las opciones
    print("Eliga una opcion correcta!")
elif opcion_8 == 1:
    print(nombre_8.upper())
elif opcion_8 == 2:
    print(nombre_8.lower())
else:
    print(nombre_8.capitalize())

#Ejercicio 9
temblor= float(input("Ingrese la magnitud del terremoto:    "))
categoria = ""

if temblor < 3:
    categoria = "Muy leve"
elif 3 <= temblor < 4:
    categoria = "Leve"
elif 4 <= temblor < 5:
    categoria = "Moderado"
elif 5 <= temblor < 6:
    categoria = "Fuerte"
elif 6 <= temblor < 7:
    categoria = "Muy fuerte"
else:
    categoria = "Extremo"

print(f"La categoría del terremoto es '{categoria}'")

#Ejercicio 10
hemisferio = input("Ingrese su hemisferio (norte/sur)  :").lower()
dia,mes=input("Ingrese la fecha (Ejemplo: 14 de febrero = 14/02)    :").split("/")
dia = int(dia)
mes = int(mes)

if hemisferio not in ("norte","sur"):
    print("Error en el ingreso de datos\nPruebe nuevamente")
else: #Asumimos que el primer hemisferio es el norte
        if (dia >= 21 and  mes == 12) or mes in (1,2) or (dia <= 20 and mes == 3):
            estacion = "Invierno"
        elif (dia >= 21 and mes == 3) or mes in (4,5) or (dia <= 20 and mes == 6):
            estacion = "Primavera"
        elif (dia >= 21 and mes == 6) or mes in (7,8) or (dia <= 20 and mes == 9):
            estacion = "Verano"
        else:
            estacion = "Otoño"

if hemisferio == "sur": #Los alterno manualmente para no repetir codigo
    if estacion == "Invierno":
        estacion = "Verano"
    elif estacion == "Primavera":
        estacion = "Otoño"
    elif estacion == "Verano":
        estacion = "Invierno"
    else:
        estacion = "Primavera"

print(f"La estación es: {estacion}")
