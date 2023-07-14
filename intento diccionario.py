diccionario = {}
palabra=0
while True:
    print("Traductor De gerentes")
    print("1.-Ingresar palabra en español e ingles")
    print("2.-Borrar")
    print("3.-listar")
    print("4.-salir")
    diccionario = input("Ingrese una opcion: ")
    if palabra == 1:
        diccionario = {}
        palabra= input("ingrese palabra en español:ingrese su traduccion en ingles: ")
    print("palabra añadida")
