#crea un aplicativo con un menú repetitivo con 4 opciones 
# 1) agregar donde pedirá nombre y apellido y concatenados 
# los agregará en una lista 
# 2) listar que mostrará todos los nombres completos de esa lista y 
# 3) eliminar que pedirá un texto buscará ese texto y se le encuentra
# lo eliminará 
# 4) será para salir 


lista = [] 
opcion = "" 
while opcion != "4": 
    print("================================") 
    print("====== MENÚ DE OPCIONES ======") 
    print("================================") 
    print("1. Agregar") 
    print("2. Listar") 
    print("3. Eliminar") 
    print("4. Salir") 
    opcion = input("Seleccione una opción: ") 
    match opcion: 
        case "1": 
            name,apellido = input("Ingrese el nombre y apellido: ").split() 
            lista.append((name + " " + apellido)) 
            print("Elemento agregado.") 
        case "2": 
            print("Lista de nombres y apellidos:") 
            for item in lista: 
                print(f"\n{item}")
        case "3": 
            name,apellido = input("Ingrese el nombre y apellido a eliminar: ").split() 
            elemento = name + " " + apellido 
            if elemento in lista: 
                lista.remove(elemento) 
                print("Elemento eliminado.") 
            else: 
                print("Elemento no encontrado.") 
        case "4": 
            print("Saliendo del programa") 
            break 
        case _: print("Opción inválida")