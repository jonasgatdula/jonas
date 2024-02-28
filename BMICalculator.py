weight = float(input("Enter your weight: "))
height = float(input("Enter your height: "))

bmi = float(weight/(height*height))

if bmi < 18.5:
    print("Underweight")
elif bmi >= 18.5 or bmi < 25:
    print("Normal")
elif bmi >= 25 or bmi < 30:
    print("Overweight")
elif bmi > 30:
    print("Obesity")