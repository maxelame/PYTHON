'''Цвета радуги, 3

Создайте словарь rainbow, в котором ключами будут английские названия цветов (red, orange, yellow, green, blue, indigo, violet), а значениями их переводы на русский язык (красный, оранжевый, желтый, зеленый, голубой, синий, фиолетовый).
 '''
rainbow = {
            "red" : "красный",
            "orange" : "оранжевый",
            "yellow" : "желтый",
            "green" : "зеленый",
            "blue" : "голубой",
            "indigo" : "синий",
            "violet" : "фиолетовый"
            }


'''Доступ по ключу

Используя словарь из прошлой задачи, напишите программу, которая получает первым аргументом командной строки название ключа словаря, а затем выводит значение связанное с этим ключом.
Пример использования:
> python program.py red
> красный
 '''

import sys
key = sys.argv[1]
rainbow = {
            "red" : "красный",
            "orange" : "оранжевый",
            "yellow" : "желтый",
            "green" : "зеленый",
            "blue" : "голубой",
            "indigo" : "синий",
            "violet" : "фиолетовый"
            }
print(rainbow[key])


'''Доход за квартал

В редакторе ниже создан словарь quarters, который хранит поквартальные доходы. Каждому кварталу соответствует определенная пара ключ: значение. В качестве значений выступает список месячных доходов.

Напишите программу, которая принимает из первого аргумента командной строки номер квартала, а затем выводит доход за этот квартал.
Пример использования:
> python program.py 1
> 847
 '''


