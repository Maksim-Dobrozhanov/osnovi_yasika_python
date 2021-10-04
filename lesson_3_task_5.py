# Программа запрашивает у пользователя строку чисел, разделённых пробелом.
# При нажатии Enter должна выводиться сумма чисел.
# Пользователь может продолжить ввод чисел, разделённых пробелом и снова нажать Enter.
# Сумма вновь введённых чисел будет добавляться к уже подсчитанной сумме.
# Но если вместо числа вводится специальный символ, выполнение программы завершается.
# Если специальный символ введён после нескольких чисел,
# то вначале нужно добавить сумму этих чисел к полученной ранее сумме и после этого завершить программу.

def sum_nums(nums_str, stop):
    nums_list = nums_str.split(' ')
    sum_list = 0
    for i in nums_list:
        if i == stop:
            break
        sum_list += int(i)
    return sum_list

stopper = 'x'
finished = False
s = 0
while not finished:
    nums_str_user = input('Enter numbers separated by space: ')
    s += sum_nums(nums_str_user, stopper)
    finished = stopper in nums_str_user
    print(f'Sum = {s}')


#Личная версия
# total_sum = 0
# i = False
# while i == False:
#     symbol_input = input('Введите несколько чисел: ')
#     print(symbol_input)
#     i = symbol_input.endswith('?')
#     print(i)
#     symbol_split = symbol_input.split(' ')
#     print(symbol_split)
#     num_list = [int(item) for item in symbol_split]
#     print(num_list)
#     num_sum = sum(num_list)
#     print(num_sum)
#     total_sum += num_sum
#     print(total_sum)





# num_split = num_input.split(' ?')
# num_cut = num_split[:1]
# num_cut_str = ''.join(num_cut)
# num_cut_sum = sum(map(int, num_cut_str.split(' ')))
# print(num_cut_sum)
#
# num_check = num_input.split(' ')
# if '?' in num_check:
#     print('Я нашел "?", поэтому сложил только то, что было до него')

