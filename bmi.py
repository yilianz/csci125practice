# input

height = input("What is your height? \n")
weight = input("What is your weight? \n") 

# prosses
BMI  = float(weight)*703 / (float(height)**2)

#output
print("Your BMI is "+ str(BMI))

if BMI < 18.5:
    print("\nYou are in the underweight range\n")
elif BMI < 25:
    print("\nYou are in the normal range\n")
elif BMI < 30:
    print("\nYou are in the overweight range\n")
else:
    print("\nYou are in the obese range\n")