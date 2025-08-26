semana,fecha_actual=input("Ingrese el dia y la fecha separado con comas(Ej: Lunes,14/02) ").split(",")
fecha,mes=fecha_actual.split("/")
fecha=int(fecha)
mes=int(mes)
semana=semana.lower()

validos = {"lunes","martes","miercoles","jueves","viernes","sabado","domingo"}
if semana not in validos:
    print("Error en el dia de la semana")
elif not (1 <= fecha <= 31) or not (1 <= mes <= 12):
    print("Error en la fecha")

if semana in ("lunes","martes","miercoles"):
  examen=input("Se tomaron examenes? (Si o No): ").strip().lower()
  if examen=="si":
   aprob,desp=input("Ingrese la cantidad de aprobados y desaprobados (separados por coma): ").split(",")
   aprob=int(aprob)
   desp=int(desp)
   total=aprob+desp
   if total > 0:
    porcentaje_aprobados = (aprob * 100) / total
    porcentaje_desaprobados = (desp * 100) / total
    print(f"El porcentaje de aprobados es de {porcentaje_aprobados}%")
    print(f"El porcentaje de desaprobados es {porcentaje_desaprobados}%")
   else:
     print("No se puede calcular, no hay alumnos.")
if semana=="jueves":
   asistencia=int(input("Ingrese el porcentaje de asistencia(Ej: 50 )"))
   if asistencia < 50:
     print("No asistió la mayoría")
   else:
      print("Asistió la mayoría")    


if semana=="viernes" and fecha==1 and (mes==1 or mes==7):
 print("Comienzo de nuevo ciclo!")
 alum_nuevos=int(input("Ingrese la cantidad nueva de alumnos: "))
 arancel_alum=float(input("Ingrese el arancel por alumno: "))
 ingresos_nuevos=alum_nuevos*arancel_alum
 print(f"EL ingreso total es de ${ingresos_nuevos}")