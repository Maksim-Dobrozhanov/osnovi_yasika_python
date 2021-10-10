# Создать (программно) текстовый файл, записать в него программно набор чисел, разделённых пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить её на экран.

with open('text_5.txt', 'w') as file:
    line_input = input('Введите набор чисел разделенных пробелами: ')
    file.write(line_input)

with open('text_5.txt') as file:
    context = file.readlines()
    a = context[0].split(' ')
    sum = 0
    for el in a:
        sum += int(el)
    print(f'Сумма чисел равна: {sum}')

