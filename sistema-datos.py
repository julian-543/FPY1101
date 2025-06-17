
'''
sistema para procesar y analizar datos
los datos se almacenan en un diccionario
cada llave es un identificador y el valor una lista con los datos del turista
los datos del turista son:
    nombre
    pais de origen
    fecha de ingreso a chile
Se pide un menú que tengas las siguientes funciones:

Cada opción del menú principal debe estar programada en una función externa al código principal (main). 

*** MENU PRINCIPAL ***
1.- Turistas por país:
    función llamada turistas_por_pais(pais)
    recibe como parámetro el nombre del país
    debe mostrar por pantalla una lista con los nombres de los turistas que pertenecen a ese país
2.- Turista por mes.
    función llamada turistas_por_mes(mes)
    recibe un mes como parámetro
    debe retornar el porcentaje de turistas que visito chile ese mes con respecto al total, redondeado a un decimal
    nota: el mes ingresado tiene que ser entre 1 y 12
    si no se cumple la nota se debe solicitar denuevo el mes hasta que sea correcto
    ejemplo: para febrero se debe ingresar 2, no 02
3.- Eliminar turista.
    funcion llamada eliminar_turista()
    no recibe parametros
    debe permitir ingresar el nombre del turista a eliminar
    debe funcionar independientemente si esta escrito en minusculas o mayusculas
    si se elimina un turista debe aparecer un mensaje de "tursita eliminado con exito"
    si no se elimina ningun turista debe aparecer un mensaje de "tursita no encontrado, no se pudo eliminar"
4.- Salir
    debe terminar el programa mostrando "programa terminado..."
si se ingresa una opcion distinta debe mostrar un mensaje de "opcion no valida, intente nuevamente"


'''

