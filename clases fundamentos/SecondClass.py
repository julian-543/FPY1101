""" Segundas Clase """


nombre = "Pedro"

#Forma 1 - Concat con ,
print("Hola ",nombre," buen dia!")

#Forma 2 - Concat con format
print(f"Bienvenido {nombre} buen dia!")

#Asignaciones de valor
entero = 10 #int
decimal = 2.5 #float
texto = "Cadena de texto" # str
caracter = 'A' #chr
booleano = True #bool

#Input solicita default str
solicitud = input("Ingrese su nombre")
#int() = Parse o Casting de datos segun formato
solNumerica = int(input("Ingrese su numero"))

nombreCompleto = "Jose Riquelme Escobar"
#Retorna letra e
print(nombreCompleto[3])
#Retorna letra u
print(nombreCompleto[-5])
#Substring o corte de cadena 
#Slice [S,S,S] Start,Stop,Step
#Start = Inicio de corte
#Stop = Donde termina de cortar el String || Ubicacion - 1
#Step = De cuanto en cuanto 
print(nombreCompleto[0:4]) # Jose

""" 
strip = limpia las cadenas de espacios en blanco (Al inicio y al final)
lower = transforma toda la cadena a minuscula
upper = transforma toda la cadena a mayuscula
replace = Permite reemplazar un segmento de cadena por otro || Reemplaza A por B
find = Permite buscar una cadena y encontrar su posicion numerica en la palabra  
split = Divide el texto en una lista de palabras
"""
print(nombreCompleto.find(" "))
nombreCompleto = nombreCompleto.replace(" ","\t")
print(nombreCompleto)
lista = nombreCompleto.split()
