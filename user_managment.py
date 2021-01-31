import re
import password_gen_grand_plus
import languages


def main():
    try:
        file_data_base = open("user_d_b.txt")
    except FileNotFoundError:
        file_data_base = open("user_d_b.txt", "w")
        list_de_users = []
    else:
        list_de_users = []
        for a in file_data_base.readlines():
            list_temp = a.split()
            d_temp = {
                "numero": list_temp[0],
                "telephone": list_temp[1],
                "e-mail": list_temp[2],
                "password": list_temp[3],
            }
            list_de_users.append(d_temp)
    finally:
        file_data_base.close()

    langue_data_base = get_langue()
    print(f"S.P.Q.R.\n{langue_data_base[3]}")
    main_menu(langue_data_base, list_de_users)


def main_menu(langue_data_base, data_base_des_users):
    user_select_1 = input(f"{langue_data_base[18]}")
    if user_select_1 not in ("1", "2", "3"):
        main_menu(langue_data_base, data_base_des_users)

    elif user_select_1 == "1":

        user_phone = get_telephone(langue_data_base)
        for user in data_base_des_users:
            if user.get("telephone") == user_phone:
                print(f"{langue_data_base[20]}")
                return main_menu(langue_data_base, data_base_des_users)

        user_e_post = get_email(langue_data_base)

        user_password = get_password(langue_data_base)

        print(
            f"\n{langue_data_base[4]}"
            f"{langue_data_base[5]} {user_phone}\n"
            f"{langue_data_base[6]} {user_e_post}\n"
            f"{langue_data_base[7]} {user_password}"
        )

        info_de_user = {
            "numero": str(len(data_base_des_users) + 1),
            "telephone": user_phone,
            "e-mail": user_e_post,
            "password": user_password,
        }
        data_base_des_users.append(info_de_user)

        return main_menu(langue_data_base, data_base_des_users)

    elif user_select_1 == "2":
        public_info_users(langue_data_base, data_base_des_users)

    else:
        input(f"{langue_data_base[19]}")
        file_data_base = open("user_d_b.txt", "w")
        for element in data_base_des_users:
            file_data_base.write(str(element.get("numero")) + " ")
            file_data_base.write(str(element.get("telephone")) + " ")
            file_data_base.write(str(element.get("e-mail")) + " ")
            file_data_base.write(str(element.get("password")) + "\n")
        file_data_base.close()
        exit()


def public_info_users(langue_data_base, data_base_des_users):
    if len(data_base_des_users) > 0:
        print(
            f"{langue_data_base[21]} {len(data_base_des_users)} "
            f"{langue_data_base[22]}"
        )

        user_select_2 = input(f"{langue_data_base[23]}")
        if user_select_2 not in (
            f"{langue_data_base[24]}",
            f"{langue_data_base[25]}",
        ):
            return public_info_users(langue_data_base, data_base_des_users)

        elif user_select_2 == f"{langue_data_base[24]}":
            for user in data_base_des_users:
                print(user.get("numero"), user.get("telephone"))

            user_select_3 = input(f"{langue_data_base[26]}")
            if user_select_3 not in (
                f"{langue_data_base[24]}",
                f"{langue_data_base[25]}",
            ):
                print(f"{langue_data_base[27]}")
                return main_menu(langue_data_base, data_base_des_users)

            elif user_select_3 == f"{langue_data_base[24]}":
                return total_info_user(langue_data_base, data_base_des_users)

            else:
                return main_menu(langue_data_base, data_base_des_users)

        else:
            return main_menu(langue_data_base, data_base_des_users)

    else:
        print(f"{langue_data_base[39]}")
        return main_menu(langue_data_base, data_base_des_users)


def total_info_user(langue_data_base, data_base_des_users):
    try:
        user_select_4 = int(input(f"{langue_data_base[28]}"))
        if user_select_4 > len(data_base_des_users):
            print(f"{langue_data_base[29]}")
            return total_info_user(langue_data_base, data_base_des_users)
    except ValueError:
        print(f"{langue_data_base[29]}")
        return total_info_user(langue_data_base, data_base_des_users)
    else:
        print(f"{langue_data_base[30]}")
        print(
            f"{langue_data_base[31]}",
            data_base_des_users[user_select_4 - 1].get("numero"),
        )
        print(
            f"{langue_data_base[32]}",
            data_base_des_users[user_select_4 - 1].get("telephone"),
        )
        print(
            f"{langue_data_base[33]}",
            data_base_des_users[user_select_4 - 1].get("e-mail"),
        )
        print(
            f"{langue_data_base[34]}",
            data_base_des_users[user_select_4 - 1].get("password"),
        )

    user_select_5 = input(f"{langue_data_base[35]}")
    if user_select_5 == f"{langue_data_base[24]}":
        change_password_delete_user(
            langue_data_base, data_base_des_users, user_select_4 - 1
        )

    elif user_select_5 == f"{langue_data_base[25]}":
        return main_menu(langue_data_base, data_base_des_users)

    else:
        print(f"{langue_data_base[27]}")
        return main_menu(langue_data_base, data_base_des_users)


def change_password_delete_user(
    langue_data_base, data_base_des_users, current_user
):
    user_select_6 = input(f"{langue_data_base[36]}")
    if user_select_6 not in ("4", "5", "6"):
        return change_password_delete_user(
            langue_data_base, data_base_des_users, current_user
        )

    elif user_select_6 == "4":
        new_password = password_gen_grand_plus.main()
        info_de_user = {
            "numero": data_base_des_users[current_user].get("numero"),
            "telephone": data_base_des_users[current_user].get("telephone"),
            "e-mail": data_base_des_users[current_user].get("e-mail"),
            "password": new_password,
        }
        data_base_des_users[current_user] = info_de_user
        return main_menu(langue_data_base, data_base_des_users)

    elif user_select_6 == "5":
        user_select_7 = input(
            f"{langue_data_base[37]}"
            f'{data_base_des_users[current_user].get("telephone")}?'
            f" {langue_data_base[24]}/"
            f"{langue_data_base[25]}"
        )

        if user_select_7 != f"{langue_data_base[24]}":
            return main_menu(langue_data_base, data_base_des_users)

        else:
            data_base_des_users.pop(current_user)
            print(f"{langue_data_base[38]}")
            data_base_des_users_temp = []
            for q_n in range(len(data_base_des_users)):
                info_de_user = {
                    "numero": q_n + 1,
                    "telephone": data_base_des_users[q_n].get("telephone"),
                    "e-mail": data_base_des_users[q_n].get("e-mail"),
                    "password": data_base_des_users[q_n].get("password"),
                }
                data_base_des_users_temp.append(info_de_user)
            data_base_des_users = data_base_des_users_temp
            return main_menu(langue_data_base, data_base_des_users)

    else:
        return main_menu(langue_data_base, data_base_des_users)


def get_langue():

    user_select_langue = input(
        f'{languages.langue_data_base_plus.get("russian")[0]}\n'
        f'{languages.langue_data_base_plus.get("francaise")[0]}\n'
        f'{languages.langue_data_base_plus.get("russian")[1]}/'
        f'{languages.langue_data_base_plus.get("francaise")[1]}\n'
        f'{languages.langue_data_base_plus.get("russian")[2]}/'
        f'{languages.langue_data_base_plus.get("francaise")[2]}: '
    )
    if user_select_langue not in ("рус", "fra"):
        return get_langue()

    if user_select_langue == "рус":
        langue_data_base_plus = languages.langue_data_base_plus.get("russian")
    else:
        langue_data_base_plus = languages.langue_data_base_plus.get(
            "francaise"
        )

    return langue_data_base_plus


def get_telephone(langue_data_base):
    base_op = (
        "050",
        "066",
        "095",
        "099",
        "067",
        "097",
        "096",
        "098",
        "063",
        "073",
        "093",
        "044",
        "045",
        "068",
    )

    telephone_de_user = input(f"{langue_data_base[8]}")

    for element in telephone_de_user:
        if not element.isdigit():
            telephone_de_user = telephone_de_user.replace(element, "")

    if len(telephone_de_user) < 10 or telephone_de_user[-10:-7] not in base_op:
        print(f"{langue_data_base[9]}")
        return get_telephone(langue_data_base)
    elif not telephone_de_user.startswith("+38"):
        telephone_de_user = "+38" + telephone_de_user[-10:]
    return telephone_de_user


def get_email(langue_data_base):
    email_de_user = input(f"{langue_data_base[10]}")

    if not re.search(r"\w+\.*\w+@\w+\.\w+", email_de_user):
        print(f"{langue_data_base[11]}")
        return get_email(langue_data_base)
    return email_de_user


def get_password(langue_data_base):
    print(f"{langue_data_base[12]}")
    password_de_user = input(f"{langue_data_base[13]}")

    if len(password_de_user) < 8 or re.search(r"\s", password_de_user):
        print(f"{langue_data_base[14]}")
        return get_password(langue_data_base)
    elif (
        not re.search(r"\d", password_de_user)
        or not re.search(r"[a-z]", password_de_user)
        or not re.search(r"[A-Z]", password_de_user)
        or not re.search(r"[^a-zA-Z0-9]", password_de_user)
    ):
        print(f"{langue_data_base[15]}")
        return get_password(langue_data_base)

    password_de_user_repond = input(f"{langue_data_base[17]}")

    if password_de_user_repond != password_de_user:
        return get_password(langue_data_base)
    return password_de_user


if __name__ == "__main__":
    main()
