import json, csv

ARCHIVO = "productos.json"


# ---------------- VALIDACIONES ----------------

def es_entero(cadena):
    if cadena == "":
        return False
    if cadena[0] == "-":
        cadena = cadena[1:]
    for c in cadena:
        if c < "0" or c > "9":
            return False
    return True

def es_numero(cadena):
    # admite enteros y decimales (para el precio), con un solo punto
    if cadena == "":
        return False
    if cadena[0] == "-":
        cadena = cadena[1:]
    puntos = 0
    for c in cadena:
        if c == ".":
            puntos += 1
        elif c < "0" or c > "9":
            return False
    return puntos <= 1

def pedir_entero(mensaje):
    while True:
        entrada = input(mensaje)
        if es_entero(entrada):
            valor = int(entrada)
            if valor >= 0:
                return valor
        print("Ingrese un número entero válido (mayor o igual a 0).")

def pedir_precio(mensaje):
    while True:
        entrada = input(mensaje)
        if es_numero(entrada):
            valor = float(entrada)
            if valor > 0:
                return valor
        print("Ingrese un precio válido (mayor a 0).")

def pedir_texto(mensaje):
    while True:
        texto = input(mensaje).strip()
        if texto != "":
            return texto
        print("Este campo no puede quedar vacío.")


##################
# json

def cargar_productos():
    try:
        with open(ARCHIVO, "r", encoding="utf-8") as archivo:
            return json.load(archivo)
    except FileNotFoundError:
        print(f"No se encontró '{ARCHIVO}'. Se iniciará un catálogo vacío.")
        return []
    except json.JSONDecodeError:
        print("El archivo JSON está corrupto. Se iniciará un catálogo vacío.")
        return []

def guardar_productos(lista):
    try:
        with open(ARCHIVO, "w", encoding="utf-8") as archivo:
            json.dump(lista, archivo, indent=4, ensure_ascii=False)
        print("Cambios guardados correctamente")
    except OSError as error:
        print(f"Error al guardar el archivo: {error}")


##########################
# crud

def listar_productos(lista):
    if len(lista) == 0:
        print("El catálogo está vacío.")
        return
    for producto in lista:
        print(f"ID: {producto['id']} | Nombre: {producto['nombre']}")
        print(f"Categoría: {producto['categoria']}")
        print(f"Precio: ${producto['precio']}")
        print(f"Stock: {producto['stock']}")
        print("-" * 37)

def buscar_producto(lista, nombre):
    for i in range(len(lista)):
        if lista[i]["nombre"].lower() == nombre.lower():
            return i
    return -1

def obtener_nuevo_id(lista):
    mayor = 0
    for producto in lista:
        if producto["id"] > mayor:
            mayor = producto["id"]
    return mayor + 1

def agregar_producto(lista):
    nombre = pedir_texto("Nombre: ")
    categoria = pedir_texto("Categoría: ")
    precio = pedir_precio("Precio: ")
    stock = pedir_entero("Stock: ")
    nuevo_id = obtener_nuevo_id(lista)
    lista.append({
        "id": nuevo_id,
        "nombre": nombre,
        "categoria": categoria,
        "precio": precio,
        "stock": stock
    })
    print(f"Producto agregado correctamente con ID {nuevo_id}.")

def modificar_stock(lista):
    nombre = input("Nombre: ")
    pos = buscar_producto(lista, nombre)
    if pos >= 0:
        nuevo = pedir_entero("Nuevo stock: ")
        lista[pos]["stock"] = nuevo
        print("Stock actualizado correctamente.")
    else:
        print("No encontrado.")

def eliminar_producto(lista):
    nombre = input("Nombre a eliminar: ")
    pos = buscar_producto(lista, nombre)
    if pos >= 0:
        lista.pop(pos)
        print("Eliminado.")
    else:
        print("No existe.")


# ------------------------- consultas ---------------------------

def productos_por_categoria(lista):
    if len(lista) == 0:
        print("El catálogo está vacío.")
        return

    categorias = {}
    for p in lista:
        if p["categoria"] in categorias:
            categorias[p["categoria"]].append(p["nombre"])
        else:
            categorias[p["categoria"]] = [p["nombre"]]

    for c in categorias:           # recorremos solo las claves
        print(f"{c}:")
        nombres = categorias[c]    # accedemos al valor con la clave
        for n in nombres:
            print(" -", n)

def mostrar_estadisticas(lista):
    if len(lista) == 0:
        print("El catálogo está vacío. No hay estadísticas para mostrar.")
        return

    print("Cantidad de productos:", len(lista))

    total_stock = 0
    valor_total_inventario = 0
    for p in lista:
        total_stock += p["stock"]
        valor_total_inventario += p["precio"] * p["stock"]
    print("Stock total:", total_stock)
    print(f"Valor total del inventario: ${valor_total_inventario:.2f}")

    mas_caro = lista[0]
    mas_barato = lista[0]
    for p in lista:
        if p["precio"] > mas_caro["precio"]:
            mas_caro = p
        if p["precio"] < mas_barato["precio"]:
            mas_barato = p
    print(f"Producto más caro: {mas_caro['nombre']} (${mas_caro['precio']})")
    print(f"Producto más barato: {mas_barato['nombre']} (${mas_barato['precio']})")

    categorias = {}
    for p in lista:
        if p["categoria"] in categorias:
            categorias[p["categoria"]] += 1
        else:
            categorias[p["categoria"]] = 1

    print("Productos por categoría:")
    for c in categorias:            # recorremos solo las claves
        cant = categorias[c]        # accedemos al valor con la clave
        print(f"{c}: {cant}")


###################

def exportar_csv(lista):
    if len(lista) == 0:
        print("El catálogo está vacío. No se generó el archivo CSV.")
        return

    encabezados = ["id", "nombre", "categoria", "precio", "stock"]

    try:
        with open("reporte_productos.csv", "w", encoding="utf-8") as archivo:
            archivo.write(",".join(encabezados) + "\n")
            for producto in lista:
                fila = [
                    str(producto["id"]),
                    producto["nombre"],
                    producto["categoria"],
                    str(producto["precio"]),
                    str(producto["stock"])
                ]
                archivo.write(",".join(fila) + "\n")
        print("Reporte exportado correctamente a 'reporte_productos.csv'.")
    except OSError as error:
        print(f"Error al exportar el archivo CSV: {error}")


############################
# ---------------- MENÚ ----------------

def menu():
    productos = cargar_productos()
    while True:
        print("\n--- Menú Supermercado ---")
        print("1. Listar productos")
        print("2. Agregar producto")
        print("3. Buscar producto por nombre")
        print("4. Modificar stock")
        print("5. Eliminar producto")
        print("6. Mostrar productos por categoría")
        print("7. Mostrar estadísticas")
        print("8. Exportar reporte CSV")
        print("9. Guardar y salir")

        opcion = input("Opción: ")

        match opcion:
            case "1":
                listar_productos(productos)
            case "2":
                agregar_producto(productos)
            case "3":
                nombre = input("Nombre: ")
                pos = buscar_producto(productos, nombre)
                if pos >= 0:
                    producto = productos[pos]
                    print(f"ID: {producto['id']} | Nombre: {producto['nombre']}")
                    print(f"Categoría: {producto['categoria']}")
                    print(f"Precio: ${producto['precio']}")
                    print(f"Stock: {producto['stock']}")
                else:
                    print("No encontrado.")
            case "4":
                modificar_stock(productos)
            case "5":
                eliminar_producto(productos)
            case "6":
                productos_por_categoria(productos)
            case "7":
                mostrar_estadisticas(productos)
            case "8":
                exportar_csv(productos)
            case "9":
                guardar_productos(productos)
                break
            case _:
                print("Opción inválida")

menu()
