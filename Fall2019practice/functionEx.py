# this is a program that show all kind of function 
def  done1(mylist):
    ''' Takes a list x as an argument and remove the first item'''
    mylist[:1] = []
    return mylist

def letterGrade(grade):
    ''' Takes a point grade as an argument and then return a letter grade  '''
    if grade >= 90:
        return "A"
    elif grade >=80:
        return "B"
    elif grade >=70:
        return "C"
    else:
        return "F"


grade = 77

if grade >= 90:
    print( "A")
elif grade >=80:
    print("B")
elif grade >=70:
    print("C")
else:
    print("F")

print(letterGrade(91))
todoList = ["1", "2","3","4"]
done1(todoList)
print(todoList)




