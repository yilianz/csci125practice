


def rate(weight):
    '''  for shippimg charge '''
    if weight <= 2:
        cost = 0.01
    elif weight <= 6 :
        cost = 0.015
    elif weight <= 10:
        cost = 0.02
    elif weight <= 20:
        cost = 0.025
    else:
        cost = "No ships" 
    return cost


weight=input("How heavy are you?       ") 
print(rate(float(weight)))