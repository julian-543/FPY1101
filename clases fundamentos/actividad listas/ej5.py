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
productos = []
opcion = 0
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
            match producto:
                case 1:
                    precio = 1000
                    print("Agua agregada al carro de compras")
                case 2:
                    precio = 2000
                    print("Cerveza agregada al carro de compras")
                case 3:
                    precio = 1500
                    print("Frutas agregadas al carro de compras")
                case 4:
                    precio = 1200
                    print("Verduras agregadas al carro de compras")
                case 5:
                    precio = 800
                    print("Pan agregado al carro de compras")
                case _:
                    print("Producto no valido")
        case 2:
            print("Ver canasta")
            if productos:
                print("Productos en la canasta:")
                for p in productos:
                    print(f"- {p['nombre']}: ${p['precio']}")
            else:
                print("La canasta está vacía.")
        case 3:
            print("Ver total")
            if productos:
                total = sum(p['precio'] for p in productos)
                print(f"Total a pagar: ${total}")
            else:
                print("La canasta está vacía.")
        case 4:
            print("Salir")
            opcion = 4
        case _:
            print("Opción no válida")
            print("Por favor, elija una opción del menú.")
            