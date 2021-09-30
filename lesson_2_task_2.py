# Для списка реализовать обмен значений соседних элементов.
# Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т. д.
# При нечётном количестве элементов последний сохранить на своём месте.
# Для заполнения списка элементов нужно использовать функцию input().


user_input = input('введите цифры: ')
list_1 = user_input.split()
len_list = len(list_1)
i = 0
if len_list > 1:
    while i < len_list - 1:
        list_1[i], list_1[i+1] = list_1[i+1], list_1[i]
        i +=2

print(list_1)


# моя личная версия
# list = input('введите цифры без пробелов ')
# list_1 = []
# b = (len(list) // 2)*2
# c = 0
#
# for el in list:
#     while c != b:
#         if c % 2 == 0:
#             list_1.insert(c, el)
#         else: list_1.insert((c-1), el)
#         c +=1
#         break
# if (len(list) % 2) != 0:
#     list_1.append(list[-1])
#
# print(list_1)