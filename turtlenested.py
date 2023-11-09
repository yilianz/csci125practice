import turtle             # Allows us to use turtles
wn = turtle.Screen()      # Creates a playground for turtles
alex = turtle.Turtle()    # Create a turtle, assign to alex
alex.speed(100)

for s in range(6):
    for i in range(6-s):
        for j in range(3):
            alex.forward(50)
            alex.left(120)
        alex.forward(50)
    for i in range(6-s):
        alex.backward(50)
    alex.left(60)
    alex.forward(50)
    alex.right(60)
        
'''
alex.left(120)
alex.forward(100)
alex.left(60)
for i in range(6):
    for j in range(3):
        alex.forward(100)
        alex.right(60)
    alex.forward(100)

'''





wn.mainloop()             # Wait for user to close window