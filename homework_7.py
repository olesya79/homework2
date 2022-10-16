# Задача № 69
countries = ('Америка', 'Англия', 'Франция', 'Германия', 'Турция')
print(countries)
country = str(input('Введите название страны: '))
print(country, 'индекс этой страны', countries.index(country))

# Задача № 70
countries = ('Америка', 'Англия', 'Франция', 'Германия', 'Турция')
print(countries)
country = str(input('Введите название страны: '))
print(country, 'индекс этой страны', countries.index(country))
index_country = int(input('Введите число от 0 до 4: '))
print(countries[index_country])

# Задача № 71
sports = ['Лёгкая атлетика', 'Плавание']
kaind_of_sport = str(input('Введите ваш любимый вид чпорта: '))
sports.append(kaind_of_sport)
sports.sort()
print(sports)

# Задача № 72
school_sujects = ['Математика', 'Русский язык', 'Физкультура', 'Рисование', 'Труд']
print(school_sujects)
school_suject = str(input('Введите школьные предметы из списка, которые Вам не нравятся: '))
school_suject_index = school_sujects.index(school_suject)
del school_sujects[school_suject_index]
print(school_sujects)

# Задача № 73
restaurant_dishes = {}
restaurant_dishes_1 = str(input('Введите первое любимое блюдо: '))
restaurant_dishes[1] = restaurant_dishes_1
restaurant_dishes_2 = str(input('Введите второе любимое блюдо: '))
restaurant_dishes[2] = restaurant_dishes_2
restaurant_dishes_3 = str(input('Введите третье любимое блюдо: '))
restaurant_dishes[3] = restaurant_dishes_3
restaurant_dishes_4 = str(input('Введите четвёртое любимое блюдо: '))
restaurant_dishes[4] = restaurant_dishes_4
print(restaurant_dishes)
restaurant_dishes_dislike = int(input('Введите какой элемент хотите исключить: '))
del restaurant_dishes[restaurant_dishes_dislike]
print(sorted(restaurant_dishes.values()))

# Задача № 74
colors = ['красный', 'синий', 'зелёный', 'жёлтый', 'чёрный', 'коричневый', 'фиолетовый',
          'розовый', 'сиреневый', 'голубой']
num_1 = int(input('Введите число от 0 до 4: '))
num_2 = int(input('Введите число от 5 до 9: '))
print(colors[num_1:num_2 + 1])

# Задача № 75
numbers = [128, 326, 413, 284]
for i in numbers:
    print(i)

num = int(input('Введите число из трёх цифр: '))
if num in numbers:
    print(num, 'соответствует позиция', numbers.index(num))
else:
    print('That is not in the list')

# Задача № 76
name_1 = str(input('Введите имя первого гостя: '))
name_2 = str(input('Введите имя второго гостя: '))
name_3 = str(input('Введите имя третьего гостя: '))
guests_list = [name_1, name_2, name_3]
answer = str(input('Вы хотите ещё кого-то пригласить (y/n): '))
while answer == 'y':
    guests_list_new = guests_list.append(input('Введите имя ещё одного гостя: '))
    answer = str(input('Вы хотите ещё кого-то пригласить (y/n): '))
else:
    print(len(guests_list), 'гостя приглашено на вечеринку')

# Задача № 77
name_1 = str(input('Введите имя первого гостя: '))
name_2 = str(input('Введите имя второго гостя: '))
name_3 = str(input('Введите имя третьего гостя: '))
guests_list = [name_1, name_2, name_3]
print(guests_list)
answer = str(input('Вы хотите ещё кого-то пригласить (y/n): '))
while answer == 'y':
    guests_list_new = guests_list.append(input('Введите имя ещё одного гостя: '))
    answer = str(input('Вы хотите ещё кого-то пригласить (y/n): '))
print(len(guests_list), 'гостя приглашено на вечеринку')
print(guests_list)
guests_name = str(input('Введите имя гостя из списка приглашённых: '))
print(guests_name, 'на позиции', guests_list.index(guests_name))
answer_1 = str(input('Хотите, чтобы этот гость присутствовал на вечеринке (y/n): '))
if answer_1 == 'n':
    del guests_list[guests_list.index(guests_name)]
print(guests_list)

# Задача № 78
tele = ['Пусть говорят', 'Новости', 'Угадай мелодию', 'Поле чудес']
for i in tele:
    print(i)
tele_1 = str(input('Введите телепередачу: '))
tele_1_position = int(input('Введите желаемую позицию этой телепередачи: '))
tele.insert(tele_1_position, tele_1)
for i in tele:
    print(i)
