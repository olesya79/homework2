import turtle

turtle.shape("turtle")
turtle.pensize(5)

for a in range(0, 10):
    for i in range(0, 8):
        turtle.forward(60)
        turtle.right(45)
    turtle.right(40)

turtle.hideturtle()

turtle.exitonclick()
