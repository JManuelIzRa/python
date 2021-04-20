grade1 = float(input("Introduzca la nota1 del alumno: "))

grade2 = float(input("Intreoduzca la nota2 del alumno: "))

absences = int(input("Introduzca el numero de ausencias: "))

total_classes = int(input("Introuzca el numero total de clases: "))

avg_grade = (grade1 + grade2) / 2

attendance = (total_classes - absences) / total_classes

#Sabiendo esto, tenemos que aplicar las siguientes reglas:
#La nota es de 0 a 10
#Los alumnos necesitan una media de 6 o más para estar aprobados
#Los alumnos necesitan un ratio de más del 80% de asistencia para estar aprobados.

print("Media: ", round(avg_grade, 2))

print("Asistencia: ", str(round((attendance*100),2))+"%")

if (avg_grade >= 6):
    if(attendance >= 0.8):
        print("El estudiante está aprobado")
    else:
        print("El estudiante ha suspendido por ausencias")
elif (attendance >= 0.8):
    print("El estudiante ha suspendido por no llegar a la media")

else:
    print("El estudiante ha suspendido por ausencias y por no llegar a la media.")


#Esto se puede simplificar usando AND y OR

if (avg_grade >= 6 and attendance >= 0.8):
    print("El alumno ha aprobado")

elif (avg_grade < 6 and attendance < 0.8):
    print("El alumno ha suspendido por nota media baja y poca asistencia")

elif (avg_grade >= 6):
    print("El alumno ha suspendido por ausencia")
else:
    print("El alumno ha suspendido por baja nota media")


if (avg_grade <6 or attendance < 0.8):
    print("El alumno ha suspendido")