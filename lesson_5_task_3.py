# Создать текстовый файл (не программно).
# Построчно записать фамилии сотрудников и величину их окладов (не менее 10 строк).
# Определить, кто из сотрудников имеет оклад менее 20 тысяч, вывести фамилии этих сотрудников.
# Выполнить подсчёт средней величины дохода сотрудников.
# Пример файла:
# Иванов 23543.12
# Петров 13749.32

with open('text_3.txt') as file:
    file_lines = file.readlines()
    employees = {}
    sum_salary = 0
    for line  in file_lines:
        emp_info = line.split()
        employees.update({emp_info[0]: float(emp_info[1])})
        sum_salary += float(emp_info[1])
salary_median = sum_salary / len(employees)
print(f'Медиана = {salary_median}')

for a, b in employees.items():
    if b < 20000:
        print(f'Сотрудник имеет оклад менее 20 000 р {a}: {b}')


# with open('text_3.txt', 'w') as f_obj:
#     finished = False
#     stopper = '   '
#     while not finished:
#         line_input = input('Введите через пробел фамилию сотрудника и его оклад: ')
#         f_obj.write(line_input + '\n')
#         finished = stopper in line_input
#
# with open('text_3.txt') as f_obj:
#     context = f_obj.readlines()
#     salary_sum = 0
#     for el in context:
#         a = el.split(' ')
#         b = int(a[1])
#         salary_sum += b
#         print(f'Сумма зп: {salary_sum}')
#         salary_median = salary_sum / len(context)
#         print(f'Медиана зп: {salary_median}')
#         if b < 20:
#             print(f'Сотрудник с низкой зп: {a[0]}')


