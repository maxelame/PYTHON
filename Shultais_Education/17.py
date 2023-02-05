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
