import turtle

turtle.shape("turtle")
turtle.color('black', 'red')
turtle.begin_fill()
for i in range(0, 4):
    turtle.forward(100)
    turtle.left(90)
turtle.penup()
turtle.end_fill()
turtle.forward(150)

turtle.pendown()
turtle.color('black', 'pink')
turtle.begin_fill()
for i in range(0, 4):
    turtle.forward(100)
    turtle.left(90)
turtle.penup()
turtle.end_fill()
turtle.forward(150)

turtle.pendown()
turtle.color('black', 'yellow')
turtle.begin_fill()
for i in range(0, 4):
    turtle.forward(100)
    turtle.left(90)
turtle.end_fill()

turtle.exitonclick()
