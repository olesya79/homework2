#Задание №1
colors = ['red', 'green', 'white', 'black', 'pink', 'yello']

print(colors[1:4])

#Задание №2
months = ['january', 'february', 'march', 'aprile']

nambers = [1, 2, 3, 4]

print(months + nambers)

#Задание №3
dict = {'carrot': 'vegetable', 'red': 'color', 'march': 'month'}

print(dict)
for key in dict:
    print(key, dict[key])

#Задание №4
name = input("Введите ваше имя:")

print('Hello,', name)

#Задание №5
first_name = input("Введите ваше имя:")

last_name = input("Введите вашу фамилию:")

print('Hello,', first_name, last_name)

#Задание №6
print('"What do you call a bear with no teeth?"', '\n', '"A gummy bear!"')

#Задание №7
num_1 = int(input("Введите первое число:"))
num_2 = int(input("Введите второе число:"))

resalt = num_1 + num_2

print("The total is:", resalt)

#Задание №8
nam_1 = int(input("Введите первое число:"))
nam_2 = int(input("Введите второе число:"))
nam_3 = int(input("Введите третье число:"))

resalt = (nam_1 + nam_2) * nam_3

print("The answer is:", resalt)

#Задание №9
pizza_1 = int(input("Сколько кусков пиццы у вас было:"))
pizza_2 = int(input("Сколько кусков пиццы вы съели:"))

resalt = pizza_1 - pizza_2

print('У вас осталось', resalt, 'кусков пиццы')

#Задание №10
name = input('Введите ваше имя:')
age = int(input('Введите ваш возраст:'))

age_1 = age + 1

print(name, 'next birthday you will be', age_1)

#Задание №11
sum = int(input('Введите общую сумму счёта:'))
people = int(input('Введите общее количество участников обеда:'))

resalt = int(sum / people)

print(resalt, 'должен заплатить каждый участник')

#Задание №12
days = int(input('Введите количество дней:'))
hours = days * 24
minutes = hours * 60
sekonds = minutes * 60

print(hours, "часа в", days, "днях")
print(minutes, "минуты в", days, "днях")
print(sekonds, "секунды в", days, "днях")

#Задание №13
kilo = int(input('Введите количество килограмм:'))
pound = kilo * 2.204

print('Это', pound, 'пуда')

#Задание №14
larg = int(input('Введите число больше 100:'))
smal = int(input('Введите число меньше 10:'))

resalt = larg // smal

print(smal, 'помещается в', larg, resalt, 'раз')
