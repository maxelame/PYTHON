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
