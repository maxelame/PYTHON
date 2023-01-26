list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
list1[2][2].append(7000)

print(list1)



list1 = ['a', 'b', ['c', ['d', 'e', ['f', 'g'], 'k'], 'l'], 'm', 'n']
sub_list = ['h', 'i', 'j']
list1[2][1][2].extend(sub_list)
print(list1)



list1 = [[1, 7, 8], [9, 7, 102], [6, 106, 105], [100, 99, 98, 103], [1, 2, 3]]
maximum = -1
for i in list1:
  if max(i) > maximum:
    maximum = max(i)
print(maximum)


print(max([max(i) for i in [[1, 7, 8], [9, 7, 102], [6, 106, 105], [100, 99, 98, 103], [1, 2, 3]]]))


list1 = [[1, 7, 8], [9, 7, 102], [6, 106, 105], [100, 99, 98, 103], [1, 2, 3]]
maximum = -1
maximum = max([max(i) for i in list1])
print(maximum)


list1 = [[1, 7, 8], [9, 7, 102], [102, 106, 105], [100, 99, 98, 103], [1, 2, 3]]
for i in range(5):
    list1[i].reverse()

print(list1)



list1 = [[1, 7, 8], [9, 7, 102], [102, 106, 105], [100, 99, 98, 103], [1, 2, 3]]
total = 0
counter = 0
for i in list1:
    total += sum(i)
    counter += len(i)
print(total / counter)


list1 = [[1, 2, 3], [4, 5]]
list2 = list1

list1[0].append(7)

print(list2)


list1 = [[1] * 3] * 3
list1[0][1] = 5
print(list1[1][1])



n = 3
list1 = []

for _ in range(n):
    row = input().split()
    list1.extend(row)

print(list1) # один саисок без вложенности



my_list = [[1], [2, 3], [4, 5, 6]]
total = 0

for row in my_list:
    total += sum(row)

print(total) # type(row) integer



my_list = [[12, 221, 3], [41, 5, 633], [71, 8, 99]]

maximum = my_list[0][0]
minimum = my_list[0][0]

for row in my_list:
    maximum = max(row)
    minimum = min(row)

print(maximum + minimum) # 107



my_list = [[12, 221, 3], [41, 5, 633], [71, 8, 99]]

maximum = my_list[0][0]
minimum = my_list[0][0]

for row in my_list:
    if max(row) > maximum:
        maximum = max(row)
    if min(row) < minimum:
        minimum = min(row)

print(maximum + minimum) # 636


n = int(input())
for _ in range(n):
    list1 = [i for i in range(1, n + 1)]
    print(list1)



print(*(lambda n: [list(range(1,n+1)) for _ in range(n)] )(int(input())) , sep='\n')


n = int(input())
l = [list(range(1, n + 1)) for _ in range(n)]
print(*l, sep='\n')


n = int(input())
list1 = [list(range(1, n + 1)) for _ in range(n)]
[print(row) for row in list1]



n = int(input())
list1 = []
for i in range(1, n + 1):
    list1.append(i)
    print(list1)


n = int(input())
print(*[list(range(1, i + 1)) for i in range(1, n + 1)], sep = '\n')



print(*[[j for j in range(1, i + 1)] for i in range(1, int(input()) + 1)], sep = '\n')



print('\n'.join(map(str, [[i for i in range(1, j + 1)] for j in range(1, int(input()) + 1)])))


# -------------------ФУНКЦИЯ-------------------
def pascal(n):
    triangle = [[1]]

    for i in range(n):
        row = [1]
        for j in range(1, len(triangle[i])):
            row += [sum(triangle[i][j - 1: j + 1])]
        row += [1]
        triangle.append(row.copy())

    return triangle[n]


# --------------------ВЫЗОВ--------------------
print(pascal(int(input())))



import math
n = int(input())
def paskal(n):
    list1 = []
    for m in range(0,n + 1):
        list1.append(int(math.factorial(n)/(math.factorial(m) * math.factorial(n-m))))
    return list1
print(paskal(n))


print((lambda n: [__import__('math').comb(n, k) for k in range(n+1)])(int(input())))



import math
n = int(input())
def paskal(n):
    list1 = []
    for m in range(0,n + 1):
        list1.append(int(math.factorial(n)/(math.factorial(m) * math.factorial(n-m))))
    return list1
for i in range(n):
    print(*paskal(i))




s_list = input().split()
list1 = []
for i in s_list:
    list1.append([i] * s_list.count(i))
    for k in s_list:
        if k == i:
            s_list.remove(i)
print(list1)
