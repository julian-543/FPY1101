'''
Cree 2 listas, en las cuales se guardará 3 nombres y 3 apellidos (1 lista para nombres
y una 1 lista para apellidos), el sistema deberá mostrar de forma ordenada los
nombres y apellidos
'''
nombres = []
apellidos = []

for i in range(3):
    nombres.append(input("ingrese su nombre: "))
    apellidos.append(input("ingrese su apellido: "))

nombres.sort()
apellidos.sort()
print(nombres)

for item in apellidos:
    print(item)
    