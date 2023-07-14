nombre=input("indique nombre: ")
edad=input("indique su edad: ")
direccion=input("indique su direccion: ")
telefono=input("indique su telefono: ")
persona={"nombre":nombre,"edad":edad,"direccion":direccion,"telefono":telefono}
for key in persona:
    print(key,":",persona[key])