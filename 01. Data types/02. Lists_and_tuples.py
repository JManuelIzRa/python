students = "John, Mary, Steve"

#As a string add or remove some data is too difficult

students = ["John", "Mary", "Steve"]

print(type(students))

print("Longitud: ", len(students))

print("Student 0: ", students[0])

print("Last student (-1): ", students[-1])

print("First two students: ", students[:2])


#Tuples
#On a tuple we cant add, remove or modify any data
#Strings are inmutable too

months = ("January", "February", "March")

print(type(months))

print(months[0])

students[0] = "Modified value"

print(students[0])

#months[0] = "Change" We cant do this

students.append("End data")

print(students[-1])

students.insert(0, "Insertado en la posicion 0")#insert(position, item)

print(students)

students.pop()#delete the last item. As default it removes the last item

print(students)

students.pop(1)#delete the element on position 1

print(students)

students.remove("Mary")#If there are two elements with the same name, it only remove the first ocurrency. If it doesnt find the word it gives an error

print(students)

students2 = ["Paul","John"]

print(students + students2)#To merge two lists


