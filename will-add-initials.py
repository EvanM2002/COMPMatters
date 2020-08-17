# initials program 
from turtle import *

# Do not change these lines (and do not create your own turtle... use t for your initials
t = Turtle()
t.speed(3)

# first initials (well, it is a box...)
t.up()
t.pencolor('red')
t.pensize(3)
t.forward(200)
t.left(90)
t.down()
t.forward(200)
t.left(90)
t.forward(400)
t.left(90)
t.forward(400)
t.left(90)
t.forward(400)
t.left(90)
t.forward(200)

t.reset()


# add your initials below and then call t.reset(), like above, so that 
# the turtle goes back to the initial state for the next initials to state
# (the pencolor and pensize are also reset).
# draw your initials with a different pensize and pencolor

t.right(90)
t.down()
t.pencolor('blue')
t.pensize(2)
t.forward(100)
t.left(135)
t.forward(50)
t.right(90)
t.forward(50)
t.left(135)
t.forward(100)
t.up()
t.right(90)
t.forward(20)
t.right(90)
t.down()
t.forward(100)
t.right(180)
t.up()
t.forward(60)
t.right(90)
t.down()
t.forward(50)
t.left(90)
t.forward(40)
t.left(90)
t.forward(50)
t.up()

t.reset()


# leave the input() function at the bottom of the code
input('hit enter to exit')
