import random
import turtle

import turtle as t
t.colormode(255)

bob = t.Turtle()
bob.shape('turtle')
bob.color('green')
bob.speed("normal")
# bob.pensize(10)
def forward():
    bob.forward(20)
def backward():
    bob.backward(20)
def left():
    bob.left(45)
def right():
    bob.right(45)

screen = t.Screen()
screen.listen()
screen.onkey(key="w", fun=forward)
screen.onkey(key="s", fun=backward)
screen.onkey(key="a", fun=left)
screen.onkey(key="d", fun=right)
screen.exitonclick()
