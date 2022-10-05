# Задание №1
# условия для ненадёжного пароля
def pass_func(password):
    letter_upp = False
    letter_low = False
    number = False
    # выполнение условий для надёжного пароля
    for letter in password:
        if 'A' <= letter <= 'Z':
            letter_upp = True
        elif 'a' <= letter <= 'z':
            letter_low = True
        elif '0' <= letter <= '9':
            number = True
    # если пароль соответствует всем условиям, то True
    if len(password) >= 8 and letter_upp and letter_low and number:
        return True
    # если пароль не соответствует хотя бы одному из условий, то False
    return False


def main():
    password = str(input('Введите пароль: '))
    if pass_func(password):
        print('У Вас надёжный пароль !')
    else:
        print('У Вас ненадёжный пароль !')


# вызываем функцию
main()
