lista = [] 
opcion = "" 
while opcion != "4": 
    print("================================") 
    print("====== MENÚ DE OPCIONES ======") 
    print("================================") 
    print("1. Agregar, 2. Listar, 3. Eliminar, 4. Salir") 
    opcion = input("Seleccione una opción: ") 
    match opcion: 
        case "1": 
            name = input("Ingrese el nombre: ") 
            apellido = input("Ingrese el apellido: ")
            lista.append((name + " " + apellido)) 
            print("Elemento agregado.") 
        case "2": 
            print("Lista de nombres y apellidos:") 
            for item in lista: 
                print(f"{item}")
        case "3": 
            elemento = input("Ingrese el nombre o apellido a eliminar: ")
            for item in lista: 
                if elemento in item: 
                    lista.remove(item) 
                    print("Elemento eliminado.") 
                    break
        case "4": 
            print("Saliendo del programa") 
            break 
        case _: print("Opción inválida")