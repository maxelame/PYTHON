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

"""Убираем табуляцию

Скоро вы познакомитесь со вложенными конструкциями в Python. Главное их свойство в том, что вложенный код всегда записывается с отступом.
age = 12
if age >= 12:
    # Вложенный блок записан с отступом в 4 пробела.
    print("Возраст:", age)

Обычно этот отступ составляет 4 пробела, но иногда редакторы кода настроены так, что делают отступ с помощью символа табуляции. Использовать табуляции для форматирования исходного кода на Python не принято, поэтому напишите программу, которая получает из первого аргумента командной строки текст с табуляций, заменяет её на 4 пробела, а после выводит.
Пример использования:

> python program.py "if x == 12:\n	print(x)"
> if x == 12:
    print(x)"""

 import sys
code = sys.argv[1]
print(code.replace("\n	","\n    "))


"""Рецепт

В строке products записан список продуктов необходимых для приготовления «Брауни». Продукты разделены точкой с запятой и пробелом, что затрудняет их чтение. Выведите список продуктов так, чтобы каждый новый ингредиент начинался с новой строки.

Точку с запятой и следующий за ней пробел выводить не надо."""


products = 'Темный шоколад: 100 г; Сливочное масло: 180 г; Коричневый сахар: 200 г; Яйцо куриное: 4 шт; Пшеничная мука: 100 г; Грецкие орехи: 100 г'
print(products.replace("; ","\n"))
