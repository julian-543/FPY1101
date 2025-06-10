'''
programa para ayudar en la venta de pasajes
1.1 inicia preguntando cuantos pasajes desea vender
1.2 utilizar bucle for para pedir el precio de cada pasaje por separado
1.3 si se ingresa un valor que no es un numero, se debe mostrar un mensaje de error y se sale del bucle con un break
1.4 al final, muestra el monto total que se obtuvo por la venta de los pasajes
'''
total = 0
pasajes = int(input("ingrese la cantidad de pasajes que  desea vender: "))
for i in range(pasajes):
        try:
            precio = float(input(f"ingrese el precio de los pasajes por separado: "))
        except ValueError:
            print("el valor debe ser un numero")
            break
        if precio < 0:
            print("el precio debe ser positivo")
            break
        else:
            total += precio
            print(f"el total de la venta es: {total}")

'''
segunda forma de realizar el ejercicio
'''           
total = 0
pasajes = int(input("ingrese la cantidad de pasajes que  desea vender: "))
for i in range(pasajes):
        try:
            precio = float(input(f"ingrese el precio de los pasajes por separado: "))
        except ValueError:
            print("el numero debe ser un numero")
            break
        else:
            total += precio
            print(f"el total de la venta es: {total}")


