
def sum13(list):
    count=0
    p=0
    for num in list:
        if num != 13 and p != 13:
            count=count+num
        else:
            count=count+0
        p=num
    return count
    
    
    
    
    
print(sum13([1,2,13,6,13]))