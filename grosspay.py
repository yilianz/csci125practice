#  Gross Pay
#  input - hours,  payrate
#   


hours = input("How many hours did you work ? \n")
payrate = input("How much are you paid per hour? \n")

payment  = int(hours) * int(payrate)

print("Your gross pay is "+ str(payment))
