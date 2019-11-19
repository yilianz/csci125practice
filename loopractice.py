'''
for i in range(10):
    for j in range(10):
        if i == j:
            print(9-i,end=" ")
        else:
            print("*",end=" ")
    print()

for i in range(10):
    for j in range(10-i):
       print("*",end=" ")
    print()
'''
sum = 0
for i in range(1,21):
    sum=sum+(1/2)**i
print(sum)