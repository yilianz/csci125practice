def pascal(n):
    #base case
    if (n<=2):
        return [1, 1]
    else:
        arr = pascal(n-1)
        print(arr)
        newarr = [1]
        for i in range(0,len(arr)-1):
            sum = arr[i]+arr[i+1]
            newarr.append(sum)
        newarr.append(1)
        return newarr
# test
print(pascal(7))
