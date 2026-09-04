import turtle
import random
import time

# ---------- setup ----------
turtle.colormode(255)          # colors can be numbers now: (red, green, blue)
turtle.shape('circle')
turtle.shapesize(1)
turtle.bgcolor('black')
turtle.pensize(5)
turtle.speed('fastest')
turtle.hideturtle()

WANDER = 300                   # how far from the middle the pattern can move

colors = ['magenta', 'cyan', 'spring green', 'violet', 'purple', 'gold', 'silver']
clr = ['white', 'snow', 'alice blue', 'floral white', 'azure', 'seashell']


def random_color():
    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)
    return (red, green, blue)


def big_pattern(x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    for i in range(40):
        turtle.color(random_color())          # or: random.choice(colors)
        turtle.right(-35 + 2)
        turtle.circle(500, 130, 5)
        turtle.left(45 + 5)
        turtle.right(3.1415)


def center_pattern(x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    for i in range(20):
        turtle.color(random.choice(clr))
        turtle.left(90 + 2)
        turtle.circle(120, 130, 9)
        turtle.right(-92 + 5)
        turtle.right(45)


# ---------- animation loop ----------
frames = 0
while frames < 40:
    x = random.randint(-WANDER, WANDER)
    y = random.randint(-WANDER, WANDER)

    turtle.clear()             # erase the last picture

    big_pattern(x, y)          # big pattern jumps to a random spot
    center_pattern(x, y)       # center pattern follows to the same spot

    time.sleep(0.3)
    frames = frames + 1

turtle.done()
