def count_evens(list):
    count=0
    for num in list:
        if num %2 ==0:
            count=count+1
    return count
    
    
    
    
    
print(count_evens([1,2,5]))