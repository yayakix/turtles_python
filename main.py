from turtle import Turtle, Screen
turtle = Turtle()
turtle.shape('turtle')
turtle.color('green')

for x in range(1,10):
    turtle.forward(10)
    turtle.penup()
    turtle.forward(10)
    turtle.pendown()

screen = Screen()
screen.exitonclick()