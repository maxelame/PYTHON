'''Новый автомобиль

В программе ниже создан список с марками автомобилей. Расширьте код так, чтобы программа принимала из первого аргумента командной строки еще одну марку, а затем добавляла её в список marks.
Пример использования:
> python program.py Nissan
> ['BMW', 'Toyota', 'Mercedes', 'Nissan']
 '''

import sys
new_mark = sys.argv[1]
marks = ["BMW", "Toyota", "Mercedes"]
marks.append(new_mark)
print(marks)


'''Удаляем марку

В программе ниже создан список с марками автомобилей. Расширьте код так, чтобы программа принимала из первого аргумента командной строки индекс элемента списка, а затем удаляла элемент, расположенный по этому индексу.
Пример использования:
> python program.py 1
> ['BMW', 'Mercedes', 'Lada', 'Nissan', 'Audi']'''

import sys
index = int(sys.argv[1])
marks = ["BMW", "Toyota", "Mercedes", "Lada", "Nissan", "Audi"]
del marks[index]
print(marks)


