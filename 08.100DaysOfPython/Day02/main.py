# BMI Calculator

height = input("enter your height in meters: \n")
weight = input("enter your weight in kg: \n")

bmi = float(weight) / float(height)**2

bmi_int = int(bmi)

print(f"Your BMI is {bmi_int}")