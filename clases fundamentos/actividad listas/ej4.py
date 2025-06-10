'''
Cree un menú para registrar usuarios e iniciar sesión, también el menú tendrá la
opción de eliminar usuarios, para ello, utilice el nombre de usuario, además para
2
confirmar la eliminación, deberán escribir la contraseña correspondiente de cada
usuario.
1. Inicio sesión.
2. Registrar usuario
3. Eliminar usuario.
4. Salir.
La opción 1 sólo deberá mostrar un mensaje exitoso en caso de haber iniciado
correctamente, o un mensaje de error de caso contrario.
'''

usuarios = []
opcion = 0

while opcion != 4:
    print(usuarios)
    print("bienvenido usuario")
    print("1. Inicio sesión.")
    print("2. Registrar usuario.")
    print("3. Eliminar usuario.")
    print("4. Salir.")

    opcion = int(input(""))
    match opcion:
        case 1:

            username = input("ingrese su nombre de usuario: ")
            password = input("ingrese su contraseña")

            conectado = False

            for item in usuarios:
                if(item["username"] == username and item["password"] == password):
                    conectado = True
                    print("ha conectado con exito")
                else:
                    print("error en las credenciales")

        case 2:

            username = input("ingrese su nombre de usuario: ")
            password = input("ingrese su contraseña")
            usuario = {
                "username":username,
                "password":password
            }
            usuarios.append(usuario)
            print("ususario agregado con exito")

        case 3:

            username = input("ingrese su nombre de usuario: ")
            for item in usuarios:
                if item["username"] == username:
                    usuarios.remove(item)
                    print(f"usuario: {username} eliminado")
                    break

        case 4:

            print("gracias por su preferencia")

        case 5:

            print("opcion fuera de rango")














