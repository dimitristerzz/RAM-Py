weight = float(input("Fill in your weight: "))
# weight input
height = float(input("Fill in your height: "))
# height input

bmi = weight / (height*height)
# bmi formula

if 16 < bmi < 18.4:
    print("Underweight, ", bmi)
elif 18.5 < bmi < 24.9:
    print("Normal range, ", bmi)
elif 25 < bmi < 29.9:
    print("Overweight, ", bmi)
elif 30 < bmi < 40:
    print("Obese, ", bmi)
else:
    print("Your bmi is not defined.")
# print in which class the user is in