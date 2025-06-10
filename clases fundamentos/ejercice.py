'''

gestionar las compras que realiza un cliente
pedir la cantidad de productos
generar un ciclo for segun la cantidad de productos quq el usuario requiere
finalizar con un mensaje indicado

cantidad de compras
total sin iva
total con iva
controlar 2 errores de codigo y uno general

'''
cantidad_productos = 0

total_con_iva = 0
total = 0
print("Bienvenido al sistema de compras")
try:
    cantidad_productos = int(input("Ingrese la cantidad de productos: "))
    if(cantidad_productos > 0):
        for 1 in range(1, cantidad_productos+1):
            precio = 0
            while (precio <= 0):
                precio = int(input("Ingrese el precio de cada producto: "))
                if (precio > 0):
                    total += precio
                    print(f"total actual: {total}")
                else:
                    print("el precio debe ser mayor a cero")
    
        total_con_iva = total * 0,19
        print(f"usted ha comprado {cantidad_productos} productos")
        print(f"total sin iva: ${total}")
        print(f"total con iva: ${total_con_iva}")

    else: 
        print("la cantidad de productos debe ser mayor a cero")
except ValueError as error:
    print(f"error: {error}")
    print("error: debe ingresar un numero entero")
except TypeError as error:
    print(f"error: {error}")
    print("error: tipo de dato incorrecto")
except:
    print("error del sistema")

