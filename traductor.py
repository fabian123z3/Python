traductor={}
while True:
    print("""
    ---------------------
      Traductor ElvisTek
    ---------------------
  1.- Ingresa palabra en español e ingles
  2.- Traducir una palabra
  3.- Borrar una palabra
  4.- Listado de palabra
  5.- Salir
    """)
    op=input("Ingrese una opcion: ")
    if op=="1":
        palabra=int(input("Ingrese cantidad de palabras: "))
        españolp=input("Ingrese palabra en español: ")
        inglesp=input("Ingrese palabra en ingles: ")
        traductor[españolp]=inglesp
    elif op=="2":
        palabra_traducir=input("Ingrese la palabra en español: ")
        if palabra_traducir in traductor:
            mostrar=traductor.get(palabra_traducir)
            print("Traduccion de ingles: ",mostrar)
        else:
            print("La palabra no puede ser traducida.")
    elif op=="3":
        palabra_traducir=input("Ingrese una palabra que quiera eliminar: ")
        if palabra_traducir in traductor:
            eliminar=traductor.pop(palabra_traducir)
            print("Se ha completado la eliminacion.")
        else:
            print("No se ha encontrado la palabra que desea eliminar.")
    elif op=="4":
        print("Listado de palabras traducidas: ")
        for i in traductor:
            print(i,":",traductor[i])
    elif op=="5":
        print("""Gracias por preferirnos 
      ----------------------
        Traductor ElvisTek
      ----------------------  """)
        break
    else:
        print("Seleccione otra opcion.")
        