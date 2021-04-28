data_valid = False

while data_valid == False:
    
    grade1 = float(input("Introduzca la nota1 del alumno: "))

    if grade1 < 0 or grade1>10:
        print("La nota debe estar entre 0 y 10")
        continue

    else:
        data_valid = True


data_valid = False

while data_valid == False:
    
    grade2 = float(input("Intreoduzca la nota2 del alumno: "))

    if grade2 < 0 or grade2 > 10:
        print("La nota debe estar entre 0 y 10")
        continue

    else:
        data_valid = True

data_valid = False

while data_valid == False:
    
    total_classes = int(input("Introuzca el numero total de clases: "))

    if total_classes <= 0:
        print("Las clases totales son un numero positivo.")
        continue
    
    else:
        data_valid = True

data_valid = False

while data_valid == False:

    absences = int(input("Introduzca el numero de ausencias: "))

    if absences > total_classes or absences < 0:
        print("Ausencias incorrectas.")
        continue

    else:
        data_valid = True






avg_grade = (grade1 + grade2) / 2

attendance = (total_classes - absences) / total_classes

print("Media: ", round(avg_grade, 2))

print("Asistencia: ", str(round((attendance*100),2))+"%")


if (avg_grade >= 6 and attendance >= 0.8):
    print("El alumno ha aprobado")

elif (avg_grade < 6 and attendance < 0.8):
    print("El alumno ha suspendido por nota media baja y poca asistencia")

elif (avg_grade >= 6):
    print("El alumno ha suspendido por ausencia")
else:
    print("El alumno ha suspendido por baja nota media")
