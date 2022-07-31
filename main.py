import random
from turtle import Turtle, Screen

turtle = Turtle()
turtle.shape('turtle')
turtle.color('green')
turtle.speed("fast")


def move():
    number = random.randint(5, 70)
    turtle.forward(number)
def turn():
    number = random.randint(0, 100)
    if number % 2 == 0:
        turtle.left(90)
    else:
        turtle.right(90)
# def random_color():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     random_color = (r, g, b)
#     return random_color
colors = ['red','green','blue','pink','yellow','purple']
x = 0
while x < 30:
    turtle.color(colors[random.randint(0,len(colors) - 1)])
    move()
    turn()
    x += 1





screen = Screen()
screen.colormode(255)
screen.exitonclick()
