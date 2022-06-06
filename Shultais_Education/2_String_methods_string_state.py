Телефонный номер на +7

Напишите программу, которая первым аргументом командной строки принимает телефонный номер, а после выводит True если номер начинается на +7 и False в противном случае.
Пример использования в командной строке Windows:
> python program.py +7813514514
> True
> python program.py 8981514514
> False


import sys
number = sys.argv[1]
print(number.startswith("+7"))

# =========================================================

Телефонный номер не на +7

Если перед переменной, которая содержит логическое значение поставить слово not, то значение переменной будет изменено на обратное.
# Создаем переменную is_phone, содержащую логическое значение True.
is_phone = True

# Выводим оригинальное значение.
print(is_phone)
True

# Выводим обратное значение.
print(not is_phone)
False

Напишите программу, которая первым аргументом командной строки принимает телефонный номер, а после выводит True если номер не начинается на +7 и False если начинается с +7.
Пример использования в командной строке Windows:
> python program.py +7813514514
> False
> python program.py 8981514514
> True

import sys
number = sys.argv[1]
print(not number.startswith("+7"))

# =========================================================
PNG изображение?

Напишите программу, которая первым аргументом командной строки принимает название файла, а после выводит True если это png изображение, и False в противном случае.
Определять png это или нет нужно по расширению файла.
Учитывайте, что имя может быть набрано в разных регистрах.
Пример использования в командной строке Windows:
> python program.py photo.png
> True
> python program.py photo.jpg
> False
> python program.py ROOM.PNG
> True

import sys
file = sys.argv[1]
file = file.lower()
print(file.endswith(".png"))
# =========================================================
Это изображение?
Введение

Мы уже познакомились с логическим типом, а также с оператором not, который меняет логическое значение на обратное. Давайте теперь изучим логическую операцию or.

Логическая операция or сравнивает несколько значений и возвращает True, если хотя бы одно из них будет логически верным:
# Создаем четыре логические переменные.
is_male = True
is_female = False
is_old = True
is_young = False

# Сравниваем: True или False.
# Получаем True, так как одна из переменных True.
print(is_male or is_female)
True

# Сравниваем: False или True (поменяли местами).
# Всё равно получаем True, так как одна из переменных True.
print(is_female or is_male)
True

# Сравниваем: False или False.
# Получаем False, так как нет True.
print(is_young or is_female)
False

# Сравниваем все переменные.
print(is_young or is_female or is_old or is_young)
True

Задание

Напишите программу, которая первым аргументом командной строки принимает название файла, а после выводит True если это изображение, и False в противном случае.
Определять изображение это или нет нужно по расширению файла: png, jpeg, jpg или gif.
Учитывайте, что имя может быть набрано в разных регистрах.
Пример использования в командной строке Windows:
> python program.py photo.png
> True
> python program.py photo.jpg
> True
> python program.py ROOM.PNG
> True
> python program.py video.mp4
> False


import sys
file_name = sys.argv[1]
file_name = file_name.lower()
print(file_name.endswith(".png") or file_name.endswith(".jpg") or file_name.endswith(".jpeg") or file_name.endswith(".gif"))



















