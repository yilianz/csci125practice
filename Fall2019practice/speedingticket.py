

def ticket(speed):
    if speed <= 75:
        munz = 0
    elif speed <= 80:
        munz = 25 
    elif speed <= 84:
        munz = 100
    elif speed < 89:
        munz = 125
    elif speed < 94:
        munz = 150
    elif speed < 104:
        munz = 500
    else:
        munz = 25000000  
    return munz

speed = input("Sir How fast were you driving  ")
print(ticket(float(speed)))
