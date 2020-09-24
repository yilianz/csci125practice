import turtle             # Allows us to use turtles
wn = turtle.Screen()      # Creates a playground for turtles
alex = turtle.Turtle()    # Create a turtle, assign to alex

alex.penup()
alex.forward(-400)
alex.pendown()

# put your code here   
def regularpoly(side,length):
    """
     display the regular shape with the given side and length
    """
    angle = 180 - (side-2.0)*180/side
    for _ in range(side):
        alex.forward(length)
        alex.left(angle)


for i in range(3,11):
    regularpoly(i, 300.0/i)
    alex.penup()
    alex.forward(130)
    alex.pendown()






wn.mainloop()             # Wait for user to close window