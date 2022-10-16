# Задача № 67
# нарисовать узор
# импортируем библиотеку turtle
import turtle

# устанавливаем курсор в виде черепахи
turtle.shape("turtle")
# устанавливаем размер пера черепахи
turtle.pensize(5)
# определяем количество повторов восьмиугольника
for a in range(0, 9):
    for i in range(0, 8):
        turtle.forward(60)
        turtle.right(45)
    turtle.right(40)

# скрываем черепаху
turtle.hideturtle()

# автоматически закрываем окно черепахи
turtle.exitonclick()
