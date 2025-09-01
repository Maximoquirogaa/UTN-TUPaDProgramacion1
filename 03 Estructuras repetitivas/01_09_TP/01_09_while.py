#Ejercicio while 01/09

import random

print("Bienvenido al juegazo 'Piedra, Papel o Tijeras' o 'ca-chi-pum'")

# Marcadores
jugador_gana = 0
compu_gana = 0

while True:
    print("Elige una opción:")
    print("1. Piedra")
    print("2. Papel")
    print("3. Tijera")
    print("0. Salir")
    
    #Pedido de opciones
    opcion = input(" Tu jugada: ")

    if opcion == "0":
        print("\n Gracias por jugar.")
        break

    jugadas = ["Piedra", "Papel", "Tijera"] #Lista de las opciones
    jugador = jugadas[int(opcion) - 1] #Pasar la opcion a entero y restarle 1
    computadora = random.choice(jugadas) #Jugada/opcion random de la mquina

    print(f"\nTú elegiste: {jugador}")
    print(f"La computadora eligió: {computadora}")

    # Reglas y suma de los contadores
    if jugador == computadora:
        print("Empate")
    elif (jugador == "Piedra" and computadora == "Tijera") \
         or (jugador == "Tijera" and computadora == "Papel") \
         or (jugador == "Papel" and computadora == "Piedra"):
        print("¡Ganaste esta ronda!")
        jugador_gana += 1
    else:
        print("La computadora gana esta ronda.")
        compu_gana += 1

    # Mostrar marcador
    print(f"\nMarcador -> Tú: {jugador_gana} | Computadora: {compu_gana}")