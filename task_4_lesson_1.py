# Пользователь вводит целое положительное число.
# Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции


num =int(input('Введите любое целое положительное число'))
max_num = 0
while num > 0:
    if num % 10 > max_num:
        max_num = num % 10
        if max_num == 9:
            break
    num = num // 10

print(f'Наибольшая цифра числа: {max_num}')

# user_number = input('Введите число: ')
# digit_list = [int(a) for a in str(user_number)]
#
# x = 0
# y = 0
#
# while y != len(digit_list):
#     if x < digit_list[y]:
#         x = digit_list[y]
#     else: y += 1
#
# print(x)
