Lista = []
Operacion = 0

while True:
    Operacion = int(input("""
1. Añadir numero a la lista
2. Añadir número de la lista en una posición
3. Longitud de la lista
4. Eliminar el último número
5. Eliminar un número
6. Contar números
7. Mostrar números
8. Salir

 """))
    
    if (Operacion == 1):
        Num = int(input("Numero para añadir: "))
        Lista.append(Num)
        print(" Numero ", Num, " Se añadio a la lista")

    elif (Operacion == 2):
        Num = int(input("Numero: "))
        Ubicacion = int(input("En que ubicacion desea añadirla: ")) - 1

        if (len(Lista) >= Ubicacion):
            Lista[Ubicacion] = Num
            print("Se agrego el numero: ", Num, " a la ubicacion: ", str(Ubicacion + 1), " con exito")
        else:
            print("No existe la ubicacion")
    elif (Operacion == 3):
        print("Hay: ", str(len(Lista)), " palabras en la lista")
    elif (Operacion == 4):
        Indice = len(Lista) - 1
        UltimoNum = Lista[Indice]
        print("El ultimo numero de la lista es: ", str(UltimoNum))
        Lista.pop()
        print("El ultimo numero fue eliminado")
    elif (Operacion == 5):
        Indice = int(input("ingrese ubicacion a eliminar: "))
        if (len(Lista) >= Indice):
            print("la palabra que se eliminara es: ", Lista[Indice - 1])
            Lista.remove(Lista[Indice - 1])
        else:
            print("No existe palabra en este indice")
    elif (Operacion == 6):
        Num = int(input("Que numero quieres buscar: "))
        Cantidad = Lista.count(Num)

        if (Cantidad > 0):
            print("Hay ", Cantidad, " visualizacion de ", Num, " en la lista")
        else:
            print("No hay visualizacion de ", Num, " en la lista")
    else:
                 print(Lista)
    