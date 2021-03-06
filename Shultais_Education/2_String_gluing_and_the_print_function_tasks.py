# Создайте две переменные: first_name и last_name. Переменной first_name присвойте строку с вашим именем, а в last_name поместите фамилию.
# Выведите с помощью print на экран строку вида «Фамилия И.» (без кавычек), где И – первая буква вашего имени.

first_name = "Maxim"
last_name = "Kunkevich"
print(last_name, first_name[0], end = '.\n')


# Программа ниже принимает из аргументов командной строки три слова, а после выводит эти слова через пробелы. Внесите изменения в функцию print так, чтобы она разделяла переданные строки слешем /.
import sys
# Принимаем данные и сохраняем их в переменных a, b, c
a, b, c = sys.argv[1], sys.argv[2], sys.argv[3]

print(a, b, c, sep = '/')

# Полный путь
# Полный путь до файлов в операционной системе WIndows начинается с имени диска, затем следуют каталоги разделенные обратным слешем и замыкает последовательность целевой файл: C:\Catalog1\catalog2\file.ext
# Программа ниже принимает из аргументов командной строки 4 переменные: диск, два каталога и имя файла.
# Используя склейку строк, сформируйте полный путь до файла в системе Windows и выведите результат.
#
# Обратите внимание, что обратный слеш в Python имеет особое значение при использовании в строках.
# Чтобы добавить в строку один обратный слеш, нужно написать его два раза:
# # Прямой слеш
# print("catalog1/catalog2/task.py")
# catalog1/catalog2/task.py
#
# # Обратный слеш
# print("catalog1\\catalog2\\task.py")  # Указываем по два слеша - выводится один.
# catalog1\catalog2\task.py

import sys

# Принимаем данные и сохраняем их в переменных disk, catalog1, catalog2, filename

disk, catalog1, catalog2, filename = sys.argv[1], sys.argv[2], sys.argv[3],  sys.argv[4]
print(disk + ':\\'+catalog1+'\\'+catalog2+'\\'+filename)# Напишите ваш код тут.

# Напишите программу, которая принимает первым аргументом командной строки слово, а после выводит его с подчеркиванием.
# В качестве символа для подчеркивания используйте минус «-».
import sys
word = sys.argv[1]
print(word)
print("-" * len(word))

# Напишите программу, которая принимает первым аргументом командной строки слово, а после выводит его в рамке. Обратите внимание, что в примере использования справа и слева от слова стоят пробелы.
# Пример использования в командной строке Windows:
# > python program.py Programming
# > +-------------+
# > | Programming |
# > +-------------+

import sys
word = sys.argv[1]
print('+' + "-" * (len(word)+2) + '+')
print('| '+ word + ' |')
print('+' + "-" * (len(word)+2) + '+')

# Напишите программу, которая получает через аргументы командной строки число, а после выводит его с правой стороны строки длиной 15 знаков. Слева от числа должны быть проставлены точки.
# Пример использования:
# > python program.py 543
# > ............543

import sys
number = sys.argv[1]
print("." *(15-len(number)) + number
