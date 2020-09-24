def ratio(n):
    if n==0:
        return 1
    else:
        return 1+ 1/ratio(n-1)

#test function 
#print(ratio(20))

def tez(n):
    if n==0:
        return 7
    else:
        ans =int(tez(n-1))
        print(ans)
        if ans % 2 ==0:
            return ans / 2 
        else:
            return (3*ans+1)/2

print(tez(5))