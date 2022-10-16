import turtle
import random

turtle.shape("turtle")
turtle.pensize(6)

for i in range(0, 8):
    turtle.color(random.choice(['yellow', 'green', 'red', 'pink', 'blue', 'brown']))
    turtle.forward(80)
    turtle.left(45)

turtle.exitonclick()
