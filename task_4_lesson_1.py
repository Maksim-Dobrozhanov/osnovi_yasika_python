# Пользователь вводит целое положительное число.
# Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции

user_number = input('Введите число: ')
digit_list = [int(a) for a in str(user_number)]

x = 0
y = 0

while y != len(digit_list):
    if x < digit_list[y]:
        x = digit_list[y]
    else: y += 1

print(x)
