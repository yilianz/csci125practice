

length=input("what is your length?")
lengthNum=float(length)

width=input("what is your width?")
widthNum=float(width)

height=input("what is your height?")
heightNum=float(height)

volume=(lengthNum * widthNum) * heightNum
volumeString=str(volume)

print("The volume of the rectangular solid is " +volumeString)