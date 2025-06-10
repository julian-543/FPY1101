'''
Escriba un programa que permita almacenar 3 nombres solicitados por pantalla en
una lista, luego el sistema deberá mostrar el nombre que tenga mayor cantidad de
caracteres en un mensaje de salida por pantalla.
'''

nombre = []
for i in range(3):
    nombres = input("ingrese su nombre: ")
    if(nombres.__len__()>0):
        nombre.append(nombres)
    else:
        print("debe ingresar mas caracteres") 

mayor = ""

for item in nombre:
    if item.__len__() > mayor.__len__():
        mayor = item

print(f"el nombre con mayor cantidad de caracteres es: {mayor}")




