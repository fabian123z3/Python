agenda = {}
while True:
    print("\n")
    print("1. ingresar palabra en español:su traduccion en ingles")
    print("2. traducir")
    print("3. Borrar")
    print("4. Listar")
    print("5. Salir")
    agenda=int(input("ingrese opcion: "))
    if agenda==1:
        diccionario = {}
        palabras = input("escribe palabra en españos:su traduccion en ingles: ")
        for i in palabras.split(','):
            key, dato = i.split(':')
            diccionario[key] = dato
    elif agenda==2:
        frase = input("ingrese una frase en español")
        for i in frase.split():
            if i in diccionario:
                print(diccionario[i], end=" ")
            else:
                print(i, end=" ")
    elif agenda==3:
        palabra = input("Nombre del contacto para borrar:")    
        if palabra in agenda:
            opcion = input("Pulsa 's' si quieres borrarlo!!!. Otra tecla para continuar.")
            if opcion == "s":
                del agenda[palabra]
    elif agenda == 4:
        for palabra, numero in agenda.items():
            print(palabra,"->",numero)
    elif agenda == 5:
        break
    else:
        print("Opción incorrecta")



