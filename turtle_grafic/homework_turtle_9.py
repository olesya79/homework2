import turtle
import random

turtle.shape("turtle")
turtle.pensize(5)

lines = random.randint(10, 30)

turtle.color("red")
for i in range(0, lines):
    lenght = random.randint(10, 50)
    turn = random.randint(45, 360)
    turtle.forward(lenght)
    turtle.right(turn)

turtle.exitonclick()
