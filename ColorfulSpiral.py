import turtle
import time
import random

turtle.shape('circle')
#turtle.color('blue')
turtle.shapesize(1)
turtle.bgcolor('black') 
turtle.pensize(5)
turtle.speed('fastest')  
turtle.goto(0,-470)

colors = ['magenta', 'cyan','spring green','violet','purple','gold','silver']
clr = [ 'white', 'snow', 'alice blue', 'floral white','azure', 'seashell']
def square():
     #turtle.color(random.choice(colors))
     for i in range(70):
         turtle.color(random.choice(colors)) 
         turtle.right(-35+2)
         turtle.circle(500,130,5)
         turtle.left(45+5)
         #i = i + 200
         turtle.right(3.1415)


def circle():
     for i in range(30):
          turtle.color(random.choice(clr))
          turtle.left(90+2)
          turtle.circle(120,130,9)
          turtle.right(-92+5)
          turtle.right(45)
          
#while True:
square()

time.sleep(1)
turtle.penup()
turtle.hideturtle()
turtle.goto(-43,-110)
turtle.pendown()

circle()
