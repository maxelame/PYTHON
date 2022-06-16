'''Идем вглубь
Добавьте с помощью метода append к списку, который содержит буквы, символ 'c'. Список L выводить не надо.'''

L = [[1, 2], ['a', 'b'], [5, 6]]
L[1].append('c')


'''Месячный бюджет

Ниже содержится список budget с бюджетами компании по годам и месяцам. Основная последовательность отвечает за годы, а вложенные списки за месяцы конкретного года, начиная с 2019.

Напишите программу, которая принимает из аргументов командной строки два параметра: год и номер месяца (1 - январь и т.д.), а затем выводит бюджет на этот месяц.
Пример использования:
> python program.py 2019 2
> 148
 '''
import sys
year = int(sys.argv[1])
month = int(sys.argv[2])
budget = [
    [176, 148, 245, 378, 451, 568, 135, 146, 761, 414, 135, 171],  # 2019
    [211, 175, 301, 474, 569, 721, 158, 172, 972, 521, 158, 205],  # 2020
    [257, 210, 374, 599, 722, 920, 188, 206, 1246, 660, 188, 249]  # 2021
]
print(budget[year-2019][month-1])



