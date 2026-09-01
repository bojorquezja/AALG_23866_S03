lista = [] 
opcion = "" 
while opcion != "4": 
    print("================================") 
    print("====== MENÚ DE OPCIONES ======") 
    print("================================") 
    print("1. Agregar, 2. Listar, 3. Eliminar, 4. Salir") 
    opcion = input("Seleccione una opción: ") 
    if opcion == "1": 
        name = input("Ingrese el nombre: ") 
        apellido = input("Ingrese el apellido: ")
        lista.append((name + " " + apellido)) 
        print("Elemento agregado.") 
    elif opcion == "2": 
        print("Lista de nombres y apellidos:") 
        for item in lista: 
            print(f"{item}")
    elif opcion == "3": 
        elemento = input("Ingrese el nombre o apellido a eliminar: ")
        for item in lista: 
            if elemento in item: 
                lista.remove(item) 
                print("Elemento eliminado.") 
                break
    elif opcion == "4": 
        print("Saliendo del programa") 
        break 
    else: 
        print("Opción inválida")