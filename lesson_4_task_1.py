# Реализовать скрипт,
# в котором должна быть предусмотрена функция расчёта заработной платы сотрудника.
# Используйте в нём формулу: (выработка в часах*ставка в час) + премия.
# Во время выполнения расчёта для конкретных значений необходимо запускать скрипт с параметрами.

from sys import argv

if len(argv) < 4:
    print('Введите все данные (выработка, ставка, премия)!')
else:
    result = float(argv[1]) * float(argv[2]) + float(argv[3])
    print(result)
