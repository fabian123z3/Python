diccionario = {}
while True:
    print(""""
    1. ingresar palabra en español:su traduccion en ingles")
    2. Borrar")
    3. Listar")
    4. Salir""")
    op=int(input("ingrese opcion: "))
    if op==1:
        
        palabra = input("palabra en español:traducción en ingles (pueden ser varias si se separan por coma): ")
        for i in palabra.split(","):
            key, dato = i.split(":")
            diccionario[key] = dato
        frase = input("palabras en español: ")
        for i in frase.split():
            if i in diccionario:
                print(diccionario[i], end=" ")
            else:
                print("su palabra no se encuentra en el diciconario")
    elif op==2:
        print(diccionario)
        palabra = input("Nombre la palabra para borrar:") 
        if palabra in diccionario:
            diccionario.pop(palabra)
        
    elif op == 3:
        for palabra, numero in diccionario.items():
            print(palabra,"-->",numero)
    elif op == 4:
        break
    else:
        print("Opción incorrecta")


