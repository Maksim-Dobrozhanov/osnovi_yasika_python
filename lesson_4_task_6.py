# Реализовать два небольших скрипта:
# итератор, генерирующий целые числа, начиная с указанного;
# итератор, повторяющий элементы некоторого списка, определённого заранее.
# Подсказка: используйте функцию count() и cycle() модуля itertools.
# Обратите внимание, что создаваемый цикл не должен быть бесконечным.
# Предусмотрите условие его завершения.
# Например, в первом задании выводим целые числа, начиная с 3.
# При достижении числа 10 — завершаем цикл.
# Вторым пунктом необходимо предусмотреть условие,
# при котором повторение элементов списка прекратится.



# Мой код
from itertools import count, cycle

for i in count(3):
    print(i)
    if i > 9:
        break

my_list = ['x', 'y', 'z']

count = 0
for i in cycle(my_list):
    count += 1
    print(i)
    if count == 5:
        break

# Код преподавателя
# from itertools import count, cycle
#
# n = 100
# num_list = [x for x in range(5)]
# counter = count()
# cycler = cycle(num_list)
# print([next(counter) for x in range(n)])
# print([next(cycler) for x in range(n)])