import turtle
wn=turtle.Screen()
wn.addshape("mario.gif")
alex=turtle.Turtle()
wn.setup(800,500)
wn.bgpic("frame.gif")
alex.shape("mario.gif")
print(alex.speed())
#alex.penup()

### start  ###
def goUP():
    alex.color("red")
    alex.seth(90)
    alex.forward(100)
    alex.backward(100)

def goDOWN():
    alex.seth(270)
    alex.forward(5)

def goLEFT():
    alex.seth(180)
    alex.forward(5)

def goRIGHT():
    alex.pencolor("yellow")
    alex.seth(0)
    alex.forward(5)

def goto(x,y):
    alex.pencolor("blue")
    alex.goto(x,y)

def clear():
    alex.clear()

wn.onkey(goUP,"Up")
wn.onkey(goDOWN,"Down")
wn.onkey(goLEFT,"Left")
wn.onkey(goRIGHT,"Right")
wn.onkey(clear,"c")
wn.onclick(goto)


#### 
wn.listen()
wn.mainloop()