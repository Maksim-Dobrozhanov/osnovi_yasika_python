# Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить, к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и dict.

month = int(input('Введите месяц в виде целого числа '))

a, b, c, d = 'Зима', 'Весна', 'Лето', 'Осень'

season_list = [a, a, b, b, b, c, c, c, d, d, d, a]

print(f'Время года {season_list[month-1]}.')


# моя личная версия
# month = int(input('Введите месяц в виде целого числа '))

# winter = [1, 2, 12]
# spring = [3, 4, 5]
# summer = [6, 7, 8]
# autumn = [9, 10, 11]
#
# if ((month) in winter):
#     i = 'winter'
# elif ((month) in spring):
#     i = 'spring'
# elif ((month) in summer):
#     i = 'summer'
# else: i = 'autumn'
#
# dict = {'winter': 'зима', 'spring': 'весна', 'summer': 'лето', 'autumn': 'осень'}
#
# print(f'Время года {dict.get(i)}.')