#Actividad de campus: Datos complejos
#Máximo Quiroga comisión 4
print("----Ejercicios 1----")

precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}

precios_frutas['Naranja'] = 1200
precios_frutas['Manzana'] = 1500
precios_frutas['Pera'] = 2300

print(f"Diccionario tras añadir frutas:\n{precios_frutas}")

print("----Ejercicios 2----")

precios_frutas['Banana'] = 1330
precios_frutas['Manzana'] = 1700
precios_frutas['Melón'] = 2800

print(f"\nDiccionario tras actualizar precios:\n{precios_frutas}")

print("----Ejercicios 3----")

lista_frutas = list(precios_frutas.keys())

print(f"\nLista de frutas (sin precios):\n{lista_frutas}")

print("\n--- Ejercicio 4: Agenda Telefónica ---")

agenda = {}

print("Por favor, ingresa 5 contactos.")
for i in range(5):
    nombre = input(f"Nombre del contacto {i+1}: ").capitalize() 
    numero = input(f"Número de {nombre}: ")
    agenda[nombre] = numero

busqueda = input("\nIngresa el nombre a buscar: ").capitalize()
numero_encontrado = agenda.get(busqueda, "El contacto no existe.")
print(f"El número de {busqueda} es: {numero_encontrado}")

print("\n----Ejercicio 5----")

frase = input("Ingresá una frase: ").lower() 
palabras = frase.split()

palabras_unicas = set(palabras)
print(f"\nPalabras únicas: {palabras_unicas}")

frecuencias = {}
for palabra in palabras:
    if palabra in frecuencias:
        frecuencias[palabra] += 1
    else:
        frecuencias[palabra] = 1

print(f"Frecuencia de palabras: {frecuencias}")

print("\n--- Ejercicio 6: Notas de Alumnos ---")

alumnos_notas = {}

for i in range(3):
    nombre = input(f"Nombre del alumno {i+1}: ")
    print(f"Ingresa las 3 notas para {nombre}:")
    n1 = float(input("Nota 1: "))
    n2 = float(input("Nota 2: "))
    n3 = float(input("Nota 3: "))
    
    alumnos_notas[nombre] = (n1, n2, n3)

print("\n--- Promedios ---")
for alumno, notas in alumnos_notas.items():
    promedio = sum(notas) / len(notas)
    print(f"{alumno}: {promedio:.2f}")

print("\n----Ejercicio 7----")

aprobados_parcial_1 = {"jose", "maxi", "giuli", "mile", "cris"}
aprobados_parcial_2 = {"maxi", "giuli", "santi", "cris", "markos"}

print(f"Aprobados P1: {aprobados_parcial_1}")
print(f"Aprobados P2: {aprobados_parcial_2}")

ambos = aprobados_parcial_1 & aprobados_parcial_2
print(f"\nAprobaron ambos parciales: {ambos}")

solo_uno = aprobados_parcial_1 ^ aprobados_parcial_2
print(f"Aprobaron solo uno de los dos: {solo_uno}")

total_aprobados = aprobados_parcial_1 | aprobados_parcial_2
print(f"Lista total de estudiantes (al menos uno aprobado): {total_aprobados}")


print("\n----Ejercicio 8----")

stock = {'Teclado': 10, 'Mouse': 25, 'Monitor': 5}

while True:
    print("\n1. Consultar Stock | 2. Agregar Stock/Producto | 3. Salir")
    opcion = input("Elige una opción: ")

    if opcion == "1":
        prod = input("Nombre del producto: ").capitalize()
        print(f"Hay {stock.get(prod, 0)} unidades de {prod}.")

    elif opcion == "2":
        prod = input("Nombre del producto: ").capitalize()
        cantidad = int(input("Cantidad a agregar: "))
        
        if prod in stock:
            stock[prod] += cantidad
            print(f"Stock actualizado. {prod}: {stock[prod]}")
        else:
            stock[prod] = cantidad
            print(f"Producto nuevo agregado. {prod}: {stock[prod]}")

    elif opcion == "3":
        break
    else:
        print("Opción inválida.")

print("\n----Ejercicio 9:----")

agenda_eventos = {
    ('Lunes', '08:00'): 'Clase de Python',
    ('Martes', '10:00'): 'Clase de matemática',
    ('Domingo', '20:00'): 'Juega River'
}

dia = input("Ingrese día (ej. Lunes): ").capitalize()
hora = input("Ingrese hora (ej. 08:00): ")

evento = agenda_eventos.get((dia, hora), "No hay actividades registradas.")
print(f"Actividad: {evento}")


print("\n----Ejercicio 10:----")

paises_capitales = {
    'Argentina': 'Buenos Aires',
    'España': 'Madrid',
    'Francia': 'París',
    'Japón': 'Tokio'
}

capitales_paises = {capital: pais for pais, capital in paises_capitales.items()}

print(f"Diccionario Original: {paises_capitales}")
print(f"Diccionario Invertido: {capitales_paises}")