import turtle             # Allows us to use turtles
wn = turtle.Screen()      # Creates a playground for turtles
alex = turtle.Turtle()    # Create a turtle, assign to alex
alex.pensize(10)

def draw_branch(t, branch_length, angle, size):
    t.pensize(size)
    if branch_length > 10:
        t.forward(branch_length)
        t.left(angle)
        draw_branch(t, branch_length * 2 /3, angle, size-1)
        t.right(2 * angle)
        draw_branch(t, branch_length * 3 / 4, angle, size-1)
        t.left(angle)
        t.backward(branch_length)
    else:
        t.forward(branch_length)
        t.backward(branch_length)


alex.seth(90)  # Point the turtle upwards
draw_branch(alex, 100, 20, 10)




wn.mainloop()             # Wait for user to close window