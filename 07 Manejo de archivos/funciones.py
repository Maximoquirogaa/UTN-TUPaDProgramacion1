import os # Importamos os para verificar si el archivo existe

def mostrar_catalogo():
    if not os.path.exists("productos.txt"):
        print("El catálogo está vacío (el archivo no existe).")
        return
    with open("productos.txt", "r") as archivo:
        archivo.readline()
        for linea in archivo:
            if not linea.strip(): 
                continue
            
            datos = linea.strip().split(",")
        
            if len(datos) != 3:
                continue
            nombre, precio, cantidad = datos
            print(f"Producto: {nombre} | Precio: ${precio} | Cantidad: {cantidad}")

def cargar_productos():
    productos = []
    nombre_archivo = "productos.txt"

    if not os.path.exists(nombre_archivo):
        return [] 

    with open(nombre_archivo, "r") as archivo:
        for linea in archivo:
            linea = linea.strip()
            if not linea:
                continue 
            
            datos = linea.split(",")
            if len(datos) != 3:
                continue 

            nombre, precio, cantidad = datos
            
            try:
                producto = {
                    "nombre": nombre,
                    "precio": float(precio),
                    "cantidad": int(cantidad)
                }
                productos.append(producto)
            except ValueError:
                print("")
    return productos

def agregar_producto():
    nombre = input("Ingrese el nombre del producto: ").replace(",", "") 
    while True:
        try:
            precio = float(input("Ingrese el precio del producto: "))
            cantidad = int(input("Ingrese la cantidad: "))
            break
        except ValueError:
            print("Error: Precio y cantidad deben ser números.")

    with open("productos.txt", "a") as archivo:
        archivo.write(f"{nombre},{precio},{cantidad}\n")
    print("Producto agregado con éxito.\n")


def buscar_producto(productos):
    nombre_buscado = input("Ingrese el nombre del producto que desea buscar: ")
    encontrado = False
    for producto in productos:
        if producto["nombre"].lower() == nombre_buscado.lower():
            print(f"Producto encontrado: {producto['nombre']} | Precio: ${producto['precio']} | Cantidad: {producto['cantidad']}")
            encontrado = True
            break
    if not encontrado:
        print("Producto no encontrado.")

def guardar_productos(productos):
    with open("productos.txt", "w") as archivo:
        for producto in productos:
            linea = f"{producto['nombre']},{producto['precio']},{producto['cantidad']}\n"
            archivo.write(linea)
    print("Archivo actualizado correctamente.\n")