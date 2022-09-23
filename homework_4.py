total = 0

while total <= 50:
    number = int(input('Введите число: '))
    total += number
    print('The total is: ', total)
    if total > 50:
        break

number = 5

while number <= 5:
    number = int(input('Введите число: '))
    if number > 5:
        print('The last number you entered was a: ', number)
        break

number_1 = int(input('Введите первое число: '))
number_2 = int(input('Введите второе число: '))
summa = number_1 + number_2
print('Сумма составляет: ', summa)
answer = str(input('Введите y/n для продолжения (y-прибавить ещё одно, n-не нужно прибавлять)'))

while answer == 'y':
    number_ev = int(input('Введите ещё одно число: '))
    answer = str(input('Введите y/n для продолжения (y-прибавить ещё одно, n-не нужно прибавлять)'))
    summa += number_ev
    if answer == 'n':
        print('Итоговая сумма:', summa)
        break

name = str(input('Введите имя гостя: '))
print(name, 'has been invited')
number_of_guests = 1
answer = str(input('Хотите пригласить ещё гостей? \
Введите y/n для продолжения (y-пригласить, n-не приглашать)'))

while answer == 'y':
    name = str(input('Введите имя гостя: '))
    answer = str(input('Хотите пригласить ещё гостей? \
    Введите y/n для продолжения (y-пригласить, n-не приглашать)'))
    number_of_guests += 1
    if answer == 'n':
        print('Количество приглашённых: ', number_of_guests, 'человек')
        break

compnum = 50
number = int(input('Введите число: '))
count = 1

while number != compnum:
     if number < compnum:
        print('Это число меньше 50')
    else:
        print('Это число больше 50')
        count += 1
        number = int(input('Введите ещё одно число: '))
  print('Well done, you took', number_ev, 'attempts')
        

number = int(input('Введите число от 10 до 20: '))

while 20> numbe> 10:
    if number< 10:
        print('Too low')
    else:
        print('Too high')
    number = int(input('Введите ещё число: '))
print('Thank you')
        

i = 5

number = int(input('haw many greeen bottles will be hanging on the wall?'))

while  i > 0:
    print('There are', i, 'green bottles hanging on the wall')
    print( i, 'green bottles hanging on the wall')
    print('And if 1 green bottle should accidentally fall')
    ('1 green bottle shout('Повторите попытку: '))
    ld accidentally fall')
    
    print('There will be', i, 'green bottles hanging on the wall')
    if i == 0:
        print('No, try again')
    if number == 0:
        print('There are no more green bottles hanging on the wall')
        break
