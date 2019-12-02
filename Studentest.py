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
'''


