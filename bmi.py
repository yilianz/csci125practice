

height = input("What is your height? \n")
weight = input("What is your weight? \n") 

payment  = float(weight)*703 / (float(height)**2)

print("Your BMI is "+ str(payment))