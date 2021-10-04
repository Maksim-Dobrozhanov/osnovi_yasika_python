# Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.

def num_div(num1, num2):
    try:
        div = num1 / num2
        return div
    except ZeroDivisionError:
        return print('На ноль делить нельзя!')

num1 = float(input("Введите первое число: "))
num2 = float(input("Введите второе число: "))
print(num_div(num1, num2))

