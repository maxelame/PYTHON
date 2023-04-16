set1 = {10, 20, 30, 40}
set2 = set(range(50))
print(set1.issubset(set2))



set1 = set('Stepik')
set2 = set('stepik')
print(set1.issubset(set2))


word = 'beegeek'
set1 = set(word*3)
set2 = set(word[::-1]*2 + 'stepik')
print(set1 < set2)


set1 = {1, 2, 3, 4, 5, 6, 7, 8}
list1 = [1, 2, 3, 4, 5]
print(set1.issuperset(list1))


set1 = {'q', 'w', 'e', 'r', 't', 'y'}
list1 = ['y', 'w', 'r']

print(set1 >= list1)
