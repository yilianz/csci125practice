
#for i in range(1,4):  # i = 1, 2, 3... 9 
#    for k in range(i,4):  # k = 1 , 2.. 9
#        print(f'{k}x{i}=',end=" ")
 #   print()
for loan in range(100000,1000001,100000):
    print(loan,end="|")
    for rate in [3.5,3.75,4,4.25,4.5,4.75,5,5.25,5.5,6]:
        r = rate /1200
        p = loan
        n = 30*12
        m = p*(r*(1+r)**n)/((1+r)**n -1)
        print(f"{m:0.2f}",end=" ")
    print()
