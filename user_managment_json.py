import re
import json


def main():
    try:
        file_data_base = open('user_d_b.json', 'r')
    except FileNotFoundError:
        file_data_base = open('user_d_b.json', 'w')
        list_de_users = []
    else:
        list_de_users = json.load(file_data_base)

    finally:
        file_data_base.close()

    langue_data_base = langue()
    print(f'S.P.Q.R.\n{langue_data_base[3]}')
    f_1(langue_data_base, list_de_users)


def f_1(langue_data_base, list_d_b):
    user_select_un = input(f'{langue_data_base[18]}')

    if user_select_un not in ('1', '2', '3'):
        f_1(langue_data_base, list_d_b)

    elif user_select_un == '1':

        travail_un = telephone(langue_data_base)
        for user in list_d_b:
            if user.get('telephone') == travail_un:
                print(f'{langue_data_base[20]}')
                return f_1(langue_data_base, list_d_b)

        travail_deux = email(langue_data_base)
        travail_trois = password(langue_data_base)
        print(f'\n{langue_data_base[4]}'
              f'{langue_data_base[5]} {travail_un}\n'
              f'{langue_data_base[6]} {travail_deux}\n'
              f'{langue_data_base[7]} {travail_trois}')
        users_data_base = {'numero': str(len(list_d_b) + 1),
                           'telephone': travail_un,
                           'e-mail': travail_deux, 'password': travail_trois}
        list_d_b.append(users_data_base)
        return f_1(langue_data_base, list_d_b)

    elif user_select_un == '2':
        f_2(langue_data_base, list_d_b)

    else:
        input(f'{langue_data_base[19]}')
        file_data_base = open('user_d_b.json', 'w')
        data_pour_ecrire = json.dumps(list_d_b, indent=4)
        file_data_base.write(data_pour_ecrire)
        file_data_base.close()
        exit()


def f_2(langue_data_base, list_d_b):
    if len(list_d_b) > 0:
        print(f'{langue_data_base[21]} {len(list_d_b)} {langue_data_base[22]}')
        user_select_deux = input(f'{langue_data_base[23]}')
        if user_select_deux not in (f'{langue_data_base[24]}',
                                    f'{langue_data_base[25]}'):
            return f_2(langue_data_base, list_d_b)

        elif user_select_deux == f'{langue_data_base[24]}':
            for user in list_d_b:
                print(user.get('numero'), user.get('telephone'))
            user_select_trois = input(f'{langue_data_base[26]}')
            if user_select_trois not in (f'{langue_data_base[24]}',
                                         f'{langue_data_base[25]}'):
                print(f'{langue_data_base[27]}')
                return f_1(langue_data_base, list_d_b)
            elif user_select_trois == f'{langue_data_base[24]}':
                return f_3(langue_data_base, list_d_b)
            else:
                return f_1(langue_data_base, list_d_b)
        else:
            return f_1(langue_data_base, list_d_b)
    else:
        print(f'{langue_data_base[39]}')
        return f_1(langue_data_base, list_d_b)


def f_3(langue_data_base, list_d_b):
    try:
        user_select_quatre = int(input(f'{langue_data_base[28]}'))
        if user_select_quatre > len(list_d_b):
            print(f'{langue_data_base[29]}')
            return f_3(langue_data_base, list_d_b)
    except ValueError:
        print(f'{langue_data_base[29]}')
        return f_3(langue_data_base, list_d_b)
    else:
        print(f'{langue_data_base[30]}')
        print(f'{langue_data_base[31]}',
              list_d_b[user_select_quatre - 1].get('numero'))
        print(f'{langue_data_base[32]}',
              list_d_b[user_select_quatre - 1].get('telephone'))
        print(f'{langue_data_base[33]}',
              list_d_b[user_select_quatre - 1].get('e-mail'))
        print(f'{langue_data_base[34]}',
              list_d_b[user_select_quatre - 1].get('password'))

    user_select_cinq = input(f'{langue_data_base[35]}')
    if user_select_cinq == f'{langue_data_base[24]}':
        f_4(langue_data_base, list_d_b, user_select_quatre - 1)
    elif user_select_cinq == f'{langue_data_base[25]}':
        return f_1(langue_data_base, list_d_b)
    else:
        print(f'{langue_data_base[27]}')
        return f_1(langue_data_base, list_d_b)


def f_4(langue_data_base, list_d_b, current_user):
    user_select_six = input(f'{langue_data_base[36]}')
    if user_select_six not in ('4', '5', '6'):
        return f_4(langue_data_base, list_d_b, current_user)
    elif user_select_six == '4':
        import password_gen_grand_plus
        new_password = password_gen_grand_plus.main()
        users_data_base = {'numero': list_d_b[current_user].get('numero'),
                           'telephone': list_d_b[current_user].get('telephone'
                                                                   ),
                           'e-mail': list_d_b[current_user].get('e-mail'),
                           'password': new_password}
        list_d_b[current_user] = users_data_base
        return f_1(langue_data_base, list_d_b)
    elif user_select_six == '5':
        user_select_sept = input(f'{langue_data_base[37]}'
                                 f'{list_d_b[current_user].get("telephone")}?'
                                 f' {langue_data_base[24]}/'
                                 f'{langue_data_base[25]}')
        if user_select_sept != f'{langue_data_base[24]}':
            return f_1(langue_data_base, list_d_b)
        else:
            list_d_b.pop(current_user)
            print(f'{langue_data_base[38]}')
            list_d_b_temp = []
            for q_n in range(len(list_d_b)):
                users_data_base = {'numero': q_n + 1,
                                   'telephone': list_d_b[q_n].get('telephone'),
                                   'e-mail': list_d_b[q_n].get('e-mail'),
                                   'password': list_d_b[q_n].get('password')}
                list_d_b_temp.append(users_data_base)
            list_d_b = list_d_b_temp
            return f_1(langue_data_base, list_d_b)
    else:
        return f_1(langue_data_base, list_d_b)


def langue():
    from languages import langue_data_base_plus
    user_select_langue = input(f'{langue_data_base_plus.get("russian")[0]}\n'
                               f'{langue_data_base_plus.get("francaise")[0]}\n'
                               f'{langue_data_base_plus.get("russian")[1]}/'
                               f'{langue_data_base_plus.get("francaise")[1]}\n'
                               f'{langue_data_base_plus.get("russian")[2]}/'
                               f'{langue_data_base_plus.get("francaise")[2]}: '
                               )
    if user_select_langue not in ('рус', 'fra'):
        return langue()

    if user_select_langue == 'рус':
        langue_data_base_plus = langue_data_base_plus.get('russian')
    else:
        langue_data_base_plus = langue_data_base_plus.get('francaise')

    return langue_data_base_plus


def telephone(langue_data_base):
    base_op = ('050', '066', '095', '099', '067', '097', '096', '098', '063',
               '073', '093', '044', '045', '068')

    telephone_de_user = input(f'{langue_data_base[8]}')

    for element in telephone_de_user:
        if not element.isdigit():
            telephone_de_user = telephone_de_user.replace(element, '')

    if len(telephone_de_user) < 10 or telephone_de_user[-10:-7] not in base_op:
        print(f'{langue_data_base[9]}')
        return telephone(langue_data_base)
    elif not telephone_de_user.startswith('+38'):
        telephone_de_user = '+38' + telephone_de_user[-10:]
    return telephone_de_user


def email(langue_data_base):
    email_de_user = input(f'{langue_data_base[10]}')

    if not re.search(r'\w+\.*\w+@\w+\.\w+', email_de_user):
        print(f'{langue_data_base[11]}')
        return email(langue_data_base)
    return email_de_user


def password(langue_data_base):
    print(f'{langue_data_base[12]}')
    password_de_user = input(f'{langue_data_base[13]}')

    if len(password_de_user) < 8 or re.search(r'\s', password_de_user):
        print(f'{langue_data_base[14]}')
        return password(langue_data_base)
    elif not re.search(r'\d', password_de_user) or \
            not re.search(r'[a-z]', password_de_user) or \
            not re.search(r'[A-Z]', password_de_user) or \
            not re.search(r'[^a-zA-Z0-9]', password_de_user):
        print(f'{langue_data_base[15]}')
        return password(langue_data_base)

    password_de_user_repond = input(f'{langue_data_base[17]}')

    if password_de_user_repond != password_de_user:
        return password(langue_data_base)
    return password_de_user


if __name__ == '__main__':
    main()
