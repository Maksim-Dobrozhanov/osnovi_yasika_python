# Создать текстовый файл (не программно),
# сохранить в нём несколько строк,
# выполнить подсчёт строк и слов в каждой строке.

with open('text_1.txt') as f_obj:
    file_lines = f_obj.readlines()
    i = 0
    for num, line in enumerate(file_lines):
        i += 1
        words_count = len(line.split())
        print(f'#{num + 1} - {words_count} слов')
    print(f'{i} строк')

# Мой код
# with open('text_1.txt') as f_obj:
#     for line in f_obj:
#         lines = len([0 for _ in f_obj])
#         print(f'Количество строк {lines} ')
#
# with open('text_1.txt') as f_obj:
#     for line in f_obj.readlines():
#         words = len(line.split(' '))
#         print(f'Количество слов в строке {words} ')


