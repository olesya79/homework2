# Задача № 68
# нарисовать узор, который меняется при каждом запуске
# импортируем библиотеку turtle
import turtle
# импортируем библиотеку random
import random

# устанавливаем курсор в виде черепахи
turtle.shape("turtle")
# устанавливаем размер пера черепахи
turtle.pensize(5)

# определяем количество линий рандомно
lines = random.randint(10, 30)

# определим цвет линии
turtle.color("red")
for i in range(0, lines):
    # определяем длину линий рандомно
    lenght = random.randint(10, 50)
    # определяем углы поворота рандомно
    turn = random.randint(45, 360)
    turtle.forward(lenght)
    turtle.right(turn)

# автоматически закрываем окно черепахи
turtle.exitonclick()
