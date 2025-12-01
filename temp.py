import turtle

playground = turtle.Screen()

frank = turtle.Turtle()

frank.setposition(-300,-250)

for i in range(6):

  for j in range(abs(i-6)):

    for k in range(3):

        frank.fd(100)

        frank.left(120)

    frank.fd(100)

  frank.bk(100*abs(i-6))

  frank.left(60)

  frank.fd(100)

  frank.right(60)

playground.mainloop()