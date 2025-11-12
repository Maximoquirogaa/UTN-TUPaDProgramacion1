import funciones


while True:
    print("\n=== Gestor de Productos ===")
    print("1. Mostrar productos")
    print("2. Agregar producto")
    print("3. Buscar producto")
    print("4. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        funciones.mostrar_catalogo()
    elif opcion == "2":
        funciones.agregar_producto()
    elif opcion == "3":
        productos = funciones.cargar_productos()
        funciones.buscar_producto(productos)
    elif opcion == "4":
        print("Saliendo del programa...")
        break
    else:
        print("Opción incorrecta")

