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
