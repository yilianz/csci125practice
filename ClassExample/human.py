#define a human class
class human:
    #initializer
    def __init__(self,name,age):
        self.name=name  #property/attribute--name
        self.age = age  #property/attribute -- age
    
    def laugh(self):
        print(f'{self.name}',end="")
        print(":-)")
    
#build a human object 
I = human("yilian",30)
he = human("mike",45)
    
#use a human object 
I.laugh()


# Create a student class


#build a student object 
