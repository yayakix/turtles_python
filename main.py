import random
from turtle import Turtle, Screen

turtle = Turtle()
turtle.shape('turtle')
turtle.color('green')

def move():
    number = random.randint(50, 100)
    turtle.forward(number)
def turn():
    number = random.randint(0, 100)
    if number % 2 == 0:
        turtle.left(number)
    else:
        turtle.right(number)
x = 0
while x < 20:
    move()
    turn()
    x += 1





screen = Screen()
screen.exitonclick()