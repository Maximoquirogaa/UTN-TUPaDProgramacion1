
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

def probar_factorial():
    try:
        num = int(input("Ingrese un número límite para calcular factoriales: "))
        if num < 0:
            print("El factorial no está definido para números negativos.")
            return
        
        print(f"Factoriales desde 1 hasta {num}:")
        for i in range(1, num + 1):
            print(f"  {i}! = {factorial(i)}")
    except ValueError:
        print("Error: Ingrese un número entero válido.")

def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

def probar_fibonacci():
    try:
        pos = int(input("Ingrese una posición límite para la serie de Fibonacci: "))
        if pos < 0:
            print("Ingrese una posición positiva.")
            return
        
        print(f"Serie de Fibonacci hasta la posición {pos}:")
        serie = [fibonacci(i) for i in range(pos + 1)]
        print(serie)
    except ValueError:
        print("Error: Ingrese un número entero válido.")

def potencia(base, exponente):
    if exponente == 0:
        return 1
    return base * potencia(base, exponente - 1)

def probar_potencia():
    try:
        base = float(input("Ingrese el número base: "))
        exponente = int(input("Ingrese el exponente (entero no negativo): "))
        
        if exponente < 0:
            print("Esta función solo soporta exponentes no negativos.")
        else:
            resultado = potencia(base, exponente)
            print(f"{base} elevado a {exponente} es = {resultado}")
    except ValueError:
        print("Error: Ingrese números válidos.")

def decimal_a_binario(n):
    if n == 0:
        return ""
    return decimal_a_binario(n // 2) + str(n % 2)

def probar_binario():
    try:
        num = int(input("Ingrese un número decimal (entero positivo): "))
        if num < 0:
            print("Ingrese un número positivo.")
        elif num == 0:
            print("El binario es: 0")
        else:
            print(f"El binario de {num} es: {decimal_a_binario(num)}")
    except ValueError:
        print("Error: Ingrese un número entero válido.")


def es_palindromo(palabra):
    if len(palabra) <= 1:
        return True
    if palabra[0].lower() == palabra[-1].lower():
        return es_palindromo(palabra[1:-1])
    else:
        return False

def probar_palindromo():
    palabra = input("Ingrese una palabra (sin espacios ni tildes): ")
    if not palabra:
        print("No ingresó texto.")
        return
        
    if es_palindromo(palabra):
        print(f"'{palabra}' SÍ es un palíndromo.")
    else:
        print(f"'{palabra}' NO es un palíndromo.")

def suma_digitos(n):
    if n < 10:
        return n
    
    return (n % 10) + suma_digitos(n // 10)

def probar_suma_digitos():
    try:
        num = int(input("Ingrese un número entero positivo: "))
        resultado = suma_digitos(num)
        print(f"La suma de los dígitos de {num} es: {resultado}")
    except ValueError:
        print("Error: Ingrese un número entero válido.")

def contar_bloques(n):
    if n <= 1:
        return 1
    return n + contar_bloques(n - 1)

def probar_bloques():
    try:
        num = int(input("Ingrese el número de bloques en el nivel más bajo (n): "))
        if num <= 0:
            print("El número debe ser 1 o mayor.")
            return
        
        resultado = contar_bloques(num)
        print(f"Una pirámide con base {num} necesita un total de {resultado} bloques.")
    except ValueError:
        print("Error: Ingrese un número entero válido.")
def contar_digito(numero, digito):

    if numero == 0:
        return 0

    ultimo_digito = numero % 10
    conteo = 0
    if ultimo_digito == digito:
        conteo = 1
    return conteo + contar_digito(numero // 10, digito)

def probar_contar_digito():
    try:
        numero = int(input("Ingrese el número entero positivo: "))
        digito = int(input("Ingrese el dígito (0-9) que desea contar: "))
        
        if not (0 <= digito <= 9):
            print("El dígito debe estar entre 0 y 9.")
            return
        if numero < 0:
            numero = abs(numero)
        if numero == 0 and digito == 0:
            print(f"El dígito {digito} aparece 1 vez.")
            return

        resultado = contar_digito(numero, digito)
        print(f"El dígito {digito} aparece {resultado} veces en {numero}.")
    except ValueError:
        print("Error: Ingrese números enteros válidos.")


def main_menu():
    while True:
        opcion = input("""
                    ===============================
                     MENÚ DE EJERCICIOS RECURSIVOS 
                    ===============================
                    1. Factorial 1 a N
                    2. Serie de Fibonacci hasta N
                    3. Potencia
                    4. Decimal a Binario
                    5. Palíndromo
                    6. Suma de Dígitos
                    7. Pirámide de Bloques
                    8. Contar Dígito Específico
                    9. Salir
                    Ingrese una opción: """)
        try:
            match opcion:
                case '1':
                    probar_factorial()
                case '2':
                    probar_fibonacci()
                case '3':
                    probar_potencia()
                case '4':
                    probar_binario()
                case '5':
                    probar_palindromo()
                case '6':
                    probar_suma_digitos()
                case '7':
                    probar_bloques()
                case '8':
                    probar_contar_digito()
                case '9':
                    print("Saliendo...")
                    break

        except ValueError:
            print("Opción no válida. Intente de nuevo.")
            continue


if __name__ == "__main__":
    main_menu()