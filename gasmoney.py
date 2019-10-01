#gas tank
gt=input("How much gallons can your car hold? ")
#miles the car drives on a full tank
gm=input("How many miles can your car drive on a full tank? ")
#mph
mph=(float(gm)/float(gt))

p = (float(gt)/float(gm))*2.720
print("your car drives "+str(mph)+" per hour")
print("you will pay "+str(p)+"each mile")