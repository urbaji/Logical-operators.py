weight = int(input("Enter your weight in KG:"))
height = float(input("Enter your height in Meters:"))

BMI = (weight/(height*height))

if BMI < 18.4:
    print("Your are underweight.")
elif BMI > 18.4 and BMI < 24.9:
    print("Your are healthy.")
elif BMI > 24.9 and BMI < 29.9:
    print("Your are overweight.")
elif BMI > 29.9 and BMI < 34.9:
    print("You are extremely overweight.")
elif BMI > 34.9 and BMI < 39.9:
    print("You are obese.")
else:
    print("You are extremely obese.")
