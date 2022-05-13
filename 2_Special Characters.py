"""Перевод строки

Для перевода строк в HTML служит тег <br>. Напишите программу, которая первым аргументом командной строки принимает HTML-текст, а затем преобразовывает <br>-теги к переводам строк на Python и выводит результат.
Пример использования:
> python title.py "Leading growth:<br>why strategy matters"
> Leading growth:
> why strategy matters"""

import sys
text = sys.argv[1]
text = text.replace("<br>","\n")
print(text)

'''Вложенные кавычки

Приведите два текста ниже к следующему виду:

"'Цыганы' мои не продаются вовсе", — сетовал Пушкин.
ООО "Компания 'Металлинвест'"
Пример использования:
> python program.py
> "'Цыганы' мои не продаются вовсе", — сетовал Пушкин.
> ООО "Компания 'Металлинвест'"'''

text1 = "\"\'Цыганы\' мои не продаются вовсе\", — сетовал Пушкин."
text2 = 'ООО \"Компания \'Металлинвест\'\"'

print(text1)
print(text2)

















