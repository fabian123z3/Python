diccionario = {}
while True:
    print("n/")
    print("1.-Ingresar palabra en español e ingles")
    print("2.-borrar")
    print("3.-listar")
    print("4.-salir")
    
    operacion=int(input("ingrese opcion: "))
    if operacion==1:
        palabra = input("ingrese una palabra en español:ahora ingrese su traducción en ingles (para agregar mas se debe agregar una coma): ")
        for p in palabra.split(","):
            key, dato = p.split(":")
            diccionario[key] = dato
        frase = input("ingrese una palabra en español: ")
        for p in frase.split():
            if p in diccionario:
                print("la traduccion de su palabra es:",diccionario[p], end=" ")
            else:
                print("su palabra no se encuentra en el diccionario")
    elif operacion==2:
        print(diccionario)
        palabra = input("ingrese una palabra para borrar:") 
        if palabra in diccionario:
            diccionario.pop(palabra)
        else:
            print("palabra no encontrada en el diccionario")
    elif operacion == 3:
        for palabra, traduccion in diccionario.items():
            print(palabra,"=",traduccion)
    elif operacion == 4:
        break
    else:
        print("Opción invalida")




