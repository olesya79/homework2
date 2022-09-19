age_people = int(input('Введите возраст человека:'))
age_dog = int(input('Введите возраст собаки:'))

if 2 >= age_dog > 0 and 2 >= age_people > 0:
    age_people1 = age_people * 10.5
    print(age_people1, "лет-возраст человека")

elif age_dog > 2 and 2 >= age_people > 0:
    age_people2 = age_people * 10.5
    print(age_people2, 'лет-возраст человека')

elif 2 >= age_dog > 0 and age_people > 2:
    age_people3 = ((age_people - 2) * 4) + (2 * 10.5)
    print(age_people3, 'лет-возраст человека')

elif age_dog > 2 and age_people > 2:
    age_people4 = ((age_people - 2) * 4) + (2 * 10.5)
    print(age_people4, 'лет-возраст человека')

else:
    print('значение', None)

months = input('Введите название месяца:')

if months == 'январь':
    print('Количество дней в этом месяце: 31')
elif months == 'февраль':
    print('28 или 29 дней в этом месяце')
elif months == 'март':
    print('31 день в этом месяце')
elif months == 'апрель':
    print('30 дней в этом месяце')
elif months == 'май':
    print('31 день в этом месяце')
elif months == 'июнь':
    print('30 дней в этом месяце')
elif months == 'июль':
    print('31 день в этом месяце')
elif months == 'август':
    print('31 день в этом месяце')
elif months == 'сентябрь':
    print('30 дней в этом месяце')
elif months == 'октябрь':
    print('31 день в этом месяце')
elif months == 'ноябрь':
    print('30 дней в этом месяце')
elif months == 'декабрь':
    print('31 день в этом месяце')
else:
    print(None)

note = input('Введите ноту:')
not_ok = int(input('Введите номер нотации октавы:'))

if note == 'C' and 8> not_ok>= 0:
    not_ok = 261.63/2**(4-not_ok)
    print('частота равна:', not_ok)
elif note == 'D' and 8> not_ok>= 0:
    not_ok = 293.66/2 ** (4 - not_ok)
    print('частота равна:', not_ok)
elif note == 'E' and 8> not_ok>= 0:
    not_ok = 329.63/2 ** (4 - not_ok)
    print('частота равна:', not_ok)
elif note == 'F' and 8> not_ok>= 0:
    not_ok = 349.23/2 ** (4 - not_ok)
    print('частота равна:', not_ok)
elif note == 'G' and 8> not_ok>= 0:
    not_ok = 392.00/2 ** (4 - not_ok)
    print('частота равна:', not_ok)
elif note == 'A' and 8> not_ok>= 0:
    not_ok = 440.00/2 ** (4 - not_ok)
    print('частота равна:', not_ok)
elif note == 'B' and 8> not_ok>= 0:
    not_ok = 493.88/2 ** (4 - not_ok)
    print('частота равна:', not_ok)
else:
    print(None)

sound_fr = float(input('Введите частоту звука:'))

if 262.63>= sound_fr>= 260.63:
    print('C4')
elif 294.66>= sound_fr>= 292.66:
    print('D4')
elif 330.63>= sound_fr>= 328.63:
    print('E4')
elif 350.23>=sound_fr>= 348.23:
    print('F4')
elif 393.00>= sound_fr>= 391.00:
    print('G4')
elif 441.00>= sound_fr>= 439.00:
    print('A4')
elif 494.88>= sound_fr>= 492.88:
    print('B4')
else:
    print(None)

years = int(input('Введите год рождения:'))
years1 = 8
years2 = 9
years3 = 10
years4 = 11
years5 = 0
years6 = 1
years7 = 2
years8 = 3
years9 = 4
years10 = 5
years11 = 6
years12 = 7

if years == 2000 or years % 12 == years1:
    print('Дракон')
elif years == 2001 or years % 12 == years2:
    print('Змея')
elif years == 2002 or years % 12 == years3:
    print('Лошадь')
elif years == 2003 or years % 12 == years4:
    print('Коза')
elif years == 2004 or years % 12 == years5:
    print('Обезьяна')
elif years == 2005 or years % 12 == years6:
    print('Петух')
elif years == 2006 or years % 12 == years7:
    print('Собака')
elif years == 2007 or years % 12 == years8:
    print('Свинья')
elif years == 2008 or years % 12 == years9:
    print('Крыса')
elif years == 2009 or years % 12 == years10:
    print('Бык')
elif years == 2010 or years % 12 == years11:
    print('Тигр')
elif years == 2011 or years % 12 == years12:
    print('Кролик')
else:
    print(None)

mark = str (input('Введите оценку:'))

if mark == 'A+'or mark == 'A':
    print('4.0')
elif mark == 'A-':
    print('3.7')
elif mark == 'B+':
    print('3.3')
elif mark == 'B':
    print('3.0')
elif mark == 'B-':
    print('2.7')
elif mark == 'C+':
    print('2.3')
elif mark == 'C':
    print('2.0')
elif mark == 'C-':
    print('1.7')
elif mark == 'D+':
    print('1.3')
elif mark == 'D':
    print('1.0')
elif mark == 'F':
    print('0')
else:
    print(None)