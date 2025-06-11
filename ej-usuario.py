'''
crar un programa que permita al usuario gestionar una lista de tareas pendientes.
el menu debe mostrar las siguientes opciones:
1. Agregar tarea
2. Ver tareas pendientes
3. Marcar tarea como completada
4. Eliminar tarea
5. Salir

requisitos:
1. cada tarea debe ser presentada como un diccionario con las claves:
- 'descripcion': una cadena de texto que describe la tarea.
- 'completada': un booleano que indica si la tarea ha sido completada o no.
2. al agregar una tarea, el usuario debe ingresar la descripcion de la tarea. 
2.1. que la tarea se aguegue a la lista con "completada" como False.
3. Al seleccionar "Ver tareas", el programa debe mostrar una lista numerada de todas las tareas.
3.1. al ver las tareas deben mostrar un estado de: ([✓] si está completada, [ ] si no lo está).
4. Al seleccionar "Marcar como completada" debe solicitar al usuario el número de la tarea. 
4.1. el programa debe cambiar el booleano "completada" a True.
5. Al seleccionar "Eliminar tarea", el programa debe solicitar al usuario el número de la tarea a eliminar.
5.1. el programa debe eliminar la tarea de la lista.
6. Al seleccionar "Salir", el programa debe cerrar el programa.

'''

opcion = 0
tareas = []
while opcion != 5:
    print("1. Agregar tarea")
    print("2. Ver tareas pendientes")
    print("3. Marcar tarea como completada")
    print("4. Eliminar tarea")
    print("5. Salir")
    opcion = int(input("Elija una opcion: "))
    match opcion:
        case 1:
            descripcion = input("Ingrese la descripcion de la tarea: ")
            tarea = {'descripcion': descripcion, 'completada': False}
            tareas.append(tarea)
            print(f"Tarea '{descripcion}' agregada.")            
        case 2:
            print("Tareas pendientes:")
            for i, tarea in enumerate(tareas):
                print(f"{i+1}. {tarea['descripcion']}")
        case 3:
            print("Marcar tarea como completada")
            numero = int(input("Ingrese el numero de la tarea: "))
            if numero in range(1, len(tareas)+1):
                tareas[numero-1]['completada'] = True                
                print(f"Tarea {numero} marcada como completada.")
            else:
                print("Numero de tarea incorrecto.")
        case 4:
            print("Eliminar tarea")
            numero = int(input("Ingrese el numero de la tarea: "))
            if numero in range(1, len(tareas)+1):
                tareas.pop(numero-1)
                print(f"Tarea {numero} eliminada.")
            else:
                print("Numero de tarea incorrecto.")
        case 5:
            print("Saliendo.")
            opcion = 5
        case _:
            print("Opcion no valida.")
            print("Por favor, elija una opcion del menú.")

