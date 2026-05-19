codigos = []
nombres = []
precios = []
stock = []
opcion = 0

# El menú principal se repite hasta que el usuario elija la opción 7
while opcion != 7:
    print("\n--- SUPERMERCADO PYTHON MARKET ---")
    print("1. Cargar producto")
    print("2. Mostrar productos")
    print("3. Buscar producto por código")
    print("4. Ordenar productos por precio")
    print("5. Mostrar producto con menor stock")
    print("6. Calcular valor total del inventario")
    print("7. Salir")
    
    opcion = int(input("\nSeleccionar una opcion: "))

    # Opcion 1 - cargar producto
    if opcion == 1:
        print("\n--- Cargar producto ---")
        
        # Validar código no repetido
        codigo_valido = False
        while not codigo_valido:
            nuevo_codigo = input("Código del producto: ")
            repetido = False
            for c in codigos:
                if c == nuevo_codigo:
                    repetido = True
                    break # Salir del for si ya encontramos una coincidencia
            
            if repetido:
                print("El código ya existe - ingresar uno diferente")
            else:
                codigo_valido = True

        # Pedir y validar nombre (que no esté vacío)
        nombre_valido = False
        while not nombre_valido:
            nuevo_nombre = input("Nombre del producto: ")
            if nuevo_nombre.strip() == "":
                print("El nombre no puede estar vacío.")
            else:
                nombre_valido = True

        # Validar precio (mayor a cero)
        precio_valido = False
        while not precio_valido:
                nuevo_precio = float(input("Precio: "))
                if nuevo_precio <= 0:
                    print("El precio debe ser mayor a cero.")
                else:
                    precio_valido = True
                print("Por favor, ingrese un número válido para el precio.")

        # Validar stock (no negativo)
        stock_valido = False
        while not stock_valido:
                nuevo_stock = int(input("Stock inicial: "))
                if nuevo_stock < 0:
                    print("El stock no puede ser negativo.")
                else:
                    stock_valido = True
                print("Por favor, ingrese un número válido para el stock.")

        # Agregar a las listas
        codigos.append(nuevo_codigo)
        nombres.append(nuevo_nombre)
        precios.append(nuevo_precio)
        stock.append(nuevo_stock)
        print("\nProducto cargado exitosamente")
    
    #opcion 2 - Mostrar Productos
    elif opcion == 2:
         print ("\n --- Lista de Productos ---")
         if (codigos) == 0:
              print ("No hay productos cargados")
         else:
              print (f)


