# Задача № 65
# нарисовать цифры 123
# импортируем библиотеку turtle
import turtle

# устанавливаем размер пера черепахи
turtle.pensize(6)

# устанавливаем угол поворота черепахи влево
turtle.left(90)
# устанавливаем количество шагов черепахи
turtle.forward(140)
# устанавливаем угол поворота черепахи вправо
turtle.right(90)
# отключаем перо, чтобы не оставался видимый след
turtle.penup()
turtle.forward(70)
# включаем перо, чтобы оставался видимый след
turtle.pendown()
turtle.forward(105)
turtle.right(90)
turtle.forward(70)
turtle.right(90)
turtle.forward(105)
turtle.left(90)
turtle.forward(70)
turtle.left(90)
turtle.forward(105)
turtle.penup()
turtle.forward(70)
turtle.pendown()
turtle.forward(105)
turtle.left(90)
turtle.forward(70)
turtle.left(90)
turtle.forward(60)
turtle.left(180)
turtle.forward(60)
turtle.left(90)
turtle.forward(70)
turtle.left(90)
turtle.forward(105)

# автоматически закрываем окно черепахи
turtle.exitonclick()

