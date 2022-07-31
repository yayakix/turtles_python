import turtle as t
import random

is_race_on = False
screen = t.Screen()
screen.setup(width=500, height=400)
bet = screen.textinput(title='What is your bet', prompt='Which turtle will win the race')
print(bet)

colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
all_turtles = []

start_y = -100

for x in range(0,len(colors)):
    new_turtle = t.Turtle(shape='turtle')
    new_turtle.color(colors[x])
    new_turtle.penup()
    new_turtle.speed('fastest')
    new_turtle.goto(-230, start_y)
    all_turtles.append(new_turtle)
    start_y += 50


if bet:
    is_race_on = True

while is_race_on:
    random_num = random.randint(1, 10)
    moving_turtle = random.choice(all_turtles)
    moving_turtle.forward(random_num)
    for x in all_turtles:
       if x.xcor() > 230:
           winner = x.pencolor()
           print(winner)
           is_race_on =  False
if winner == bet:
    print('you got it right')
else:
    print('that is not the winner')


screen.exitonclick()
