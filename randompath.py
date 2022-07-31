import random
import turtle as t
t.colormode(255)

bob = t.Turtle()
bob.shape('turtle')
bob.color('green')
bob.speed("normal")
bob.pensize(10)


def move():
    number = random.randint(5, 70)
    bob.forward(number)
def turn():
    number = random.randint(0, 100)
    if number % 2 == 0:
        bob.left(90)
    else:
        bob.right(90)
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color
x = 0
while x < 30:
    bob.color(random_color())
    move()
    turn()
    x += 1





screen = t.Screen()
screen.exitonclick()
