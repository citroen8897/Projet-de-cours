# Генератор паролей.
"""
Программа генерирует пароль пользователю согласно встроенным алгоритмам и
пользовательским вводам.
На всех этапах осуществляется проверка корректности польз. ввода.
Реализация на функциях и рекурсии
"""
import re
from random import choice, randint
from string import digits, punctuation, ascii_letters


def main():
    print('S.P.Q.R.')

    var_1 = '1'
    var_2 = '2'
    var_3 = '3'
    var_6 = '4'
    user_select = input(f'Выберите опцию генерации пароля:\n{var_1} - '
                        f'Сгенерировать простой пароль\n{var_2} - '
                        f'Сгенерировать средний пароль \n'
                        f'{var_3} - Сгенерировать сложный пароль\n'
                        f'{var_6} - Пользовательский пароль\nВаш выбор: ')
    if user_select not in (var_1, var_2, var_3, var_6):
        return main()

    if user_select == var_6:
        user_password = parole_de_user(symbols_de_user(), len_de_user())
        print(f'Сгенерированный пароль: {user_password}')
        return user_password

    if user_len_valid():
        password_gen_len_wake = password_gen_len_medium = \
            password_gen_len_power = len_password()
    else:
        password_gen_len_wake = 8
        password_gen_len_medium = 8
        password_gen_len_power = randint(8, 16)

    symbols_data_base = digits + punctuation + ascii_letters

    if user_select == var_1:
        user_password = password_wake(symbols_data_base, password_gen_len_wake)

    elif user_select == var_2:
        user_password = password_medium(symbols_data_base,
                                        password_gen_len_medium)

    else:
        user_password = password_power(symbols_data_base,
                                       password_gen_len_power)

    print(f'Сгенерированный пароль: {user_password}')
    return user_password


def symbols_de_user():
    string_symbols = input('Через пробел введите символы из которых будет '
                           'состоять Ваш пароль\n')
    string_symbols = string_symbols.replace('  ', ' ').replace(' ', '')
    if len(string_symbols) == 0:
        return symbols_de_user()
    return string_symbols


def len_de_user():
    len_de_parole = input('Введите желаемую длину пароля: ')
    if not len_de_parole.isdigit() or int(len_de_parole) == 0:
        return len_de_user()
    elif int(len_de_parole) < 8:
        print('Вы выбрали ненадежный пароль, но это Ваш выбор...')
    return int(len_de_parole)


def parole_de_user(symbols, lenght):
    password = ''

    if len(symbols) > lenght:
        print('Ошибочка. Задайте снова параметры пароля.')
        return parole_de_user(symbols_de_user(), len_de_user())

    for element in range(lenght):
        element = choice(symbols)
        password += element

    for symbol in symbols:
        if symbol not in password:
            print(f'Пароль неверно сгенерирован: {password}')
            return parole_de_user(symbols, lenght)

    return password


def user_len_valid():
    var_4 = 'Д'
    var_5 = 'н'
    user_select_deux = input(f'Желаете задать длину пароля?\n{var_4}/{var_5}')
    if user_select_deux == var_4:
        return 1
    elif user_select_deux == var_5:
        return 0
    else:
        return user_len_valid()


def len_password():
    len_of_password = input('Задайте длину пароля: ')
    if not len_of_password.isdigit() or int(len_of_password) == 0:
        return len_password()
    elif int(len_of_password) < 8:
        print('Вы выбрали ненадежный пароль, но это Ваш выбор...')
    return int(len_of_password)


def password_wake(s_d_b, p_g_l):

    if p_g_l < 2:
        print('Ошибочка! Для простого пароля не может быть длины меньше 2 '
              'символов.\nПерезадайте длину пароля.')
        return password_wake(s_d_b, p_g_l=len_password())

    password = ''
    for element in range(p_g_l):
        element = choice(re.findall(r'[a-z]', s_d_b))
        password += element
    return password


def password_medium(s_d_b, p_g_l):

    if p_g_l < 2:
        print('Ошибочка! Для среднего пароля не может быть длины меньше 2 '
              'символов.\nПерезадайте длину пароля.')
        return password_medium(s_d_b, p_g_l=len_password())

    password = ''
    for element in range(p_g_l):
        element = choice(re.findall(r'[a-zA-Z0-9]', s_d_b))
        password += element
    return password


def password_power(s_d_b, p_g_l):

    if p_g_l < 4:
        print('Ошибочка! Для сложного пароля не может быть длины меньше 4 '
              'символов.\nПерезадайте длину пароля.')
        return password_power(s_d_b, p_g_l=len_password())

    password = ''
    for element in range(p_g_l):
        element = choice(s_d_b)
        password += element

    counter_up = counter_lo = counter_di = counter_pu = 0
    for symbol in password:
        if symbol.isdigit():
            counter_di += 1
        elif symbol.islower():
            counter_lo += 1
        elif symbol.isupper():
            counter_up += 1
        else:
            counter_pu += 1
    if counter_di == 0 or counter_pu == 0 or counter_up == 0 or \
            counter_lo == 0:
        print(f'пароль не сложный и будет перегенерирован: {password}')
        return password_power(s_d_b, p_g_l)

    return password


if __name__ == '__main__':
    main()
