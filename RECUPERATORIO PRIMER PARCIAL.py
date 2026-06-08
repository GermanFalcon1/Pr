# ==============================
#  SUPERMERCADO PYTHON MARKET
# ==============================

codigos = [101,     102,   103    ]
nombres = ["Leche", "Pan", "Arroz"]
precios = [2500,    1800,  3200   ]
stocks  = [10,      20,    5      ]

opcion = "0"

while opcion != "7":

    print("")
    print("==============================")
    print("  SUPERMERCADO PYTHON MARKET  ")
    print("==============================")
    print("1. Cargar producto")
    print("2. Mostrar productos")
    print("3. Buscar producto por codigo")
    print("4. Ordenar productos por precio")
    print("5. Mostrar producto con menor stock")
    print("6. Calcular valor total del inventario")
    print("7. Salir")
    opcion = input("Elegi una opcion: ")

    match opcion:

        case "1":
            print("--- Cargar producto ---")

            codigo = int(input("Codigo del producto: "))
            nombre = input("Nombre del producto: ")
            precio = int(input("Precio del producto: "))
            stock  = int(input("Stock del producto: "))

            codigos.append(codigo)
            nombres.append(nombre)
            precios.append(precio)
            stocks.append(stock)

            print("Producto cargado correctamente.")

        case "2":
            print("--- Mostrar productos ---")

            i = 0
            while i < len(codigos):
                print("Codigo:", codigos[i])
                print("Nombre:", nombres[i])
                print("Precio:", precios[i])
                print("Stock: ", stocks[i])
                print("")
                i = i + 1

        case "3":
            print("--- Buscar producto por codigo ---")

            busqueda = int(input("Codigo a buscar: "))
            encontrado = False

            i = 0
            while i < len(codigos):
                print("Elemento", i+1, "-> codigo", codigos[i], end="")
                if codigos[i] == busqueda:
                    print(" -> coincide!")
                    print("Nombre:", nombres[i])
                    print("Precio:", precios[i])
                    print("Stock: ", stocks[i])
                    encontrado = True
                    break
                else:
                    print(" -> no coincide")
                i = i + 1

            if encontrado == False:
                print("No existe ese producto.")

        case "4":
            print("--- Ordenar por precio ---")

            n = len(codigos)
            i = 0
            while i < n - 1:
                j = 0
                while j < n - 1 - i:
                    if precios[j] > precios[j + 1]:
                        temp = precios[j];  precios[j] = precios[j+1];  precios[j+1] = temp
                        temp = codigos[j];  codigos[j] = codigos[j+1];  codigos[j+1] = temp
                        temp = nombres[j];  nombres[j] = nombres[j+1];  nombres[j+1] = temp
                        temp = stocks[j];   stocks[j]  = stocks[j+1];   stocks[j+1]  = temp
                    j = j + 1
                i = i + 1

            print("Productos ordenados de menor a mayor precio.")

        case "5":
            print("--- Producto con menor stock ---")

            indice_menor = 0
            i = 1
            while i < len(stocks):
                if stocks[i] < stocks[indice_menor]:
                    indice_menor = i
                i = i + 1

            print("Codigo:", codigos[indice_menor])
            print("Nombre:", nombres[indice_menor])
            print("Precio:", precios[indice_menor])
            print("Stock: ", stocks[indice_menor])

        case "6":
            print("--- Valor total del inventario ---")

            total = 0
            i = 0
            while i < len(codigos):
                subtotal = precios[i] * stocks[i]
                print(nombres[i], "->", precios[i], "x", stocks[i], "=", subtotal)
                total = total + subtotal
                i = i + 1

            print("Valor total:", total)

        case "7":
            print("Hasta luego!")

        case _:
            print("Opcion invalida.")
