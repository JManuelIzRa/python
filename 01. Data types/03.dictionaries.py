#Es como una lista pero cada elemento tiene una key.

person = { "first_name" : "John", "last_name" : "Green", "birth_year" : 1980, "country_of_birth" : "Canada"}

print(person)

print(type(person))

print(person["first_name"]) #person[key of the data we want]

person["birth_year"] = 1979 #Modify an element of the dictionary

print(person)

person["marital_status"] = "Married" #Add new key value (property) to our dictionary

print(person)

person["children"] = ["Nathalie", "Ethan"]

print(person)

person["children"].append("Anna")

print(person)

#If the property doesnt exist it gives us an error, to solve it we can use:

person.get("age","invalid property")

#If it doesnt exist it doesnt give an error, they give the message we wrote down

key = "first_name"

print(person[key])

person.clear()

print(person)