#datosdelpaciente
Estado_civil,Genero,Previsión,=0,0,0
Numero_de_atención=0
Nombres_y_apellidos=input("ingrese nombre y apellido de paciente: ")
Cédula_de_identidad=input("ingrese cedula de identidad del paciente: ")
Fecha_de_nacimiento=input("ingrese fecha de  nacimiento de paciente: ")
Estado_civil=input("""ingrese estado civil
1.-soltero
2.-casado
3.- viudo
4.- separado
""")
if (Estado_civil ==1):
    print(" soltero ")
elif (Estado_civil==2):
    print("casado")
elif (Estado_civil==3):
    print("viudo")
elif (Estado_civil==4):
    print("separado")
Domicilio=input("ingrese direccion de paciente: ")
Teléfono=input("ingrese telefono de paciente: ")
Genero=input("""ingrese su genero
1.- Masculino
2.- Femenino
3.- no binarie
""")
if (Genero ==1):
    print(" masculino ")
elif (Genero==2):
    print("femenino")
elif (Genero==3):
    print("motor de helicoptero apache turboneitor3000")
Ocupación=input("ingrese ocupacion de paciente: ")
Previsión=input(""" indique su prevision social
1.- A
2.- B
3.- C
4.- D
5.- fonasa
""")
#datos del médico
Nombres_y_apellidos=input("ingrese nombre y apellido del medico: ")
Especialidad=input("ingrese especialidad del medico: ")
Teléfono=input("ingrese telefono del medico: ")
#Información de atención
Numero_de_atención=int(input("ingrese numero actual de atencion: "))
Numero_de_atención=Numero_de_atención+1
print("su numero de atencion es",Numero_de_atención)
Síntomas=input("indique sintomas")
Diagnostico=str(input("ingrese diagnostico medico: "))
Licencia_médica=input("ingrese Cantidad de días: ")
Fecha=input("indique fecha: ")
#Medicamentos
Nombre=("ingrese nombre de medicamentos: ")
Cantidad_recetada=("ingrese cantidad de medicamentos: ")
print("los datos de paciente fueron agregados correctamente")