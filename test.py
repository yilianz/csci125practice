input1= input("what is your cars total gas storage")
input2= input("what is the ammount of miles you get per gallon in your vehicle")
process1= float(input1)*float(input2)
print("your total miles your car can drive with a full tank of gas is"+ str(process1))
#gas price is $2.720 
gasprice=2.720
process2=(float(gasprice)*float(input1))/(float(process1))
print( "the price of your gas per mile is " + str(process2)+"dollars")