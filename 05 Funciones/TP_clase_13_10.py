import csv
import os
def escribir(nombre,precio):
        with open("productos.csv", "a", newline="") as archivo:
            escritor = csv.writer(archivo)
            escritor.writerow([nombre,precio])

def leer():
    try:
        with open("productos.csv", "r",newline="") as archivo:
            lector = csv.reader(archivo)
            for fila in lector:
                print(fila)
    except:
        print("Error en la lectura del archivo.")

def eliminar():
    ARCHIVO = "productos.csv"
    if not os.path.exists(ARCHIVO):
        print("No hay productos para eliminar.")
        return
    leer()
    try:
        eliminar_producto = input("Ingrese el producto que desea eliminar: ")
        with open(ARCHIVO, "r", newline="", encoding="utf-8") as archivo:
            lector = csv.reader(archivo)
            productos = [fila for fila in lector if fila and fila[0] != eliminar_producto]
        with open(ARCHIVO, "w", newline="", encoding="utf-8") as archivo:
            escritor = csv.writer(archivo)
            escritor.writerows(productos)
        print("Producto eliminado correctamente!")
    except:
        print("Error en el archivo. Por favor revisar")



while True:
    opcion = input("""
                   ====== MENÚ DE PRODUCTOS ======
                    1. Mostrar productos
                    2. Agregar producto
                    3. Eliminar producto
                    4. Salir
                   ===============================
                    Seleccione una opción: """)
    if opcion == "4":
        print("Saliendo del programa...")
        break
    elif opcion == "1":
        leer()
    elif opcion == "2":
         nombre = input("Ingrese nombre del producto: ")
         precio = input("Ingrese el precio: ")
         escribir(nombre,precio)
         leer()
    elif opcion == "3":
         eliminar()