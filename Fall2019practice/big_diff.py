def diff(mylist):
    big=mylist[0]

    small=mylist[0]
    for num in mylist:
        if num > big:
            big=num
        elif num < small:
            small=num   
    return big-small

print(diff([10,3,5,-6]))