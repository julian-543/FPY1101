'''
Cree un sistema de ventas de supermercado en el cual se pueda agregar productos
al carro de compras, las opciones del menú serán.
1. Agregar productos
2. Ver canasta
3. Ver total
4. Salir
• En agregar productos deberá mostrar un menú con 5 productos y sus precios
(creado por usted), cada vez que se seleccione un producto quedará
agregado en la lista.
• Ver canasta, es mostrar todos los productos seleccionados.
• Ver total, es mostrar el total a pagar por el cliente.
'''

opcion = 0
productos = []
while opcion != 4:
    print("1. Agregar productos")
    print("2. Ver canasta")
    print("3. Ver total")
    print("4. Salir")
    opcion = int(input("Elija una opcion: "))
    match opcion:
        case 1:
            print("Agregar productos")
            print("1. Agua")
            print("2. Cerveza")
            print("3. Frutas")
            print("4. Verduras")
            print("5. Pan")
            producto = int(input("Seleccione un producto: "))
            nombre = ""
            precio = 0

            match producto:
                case 1:
                    precio = 1000
                    nombre = "Agua"
                case 2:
                    precio = 2000
                    nombre = "Cerveza"
                case 3:
                    precio = 1500
                    nombre = "Frutas"
                case 4:
                    precio = 1200
                    nombre = "Verduras"
                case 5:
                    precio = 800
                    nombre = "Pan"
                case _:
                    print("Producto no valido")
                    continue
            productos.append({'nombre': nombre, 'precio': precio})
            print(f"{nombre} agregado al carro de compras")
        case 2:
            print("Ver canasta")
            if productos:
                print("Productos en la canasta:")
                for item in productos:
                    print(f"- {item['nombre']}: ${item['precio']}")
            else:
                print("La canasta está vacía.")
        case 3:
            print("Ver total")
            if productos:
                total = sum(item['precio'] for item in productos)
                print(f"Total a pagar: ${total}")
            else:
                print("La canasta está vacía.")
        case 4:
            print("Salir")
            opcion = 4
        case _:
            print("Opción no válida")
            print("Por favor, elija una opción del menú.")
