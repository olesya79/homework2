# Задача № 66
# нарисовать восьмиугольник, все стороны которого окрашены в разные цвета
# импортируем библиотеку turtle
import turtle
# импортируем библиотеку random
import random

# устанавливаем курсор в виде черепахи
turtle.shape("turtle")
# устанавливаем размер пера черепахи
turtle.pensize(6)

for i in range(0, 8):
    # определяем цвет стороны рандомно
    turtle.color(random.choice(['yellow', 'green', 'red', 'pink', 'blue', 'brown']))
    # устанавливаем количество шагов черепахи
    turtle.forward(80)
    # устанавливаем угол поворота черепахи влево
    turtle.left(45)

# автоматически закрываем окно черепахи
turtle.exitonclick()
