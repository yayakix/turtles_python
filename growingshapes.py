from turtle import Turtle, Screen
turtle = Turtle()
turtle.shape('turtle')
turtle.color('green')

round = 3
while round < 10:
    for x in range(round):
        turtle.forward(100)
        turtle.left((360/round))
        turtle.forward(10)
    round+= 1


screen = Screen()
screen.exitonclick()