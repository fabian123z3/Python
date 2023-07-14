agenda = {}
while True:
    print(""""
    1. ingresar palabra en español:su traduccion en ingles")
    2. traducir")
    3. Borrar")
    4. Listar")
    5. Salir""")
    agenda=int(input("ingrese opcion: "))
    if agenda==1:
        diccionario = {}
        palabras = input("escribe palabra en españos (luego : )y luego su traduccion en ingles: ")
        for i in palabras.split(","):
            key, dato = i.split(":")
            diccionario[key] = dato
    elif agenda==2:
        frase = input("ingrese una frase en ingles")
        for i in frase.split():
            if i in diccionario:
                print(diccionario[i], end=" ")
            else:
                print(i, end=" ")
    elif agenda==3:
        palabra = input("Nombre del contacto para borrar:")    
        if palabra in agenda:
            opcion = input("Pulsa 's' si quieres borrarlo y Otra tecla para continuar.").lower()
            if opcion == "s":
                del agenda[palabra]
    elif agenda == 4:
        for palabra, numero in agenda.items():
            print(palabra,"->",numero)
    elif agenda == 5:
        break
    else:
        print("Opción incorrecta")



