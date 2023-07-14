#calcular sueldo base
def calcular_base(hrs, monto):
    sueldoBase = monto*hrs

    descuentoIsapre = (7*sueldoBase) / 100
    descuentoAfp = (10*sueldoBase) / 100
    descuentoComision = (1.27*sueldoBase) / 100

    sueldoBase = sueldoBase-descuentoIsapre-descuentoAfp-descuentoComision

# calcular horas Extras
    if (hrs > 44):
        for i in range(0, hrs - 44):
            sueldoBase += monto * 1.510

            # No se pagara mas de 40 horas extras mensuales
            if (i > 40):
                break
    return sueldoBase

#calcular monto imponible
def calcular_monto_impuesto(imponible):
    if (imponible > 0 and imponible <= 680022):
#monto exento
        return imponible

    elif (imponible > 680022 and imponible <= 1511160):
        Tasa = imponible * 4 / 100
        return imponible - Tasa - 27200

    elif (imponible > 1511160 and imponible <= 2518600):  
        Tasa = imponible * 8 / 100
        return imponible - Tasa - 87647         

    elif (imponible > 2518600 and imponible <= 3526040):    
        Tasa = imponible * 13.5 / 100
        return imponible - Tasa - 226170       

    elif (imponible > 3526040 and imponible <= 4533480):    
        Tasa = imponible * 23 / 100
        return imponible - Tasa - 561144    

    elif (imponible > 4533480 and imponible <= 6044640):    
        Tasa = imponible * 30.4 / 100
        return imponible - Tasa - 896621  

    elif (imponible > 6044640 and imponible <= 15615320):     
        Tasa = imponible * 35 / 100
        return imponible - Tasa - 1174675

    else:    
        Tasa = imponible * 40 / 100
        return imponible - Tasa - 1955441

#funcion final para obtener sueldo final

def Main():
    PorHora = int(input("ingrese sueldo por hora: "))
    HorasTrabajadas = int(input("ingrese Horas trabajadas: "))

    montoBase = calcular_base(HorasTrabajadas, PorHora)
    MontoImpuesto = calcular_monto_impuesto(montoBase)

    print("su sueldo final es: ", MontoImpuesto)

Main()
