# Реализовать функцию my_func(),
# которая принимает три позиционных аргумента и возвращает сумму наибольших двух аргументов.

def sum_of_two_biggest_numbers(num_1, num_2, num_3):
    list = sorted([num_1, num_2, num_3])
    return list[1] + list[2]

num_1 = int(input("Введите первое число: "))
num_2 = int(input("Введите второе число: "))
num_3 = int(input("Введите третье число: "))
a = sum_of_two_biggest_numbers(num_1, num_2, num_3)
print(a)


