# Реализовать генератор с помощью функции с ключевым словом yield,
# создающим очередное значение. При вызове функции должен создаваться объект-генератор.
# Функция вызывается следующим образом: for el in fact(n).
# Она отвечает за получение факториала числа.
# В цикле нужно выводить только первые n чисел, начиная с 1! и до n!.
# Подсказка: факториал числа n — произведение чисел от 1 до n.
# Например, факториал четырёх 4! = 1 * 2 * 3 * 4 = 24.

# Мой код
from math import factorial

def my_generator(finish):
    for i in range(finish+1):
        yield factorial(i)

my_gen = my_generator(12)

for i in my_gen:
    print(i)
# Код преподователя
# def gen_factorial(number):
#     cur = 1
#     for i in range (1, number + 1):
#         cur *= i
#         yield cur
#
# n = 12
# for ind, el in enumerate(gen_factorial(n)):
#     print(f'#{ind + 1} {el}')