#imports
import turtle

#declare variables
u = 10
t = turtle.Turtle() #creates turtle
t.pensize(5)

#drawing the letter K
t.down()
t.left(90)
t.forward(u * 10)
t.up()
t.left(180)
t.forward(u * 5)
t.down()
t.left(45)
t.forward(u * 7)
t.up()
t.left(180)
t.forward(u * 7)
t.down()
t.right(90)
t.forward(u * 7)
t.up()

#drawing the letter C
t.right(45)
t.forward(u * 8)
t.right(45)
t.forward(u * 2)
t.left(180)
t.down()
t.forward(u * 2)
t.left(45)
t.forward(u * 4)
t.left(45)
t.forward(u * 2)
t.left(45)
t.forward(u * 7)
t.left(45)
t.forward(u * 2)
t.left(45)
t.forward(u * 4)
t.left(45)
t.forward(u * 2)

t.reset()