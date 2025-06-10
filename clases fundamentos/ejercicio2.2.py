
"""
generar split en su nombre
esto genera una variable con 4 indices
de cada uno debe:
1. transformar la primera ubicacion a minuscula
2. transformar la segunda ubicacion a mayuscula
3. tomar tercera posicion y cortar las primeras 3 letras y reempalzar la posicion con esas 3 letras
4. generar y mostrar un saludo usando los indices con su nombre
4.1. el formato es "bienvenido {nombre} {apellidopaterno} {apellidomaterno}"
5 generar una variable que contenga la primera letra de cada nombre
5.1. formato ideal || julian antonio ignacio molina rojas || J A I M R
"""
nombre_com= "Julian Antonio Ignacio Molina Rojas" 
lista= nombre_com.split()
print(lista)
nombre=nombre_com[0:22]
nombre=nombre.lower()
print(nombre)
apellidopaterno=nombre_com[23:29]
apellidopaterno=apellidopaterno.upper()
print(apellidopaterno)
apellidomaterno=nombre_com[30:35]
apellidomaterno=apellidomaterno[0:3]
print(apellidomaterno)
print(f"bienvenido {nombre} {apellidopaterno} {apellidomaterno}")
print(nombre_com[0], nombre_com[7], nombre_com[15], nombre_com[23], nombre_com[30])
