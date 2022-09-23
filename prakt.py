


print('Меня зовут Олеся')
print('Мой адрес: г.Орша')

len = int(input('Введите длину садового участка: '))
wid = int(input('Введите ширину садового участка: '))
squary = len * wid
squary1 = squary * 43560
print(squary1)

zak = float(input('Введите сумму заказа в ресторане: '))
nal = (zak * 20) / 100
chaev = (zak * 18) / 100
zak1 = zak + nal + chaev
print(format(nal, ".2f"))
print(format(chaev, ".2f"))
print(format(zak1, ".2f"))

size = int(input('Введите длину стороны многоугольника: '))
nam = int(input('Введите количество сторон многоугольника: '))
squary = size * nam
print(squary)

age1 = int(input('Введите количество детей до двух лет: '))
age2 = int(input('Введите количество детей до 12 лет: '))
age3 = int(input('Введите количество человек от 12 до 65 лет: '))
age4 = int(input('Введите количество человек старше 65 лет: '))
sum = (age1 * 0) + (age2 * 14) + (age3 * 23) + (age4 * 18)
print(format(sum, ".2f"))

import math
area = (n * s ** 2) / 4 * math.tan(math.pi /n)
