'''
Cree una lista y comience a almacenar nombres, cada vez que se agregue un nombre
nuevo, el sistema preguntará si desea agregar otro nombre, deberá agregar nombres
hasta que la respuesta sea “no”, “No”, “nO” o “NO” (use funciones lower() y upper() )

Una vez ingresa n nombres, deberán eliminar el nombre con la menor cantidad de
caracteres
'''
nombre = []
opcion = ""
all = 0
while all == 0:
    nombre.append(input("ingrese su nombre: "))
    opcion = input("desea ingresar un nombre?: ")
    if opcion.lower() == "no":
        all = 1
    elif opcion.lower() == "si":
        all = 0
    else:
        print("ingresa si o no")
        break
print(nombre)

#solucion

nombres = []
opcion = "si"
while opcion == "no":
    nombre = input("ingrese nombre: ")
    nombres.append = nombre
    print("desea ingresar otro nombre?: ")
    opcion = input("si/no: ").lower()

menor = ""

print(nombres)

for item in nombres:
    if len(menor) == 0:
        menor = item
    if len(item) < len(menor):
        menor = item

print(f"nombre: {menor} sera eliminado")
nombres.remove(menor)
print(nombres)


