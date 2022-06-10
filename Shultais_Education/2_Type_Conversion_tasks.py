'''Корень и квадрат

Напишите программу, которая первым аргументом командной строки принимает целое число, а после выводит квадратный корень из этого числа, само число и число возведенное в квадрат. Все значения должны быть разделены точкой с запятой.
Пример использования:
> python program.py 81
> 9;81;6561
'''

import sys
a = sys.argv[1]
print(str(int((int(a) **.5))),str(a),str(int(a) ** 2), sep = ';')


'''Потенциальная энегрия

Вы уже научились вычислять кинетическую энергию тела, теперь самое время вычислить потенциальную. Формула потенциальной энергии такая:
Ep = m x g x h, где m — масса в кг, g — ускорение свободного падения и h — высота тела над нулевым уровнем в метрах.

Напишите программу, которая из первого аргумента командной строки принимает массу тела в кг, а из второго высоту тела над нулевым уровнем в метрах. После программа должна посчитать и вывести потенциальную энергию этого тела. Величину ускорения свободного падения возьмите за 9.8.
Масса и высота могут быть вещественными числами.
Результат преобразуйте к целому числу.
Пример использования:
> python program.py 10 10
> 980'''

import sys
m = float(sys.argv[1])
h = float(sys.argv[2])
E = int( m * h * 9.8)
print (E)

'''Стоимость полного бака

Начинающий разработчик написал программу для расчета стоимости заправки автомобиля до полного бака. Программа принимает три параметра: цену 1 литра бензина, полный объем бензобака и объем уже залитого топлива в бак.

Однако программа не работает как было запланировано и выводит неверные данные
Исправьте все ошибки в коде.
Пример использования:
> python program.py 45.2 50 11.7
> 1731.16'''

import sys

# Получаем данные.
price = float(sys.argv[1])
full = float(sys.argv[2])
busy = float(sys.argv[3])

# Делаем финальный расчет.
amount = (full - busy) * price

# Выводим результат.
print(amount)

'''Преобразование валют

Напишите программу, которая принимает из аргументов командной строки два параметра: курс доллара и количество долларов, а затем выводит следующую фразу: «N долларов в рублях = M руб.», где N — это количество долларов, а M — количество рублей по текущему курсу.
Склонением существительных в этой задаче можно пренебречь.

Обратите внимание, что курс доллара передается с запятой в качестве разделителя (64,66), однако в Python к вещественным числам можно преобразовывать только строки с точкой (64.66).
Также учитывайте, что количество долларов является целым числом.
Пример использования:
> python program.py 64,66 12
> 12 долларов в рублях = 775.92 руб.'''

import sys
kurs = sys.argv[1]
kurs = float(kurs.replace(",","."))
doll = int(sys.argv[2])
print(str(doll)+" долларов в рублях = "+str(kurs*doll)+" руб.")

