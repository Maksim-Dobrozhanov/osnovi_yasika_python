# Реализовать структуру «Рейтинг», представляющую собой набор натуральных чисел, который
# не возрастает. У пользователя нужно запрашивать новый элемент рейтинга. Если в рейтинге
# существуют элементы с одинаковыми значениями, то новый элемент с тем же значением
# должен разместиться после них.
# Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
# Пользователь ввёл число 3. Результат: 7, 5, 3, 3, 3, 2.
# Пользователь ввёл число 8. Результат: 8, 7, 5, 3, 3, 2.
# Пользователь ввёл число 1. Результат: 7, 5, 3, 3, 2, 1.
# Набор натуральных чисел можно задать сразу в коде, например, my_list = [7, 5, 3, 3, 2].

list = [7, 5, 3, 3, 2]
a = int(input('Введите новый элемент рейтинга '))

for element in list:
    if a == element:
        position = list.index(a) + 1
        list.insert(position, a)
        print(list)
    else:
        list.append(a)
        list = sorted(list, reverse=True)
        print(list)
    break
#
#
# rating_list = [7, 5, 3, 3, 2]
# rating = int(input('enter rating: '))
# inserted = False
# for index, elem in enumerate(rating_list):
#     if rating > elem:
#         rating_list.insert(index, rating)
#         inserted = True
#         break
#
# if not inserted:
#     rating_list.append(rating)
#
# print(rating_list)
