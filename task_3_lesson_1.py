# Узнайте у пользователя число n.
# Найдите сумму чисел n + nn + nnn.
# Например, пользователь ввёл число 3.
# Считаем 3 + 33 + 333 = 369.

user_number = input('Введите любое число ')
 c = int(user_number) + int(user_number*2) + int(user_number*3)
print(c)





# user_number = input('Введите любое число ')
#
# a = int(user_number + user_number)
# b = int(user_number + user_number + user_number)
# user_number = int(user_number)
# c = user_number + a + b
#
# print(c)