import random
import turtle
import turtle as t
t.colormode(255)

bob = t.Turtle()
bob.shape('turtle')
bob.color('green')
bob.speed("fastest")
# bob.pensize(10)

number = 13
size = 50
while number < 18:
    angle = 360/number
    for x in range(0,number):
        bob.circle(size)
        bob.left(angle)
    number += 1
    size += 20


screen = t.Screen()
screen.exitonclick()
