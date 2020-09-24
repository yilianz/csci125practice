'''  Answer 25
ans = 1
for num in range(15,30,5):     
    if num % 3 == 0:
        ans = ans + num
print(num)

for i in range(1,3):
    for j in range(2,5): 
        print(f'({i},{j})', end=" ")
    print()

(1,2) (1,3) (1,4) 
(2,2) (2,3) (2,4)



for i in range(1,5):
    for j in range(i,5): 
        print(f'({i},{j})', end=" ")
    print()

(1,1) (1,2) (1,3) (1,4) 
(2,2) (2,3) (2,4) 
(3,3) (3,4) 
(4,4) 



for i in range(1,5):
    for j in range(i,i+3): 
        print(f'({i},{j})', end=" ")
    print()

(1,1) (1,2) (1,3) 
(2,2) (2,3) (2,4) 
(3,3) (3,4) (3,5) 
(4,4) (4,5) (4,6)


mylist = [1,2,3,4,5]
def reverseL(mylist):
	if int(mylist) == 0:
		return mylist
	else:
		return reverseL(mylist[1:]) + mylist[0]


print(reverseL(mylist))
 '''


class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def origin(self):
        (x,y) = (0,0)
        print(f"{self.x,self.y}",end="")
        
    def distance(n):
        distance = x - y
    print(distance)