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
    print("S.P.Q.R.")

    option_1 = "1"
    option_2 = "2"
    option_3 = "3"
    option_6 = "4"
    user_select = input(
        f"Выберите опцию генерации пароля:\n{option_1} - "
        f"Сгенерировать простой пароль\n{option_2} - "
        f"Сгенерировать средний пароль \n"
        f"{option_3} - Сгенерировать сложный пароль\n"
        f"{option_6} - Пользовательский пароль\nВаш выбор: "
    )
    if user_select not in (option_1, option_2, option_3, option_6):
        return main()

    if user_select == option_6:
        user_password = get_de_speciale_password(
            get_symbols_de_speciale_password(), get_len_de_speciale_password()
        )
        print(f"Сгенерированный пароль: {user_password}")
        return user_password

    if get_answer_de_standart_password():
        password_gen_len_wake = (
            password_gen_len_medium
        ) = password_gen_len_power = get_len_de_standart_password()
    else:
        password_gen_len_wake = 8
        password_gen_len_medium = 8
        password_gen_len_power = randint(8, 16)

    symbols_data_base = digits + punctuation + ascii_letters

    if user_select == option_1:
        user_password = get_password_wake(
            symbols_data_base, password_gen_len_wake
        )

    elif user_select == option_2:
        user_password = get_password_medium(
            symbols_data_base, password_gen_len_medium
        )

    else:
        user_password = get_password_power(
            symbols_data_base, password_gen_len_power
        )

    print(f"Сгенерированный пароль: {user_password}")
    return user_password


def get_symbols_de_speciale_password():
    string_symbols = input(
        "Через пробел введите символы из которых будет "
        "состоять Ваш пароль\n"
    )
    string_symbols = string_symbols.replace("  ", " ").replace(" ", "")
    if len(string_symbols) == 0:
        return get_symbols_de_speciale_password()
    return string_symbols


def get_len_de_speciale_password():
    len_de_parole = input("Введите желаемую длину пароля: ")
    if not len_de_parole.isdigit() or int(len_de_parole) == 0:
        return get_len_de_speciale_password()
    elif int(len_de_parole) < 8:
        print("Вы выбрали ненадежный пароль, но это Ваш выбор...")
    return int(len_de_parole)


def get_de_speciale_password(symbols, lenght):
    password = ""

    if len(symbols) > lenght:
        print("Ошибочка. Задайте снова параметры пароля.")
        return get_de_speciale_password(
            get_symbols_de_speciale_password(), get_len_de_speciale_password()
        )

    for element in range(lenght):
        element = choice(symbols)
        password += element

    for symbol in symbols:
        if symbol not in password:
            print(f"Пароль неверно сгенерирован: {password}")
            return get_de_speciale_password(symbols, lenght)

    return password


def get_answer_de_standart_password():
    option_4 = "Д"
    option_5 = "н"
    user_select_deux = input(
        f"Желаете задать длину пароля?\n{option_4}/" f"{option_5}"
    )
    if user_select_deux == option_4:
        return 1
    elif user_select_deux == option_5:
        return 0
    else:
        return get_answer_de_standart_password()


def get_len_de_standart_password():
    len_of_password = input("Задайте длину пароля: ")
    if not len_of_password.isdigit() or int(len_of_password) == 0:
        return get_len_de_standart_password()
    elif int(len_of_password) < 8:
        print("Вы выбрали ненадежный пароль, но это Ваш выбор...")
    return int(len_of_password)


def get_password_wake(symbols_pour_generation, len_de_password_select):

    if len_de_password_select < 2:
        print(
            "Ошибочка! Для простого пароля не может быть длины меньше 2 "
            "символов.\nПерезадайте длину пароля."
        )
        return get_password_wake(
            symbols_pour_generation,
            len_de_password_select=get_len_de_standart_password(),
        )

    password = ""
    for element in range(len_de_password_select):
        element = choice(re.findall(r"[a-z]", symbols_pour_generation))
        password += element
    return password


def get_password_medium(symbols_pour_generation, len_de_password_select):

    if len_de_password_select < 2:
        print(
            "Ошибочка! Для среднего пароля не может быть длины меньше 2 "
            "символов.\nПерезадайте длину пароля."
        )
        return get_password_medium(
            symbols_pour_generation,
            len_de_password_select=get_len_de_standart_password(),
        )

    password = ""
    for element in range(len_de_password_select):
        element = choice(re.findall(r"[a-zA-Z0-9]", symbols_pour_generation))
        password += element
    return password


def get_password_power(symbols_pour_generation, len_de_password_select):

    if len_de_password_select < 4:
        print(
            "Ошибочка! Для сложного пароля не может быть длины меньше 4 "
            "символов.\nПерезадайте длину пароля."
        )
        return get_password_power(
            symbols_pour_generation,
            len_de_password_select=get_len_de_standart_password(),
        )

    password = ""
    for element in range(len_de_password_select):
        element = choice(symbols_pour_generation)
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
    if (
        counter_di == 0
        or counter_pu == 0
        or counter_up == 0
        or counter_lo == 0
    ):
        print(f"пароль не сложный и будет перегенерирован: {password}")
        return get_password_power(
            symbols_pour_generation, len_de_password_select
        )

    return password


if __name__ == "__main__":
    main()
