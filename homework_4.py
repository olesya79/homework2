# 'Задание №1'
total = 0

while total <= 50:
    # 'предлагаем пользователь ввести число'
    number = int(input('Введите число: '))
    total += number
    # 'выводим введённые пользователем числа, если они меньше или равны числу 50'
    print('The total is: ', total)
    # 'если число больше 50 , останавливаем цикл'
    if total > 50:
        break
# Задание №2
number = 5

while number <= 5:
    # 'предлагаем пользователю ввести число'
    number = int(input('Введите число: '))
    # если введённое число больше 5, останавливаем цикл
    if number > 5:
        # выводим последнее введённое пользователем число
        print('The last number you entered was a: ', number)
        break

# Задание №3
# просим пользователя ввести 2 числа
number_1 = int(input('Введите первое число: '))
number_2 = int(input('Введите второе число: '))
summa = number_1 + number_2
# 'выводим сумму этих двух чисел'
print('Сумма составляет: ', summa)
# 'спрашиваем у пользователя желает ли он продолжить'
answer = str(input('Введите y/n для продолжения (y-прибавить ещё одно, n-не нужно прибавлять)'))

while answer == 'y':
    # 'если отвечает "да", то вводим ещё одно число'
    number_ev = int(input('Введите ещё одно число: '))
    answer = str(input('Введите y/n для продолжения (y-прибавить ещё одно, n-не нужно прибавлять)'))
    summa += number_ev
    if answer == 'n':
        # 'hcom отвечает "нет", выводим итоговую сумму'
        print('Итоговая сумма:', summa)
        break

# Задание №4
# просим пользователя ввести имя гостя
name = str(input('Введите имя гостя: '))
print(name, 'has been invited')
number_of_guests = 1
# спрашиваем у пользователя хочет ли он ещё кого либо пригласить
answer = str(input('Хотите пригласить ещё гостей? \
Введите y/n для продолжения (y-пригласить, n-не приглашать)'))

while answer == 'y':
    # если отвечает "да", то предлагаем ввести ещё имя
    name = str(input('Введите имя гостя: '))
    answer = str(input('Хотите пригласить ещё гостей? \
    Введите y/n для продолжения (y-пригласить, n-не приглашать)'))
    number_of_guests += 1
    if answer == 'n':
        # если отвечает "нет", то выводим список приглашённых
        print('Количество приглашённых: ', number_of_guests, 'человек')
        break

# Задание №5
compnum = 50
# предлагаем пользователю ввести число
number = int(input('Введите число: '))
count = 1

while number != compnum:
    # если пользователь ввёл число меньше 50, то он продолжает вводить числа
    if number < compnum:
        print('Это число меньше 50')
else:
    # если пользователь ввёл число больше 50, то он продолжает вводить числа
    print('Это число больше 50')
    count += 1
    number = int(input('Введите ещё одно число: '))
    # если введённое число совпадает с 50, то выводится число попыток
print('Well done, you took', count, 'attempts')

# Задание №6
# предлагаем пользователю ввести число от 10 до 20
numb = int(input('Введите число от 10 до 20: '))

while 20 > numb > 10:
    # 'если введённое число меньше 10, то выводится соответствующее сообщение и предлагается ввести число'
    if numb < 10:
        print('Too low')
    else:
        # в остальных случаях, предлагается ввести число, пока оно не совпадёт с диапазоном
        print('Too high')
    number = int(input('Введите ещё число: '))
print('Thank you')

# Задание №7
i = 5

while i > 0:
    # 'выводим количество зелёных бутылок на стене'
    print('There are', i, 'green bottles hanging on the wall')
    print(i, 'green bottles hanging on the wall')
    # одна бутылка упала
    print('And if 1 green bottle should accidentally fall')
    i = i - 1
    # выводим количество оставшихся бутылок
    answer = int(input('haw many green bottles will be hanging on the wall? '))
    if answer == i:
        print('There will be', i, 'green bottles hanging on the wall')
    else:
        while answer != i:
            answer = int(input('No, try again: '))
print('There are no more green bottles hanging on the wall')
