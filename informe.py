monto = int(input("ingrese monto a calcular:  "))
mil = int(monto/1000)
milr = monto%1000
dosmil = int(monto/2000)
dosmilr = monto%2000
cincomil = int(monto/5000)
cincomilr = monto%5000
diezmil = int(monto/10000)
diezmilr = monto%10000
veintemil = int(monto/20000)
veintemilr = monto%20000
print("===")
print("Son",mil,"billetes de mil y sobran",milr)
print("son",dosmil,"billetes de dos mil y sobran",dosmilr)
print("son",cincomil,"billetes de cinco mil y sobran",cincomilr)
print("son",diezmil,"billetes de diez mil y sobran",diezmilr)
print("son",veintemil,"billetes de veinte mil y sobran",veintemilr)

    
    
    