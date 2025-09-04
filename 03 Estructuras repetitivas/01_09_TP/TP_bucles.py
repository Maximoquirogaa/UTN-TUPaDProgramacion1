#Ejercicio FOR 01/09

#Declaracion de variables e inputs
alfabeto = "abcdefghijklmnñopqrstuvwxyz"

# Pedir corrimiento
corrimiento = int(input("Ingrese el corrimiento deseado: "))

#Repetirlo 5 veces
for j in range(5):
    mensaje = input(f"\nIngrese el mensaje #{j+1}: ")
    mensaje_cifrado = ""
    
    for letra in mensaje.lower():
        if letra in alfabeto:   # Buscar la posición
            for i in range(len(alfabeto)):
                if letra == alfabeto[i]:
                    nueva_pos = (i + corrimiento) % len(alfabeto)
                    mensaje_cifrado += alfabeto[nueva_pos]
    print(f"Mensaje cifrado #{j+1}: {mensaje_cifrado}")
