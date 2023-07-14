#practica de listas

lista= ["lunes","martes","miercoles","jueves","viernes"]
print(len(lista))
lista.append("sabado")
print(lista)
lista.insert(1,"tilin") 
print(lista)
lista.extend(["domingo"])
print(lista)
print("lunes" in lista)
if 10 in lista:
    print("bien")
else:
    print("mal")