#usar el solo el dev
def resta(a,b):
    r=a-b
    print(r)
    return print(a-b)
resta(b=30,a=9)

#usar el return
def prueba():
    return("plone",20,[1,2,3])
print(prueba())

#Calcular iva
def iva():
    iva=19
    costo= int(input("cual es el monto a calcular: "))
    calculo= costo*iva/100
    print("el calculo del iva es:" + str(calculo)+"\n")
iva()

#funcion con argumento multiple

def suma(num1,num2):
    print(num1+num2)
suma(25,29)