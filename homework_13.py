try:
    num_1 = int(input('Введите первое число '))
    num_2 = int(input('Введите второе число '))
    num_3 = num_1 / num_2
    print(num_3)
except ZeroDivisionError:
    print('Ошибка: деление на ноль запрещено!')
    num_1 = int(input('Введите первое число заново '))
    num_2 = int(input('Введите второе число заново '))
    num_3 = num_1 / num_2
    print(num_3)
except ValueError:
    print('Введён неверный тип ')
