# Выполнить функцию, которая принимает несколько параметров, описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы.
# Осуществить вывод данных о пользователе одной строкой.

def pers_data(name, surname, date, city, email, tel):
    print(f'name - {name}; surname - {surname}; date - {date}; city - {city}; email - {email}; tel - {tel}')

n = input("Введите имя: ")
s = input("Введите фамилию: ")
d = input("Введите год рождения: ")
c = input("Введите город проживания: ")
e = input("Введите email: ")
t = input("Введите телефон: ")

pers_data(name=n, surname=s, date=d, city=c, email=e, tel=t)





# Личная версия 1
# def pers_data(name, surname, date, city, email, tel):
#     print(f'name - {name}; surname - {surname}; date - {date}; city - {city}; email - {email}; tel - {tel}')
#
# pers_data(name='Max', surname='Dobro', date=31, city='Montclair', email='xxmail@com', tel=232343435)
#
# Личная версия 2
# def pers_data():
#     name = input("Введите имя: ")
#     surname = input("Введите фамилию: ")
#     date = input("Введите год рождения: ")
#     city = input("Введите город проживания: ")
#     email = input("Введите email: ")
#     tel = input("Введите телефон: ")
#     return name, surname, date, city, email, tel
#
# name, surname, date, city, email, tel = pers_data()
# print(f'имя - {name}, фамилия - {surname}, год рождения - {date}, город проживания - {city}, email - {email}, телефон - {tel}')


