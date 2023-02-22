matrix  = [[45, 4, 77],
           [41, 7, 17]]



matrix  = [[1, 2, 8, 0],
           [-4, 1, 9, 4],
           [41, 71, 2, -2]]

print(matrix[2][3])


n = 3
a = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]

for i in range(n):
    for j in range(n):
        print(a[i][j], end=' ')
    print()


n = 3
a = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]

for i in range(n):
    for j in range(n):
        print(a[j][i], end=' ')
    print()


n = 3
a = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]

for i in range(n):
    for j in range(n):
        print(a[n - i - 1][n - j - 1], end=' ')
    print()


n = 5
a = [[19, 21, 33, 78, 99],
     [41, 53, 66, 98, 76],
     [79, 80, 90, 60, 20],
     [33, 11, 45, 67, 90],
     [45, 67, 12, 98, 23]]

maximum = -1
minimum = 100

for i in range(n):
    if a[i][i] > maximum:
        maximum = a[i][i]
    if a[i][n - i - 1] < minimum:
        minimum = a[i][n - i - 1]
print(minimum + maximum)
==========================================создание и вывод матрицы ========================
n, m = int(input()), int(input())
matrix = []
for _ in range(n):
    temp = [input() for _ in range(m)]
    matrix.append(temp)  # создали матрицу

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        print(matrix[i][j], end=' ')  # используем необязательный параметр end
    print()  # перенос на новую строку

    ========================================================================================

    n, m = int(input()), int(input())
    matrix = []
    for _ in range(n):
        temp = [input() for _ in range(m)]
        matrix.append(temp)  # создали матрицу

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print(matrix[i][j], end=' ')  # используем необязательный параметр end
        print()  # перенос на новую строку

    print()
    matrix2 = list(zip(*matrix))

    for i in range(len(matrix2)):
        for j in range(len(matrix2[i])):
            print(matrix2[i][j], end=' ')  # используем необязательный параметр end
        print()


============ След матрицы ================

matrix, total = [], 0  # создаем пустой список и счетчик элементов по диагонали

for i in range(int(input())):
    line = list(map(int, input().split()))  # считываем строку и преобразуем ее в список чисел int
    matrix.append(line)  # формируем матрицу
    total += matrix[i][i]  # подсчитываем главную диагональ с индексами  [i][i]

print(total)



# оцифровываем матрицу
n, summ = int(input()), 0
matrix = [list(map(int, input().split())) for _ in range(n)]
# находим среднее арифметическое
for q in matrix:
    summ += sum(q)
sr_arif = summ/(n ** 2)
# построчно сравниваем строки матрицы и выводим количество элементов больше ср.арифм
for i in range(n):
    counter = 0
    for j in range(n):
        if matrix[i][j] > sr_arif:
            counter += 1
    print(counter)


======================================
# оцифровываем матрицу
n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]

for i in range(n):
    sr_arif = sum(matrix[i])/n # среднее арифм.каждой строки
    counter = 0 # счетчик, который обнуляется после подсчета строки
    for j in range(n):
        if matrix[i][j] > sr_arif:  # поэлементно сравниваем в строке со ср.арифм
            counter += 1
    print(counter)

==========================================
n = int(input())

for i in range(n):
    row = [int(i) for i in input().split()]
    print(len([i for i in row if i > sum(row) // n]))


============================================
n = int(input())

matr = [[int(i) for i in input().split()]for _ in range(n)]

print(max([max([matr[i][j] for i in range(n) if j <= i])for j in range(n)]))


============================================

# оцифровываем матрицу
n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]
# вводим переменную равную минус бесконечности
max_digit = float('-inf')
for i in range(n):
    for j in range(i + 1): # подсчет только по заштрихованному треугольнику
        if matrix[i][j] > max_digit:
            max_digit = matrix[i][j]

print(max_digit)

============================================

# оцифровываем матрицу
n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]
# вводим переменную равную минус бесконечности
max_digit = float('-inf')
for i in range(n):
    for j in range(n):
        # подсчет только по заштрихованному треугольнику
        if (i >= j and i <= n - 1 - j) or (i <= j and i >= n - 1 - j):
            if matrix[i][j] > max_digit:
                max_digit = matrix[i][j]

print(max_digit)

============================================


maximum = []
m = int(input())
for i in range(m):
    my_string = [int(i) for i in input().split()]
    maximum.extend(my_string[:min(i + 1, m - i)])
    maximum.extend(my_string[max(-i - 1, i - m):])
print(max(maximum))


============================================

# оцифровываем матрицу
n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]
# вводим переменную равную минус бесконечности
s1, s2, s3, s4 =0, 0, 0, 0
for i in range(n):
    for j in range(n):
        # подсчет по четвертям
        if i < j and i < n - 1 - j:
            s1 += matrix[i][j]
        if i < j and i > n - 1 - j:
            s2 += matrix[i][j]
        if i > j and i > n - 1 - j:
            s3 += matrix[i][j]
        if i > j and i < n - 1 - j:
            s4 += matrix[i][j]
print(f"Верхняя четверть: {s1}")
print(f"Правая четверть: {s2}")
print(f"Нижняя четверть: {s3}")
print(f"Левая четверть: {s4}")

=================================================

n = int(input())
mtx = [[*map(int, input().split())] for _ in range(n)]
print('Верхняя четверть:', sum([mtx[i][j] for i in range(n) for j in range(n) if j > i < n-1-j]))
print('Правая четверть:', sum([mtx[i][j] for i in range(n) for j in range(n) if j > i > n-1-j]))
print('Нижняя четверть:', sum([mtx[i][j] for i in range(n) for j in range(n) if j < i > n-1-j]))
print('Левая четверть:', sum([mtx[i][j] for i in range(n) for j in range(n) if j < i < n-1-j]))

=================================================

n, m = int(input()), int(input())
for i in range(n):
    for j in range(m):
        print((str(i*j)).ljust(3), end = " ")
    print()

=================================================

n, m = int(input()), int(input())
mult = [[0] * m for _ in range(n)]

for i in range(n):
    for j in range(m):
        mult[i][j] = i * j

for i in range(n):
    for j in range(m):
        print(str(mult[i][j]).ljust(3), end=' ')
    print()

=================================================

n, m = int(input()), int(input())
matrix = [list(map(int, input().split())) for _ in range(n)] # создаем матрицу
max_el = max(max(matrix, key = max)) # находим максимальный элемент не через циклы, а встроенными функциями
break_out_flag = False # создаем флаг без которого не выйти из двойного цикла
for i in range(n):
    for j in range(m):
        if matrix[i][j] == max_el:
            print(i, j)
            break_out_flag = True
            break
    if (break_out_flag):
        break
=================================================

rows, cols = int(input()), int(input())
matrix = [int(i) for _ in range(rows) for i in input().split()]
x = matrix.index(max(matrix))
print(x // cols, x - cols * (x // cols), end=' ')

=================================================
n, m = int(input()), int(input())
matrix = [[*map(int, input().split())] for _ in range(n)] # создаем матрицу
i, j = list(map(int, input().split()))
for k in range(n):
    matrix[k][i], matrix[k][j] = matrix[k][j], matrix[k][i]
for r in range(n):
    for c in range(m):
        print(matrix[r][c], end=' ')
    print()
=================================================



================ПОСТРОЧНЫЙ ВЫВОД МАТРИЦЫ =============

for row in matrix:
    print(*row)

=================================================

n, m = int(input()), int(input())
matrix = [[*map(int, input().split())] for _ in range(n)] # создаем матрицу
i, j = list(map(int, input().split()))
for k in range(n):
    matrix[k][i], matrix[k][j] = matrix[k][j], matrix[k][i] # меняем построчно элементы столбцов местами
for row in matrix: # выводим новую матрицу
    print(*row)
=================================================

n = int(input())
matrix = [[*map(int, input().split())] for _ in range(n)] # создаем матрицу
flag = True
for i in range(n):
    for j in range(n):
        if matrix[i][j] != matrix[j][i]:
            flag = False
if (flag):
    print("YES")
else:
    print("NO")

=================================================

n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)] # создаем матрицу
for i in range(n): # перебираем построчно
    matrix[i][i], matrix[n-i-1][i] = matrix[n-i-1][i], matrix[i][i] # меняем местами элементы диагонали
for _ in matrix:
    print(*_)

=================================================

n = int(input())
matrix = [input().split() for _ in range(n)] # в данном случае необязательно переводить из строки в число

for i in range(n):
    matrix[i][i], matrix[n - i - 1][i] = matrix[n - i - 1][i], matrix[i][i]

for row in matrix:
    print(*row)

=================================================

n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)] # создаем матрицу
for i in range(n // 2):
    for j in range(n):
        matrix[i][j], matrix[n-i-1][j] = matrix[n-i-1][j], matrix[i][j]
for _ in matrix:
    print(*_)

=================================================

n = int(input())

matrix = [[int(item) for item in input().split()] for _ in range(n)]
matrix.reverse()

for row in matrix:
    print(*row)

=================================================
n = int(input())
matrix = [input().split() for i in range(n)] # создаем матрицу
new_matrix = [[0]*n for i in range(n)] # создаем новую матрицу заполненную нулями
for i in range(n):
    for j in range(n):
        new_matrix[i][j] = matrix[n-j-1][i] # проводим перезаписывание элементов из одной матрицы в другую
for row in new_matrix:
    print(*row) # выводти результат

=================================================

char,position = list(input())
y = ord(char)-97
x = 8 - int(position)
matrix = [["."]*8 for i in range(8)]
matrix[x][y] = "N"
for i in range(8):
    for j in range(8):
        if (x - i) ** 2 + (y - j) ** 2 == 5:
            matrix[i][j]="*"
for row in matrix:
    print(*row)


=================================================


char, position = input() # строка уже является итерируемым объектом
y = ord(char) - ord('a')
x = 8 - int(position)
matrix = [['.' for j in range(8)] for i in range(8)] # Вместо генератора списков использовал более эффективный подход - создание матрицы с помощью двойного цикла и списка в списке
matrix[x][y] = 'N'

for i in range(max(0, x-2), min(8, x+3)): # ограничили вложенный цикл областью, где могут находиться возможные ячейки с символом *
    for j in range(max(0, y-2), min(8, y+3)):
        if abs(x-i) + abs(y-j) == 3: # место возведения в степень мы использовали операцию abs() и сложение, так как это быстрее и проще
            matrix[i][j] = '*'

for row in matrix:
    print(*row)



=================================================

n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]
flag = True
common_list = []
sum_row1 = sum(matrix[0])
for row in matrix:
    common_list.extend(row)
    if "0" in list(map(str, row)): # проверка на нули
        flag = False
    if sum(row) != sum_row1: # проверка на одинаковость суммы всех рядов
        flag = False
if len(set(common_list)) != n ** 2: # проверка на уникальность
    flag = False
summ_diag1 = 0  # сумма по диагонали 1
summ_diag2 = 0  # сумма по диагонали 2
for i in range(n):
    for j in range(n):
        summ_diag1 += matrix[i][i]
        summ_diag2 += matrix[i][n -i - 1]
if summ_diag1 != summ_diag2:
    flag = False
transpose = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]   # транспонируем матрицу
sum_row2 = sum(transpose[0])
for row in transpose:
    if sum(row) != sum_row2: # проверка на одинаковость суммы всех рядов
        flag = False
print("YES" if flag else "NO")



======================


n = int(input())

# Считываем матрицу с помощью генератора списков
matrix = [list(map(int, input().split())) for _ in range(n)]

# Проверяем на отсутствие нулей и на одинаковость сумм в строках
flag = all(0 not in row and sum(row) == sum(matrix[0]) for row in matrix)

# Проверяем на уникальность элементов
flag = flag and len(set(matrix[i][j] for i in range(n) for j in range(n))) == n ** 2

# Проверяем на равенство сумм по диагоналям
diag1 = sum(matrix[i][i] for i in range(n))
diag2 = sum(matrix[i][n-i-1] for i in range(n))
flag = flag and diag1 == diag2

# Транспонируем матрицу
transpose = [[matrix[j][i] for j in range(n)] for i in range(n)]

# Проверяем на одинаковость сумм в строках транспонированной матрицы
flag = flag and all(sum(row) == sum(transpose[0]) for row in transpose)

# Выводим ответ
print("YES" if flag else "NO")




=========================================

n, m = map(int, input().split())

# генерируем каждую строку матрицы в виде списка
matrix = [['.' if (i+j) % 2 == 0 else '*' for j in range(m)] for i in range(n)]

# объединяем списки в матрицу и выводим ее
for row in matrix:
    print(*row)  # используем звездочный оператор для распаковки списка в строку

=========================================


n, m = map(int, input().split())
for i in range(n):
    for j in range(m):
        if (i + j) % 2 == 0: # если сумма индексов четная ставим точку
            print(".", end = " ")
        if (i + j) % 2 == 1: # если сумма индексов нечетная ставим звезду
            print("*", end = " ")
    print() # перенос строки


=================================


n = int(input())
for i in range(n):
    for j in range(n):
        if (i + j + 1)  < n: # если сумма индексов меньше n
            print("0", end = " ")
        elif (i + j + 1)  == n: # если сумма индексов = n
            print("1", end = " ")
        else:
            print("2", end = " ")
    print() # перенос строки


===============================


n, m = map(int, input().split())
a = 1
for i in range(n):
    for j in range(m):
        print(str(a).ljust(3), end = "")
        a += 1
    print()


===============================


import numpy as np

n, m = map(int, input().split())

numbers = np.arange(1, n * m + 1)  # Создание списка из n*m элементов в диапазоне от 1 до n*m
matrix = numbers.reshape(n, m)  # Преобразует одномерный массив в двумерный массив из n строк и m столбцов

for item in matrix:
    print(*item)

===============================

n, m = [int(num) for num in input().split()]
for i in range(1, n*m+1, m):
    row = [i + j for j in range(m)]
    print(*row)

=================================

n, m = map(int, input().split())
for i in range(1, n + 1):
    a = i
    for j in range(1, m + 1):
        print(str(a).ljust(3), end = "")
        a += n
    print()

=================================

n = int(input())
matrix = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if i== j or i == n - j - 1:
            matrix[i][j] = 1
for row in matrix:
    print(*row)

=================================

n = int(input())

res = [[1 if i == j or i == n - j - 1 else 0 for j in range(n)] for i in range(n)]
#    [1 if i == j or i == n - j - 1 else 0 for j in range(n)] подставляем 1 усли i == j or i == n-j-1 иначе 0 for j in range(n)
#
for x in res:
    print(*x)

=================================

n = int(input())
matrix = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if (i <= j and i <= n-1-j) or (i >= j and i >= n-1-j):
            matrix[i][j] = 1
for row in matrix:
    print(*row)

==================================

n, m = map(int, input().split())
s = list(range(1, m + 1)) # формируем первоначальный список
for _ in range(0, n):
    print(*s) # выводим список
    s = s[1:] + [s[0]] # формируем новый список, отрезая первый элемент и приставляя его в конец списка
=================================

n, m = map(int, input().split())
matrix = [[i * m + j + 1 for j in range(m)] for i in range(n)] # создаем заполненную матрицу
for i in range(1, n, 2): # каждую вторую строку инвертируем
    matrix[i] = matrix[i][::-1]
for row in matrix:
    print(*row)

=============================== ИСПОЛЬЗОВАНИЕ IF В СРЕЗАХ =========================


nm = list(map(int, input().split()))
[print(*[j for j in range(1 + nm[1] * (i - 1), nm[1] * i + 1)][::-1 if i % 2 == 0 else 1] ) for i in range(1, nm[0] + 1)]

======================================

n, m = [int(i) for i in input().split()]
matrix = [[str(j+i*m).ljust(3) for j in range(1,m+1)] for i in range(n)]
for i in range(n):
    print(*matrix[i][::(-1)**i]) # используем -1 в срезах совместно с индексом

======================================
