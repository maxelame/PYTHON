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


set1 = set(range(1, 10))
set2 = set(range(10, 20))
print(set1.isdisjoint(set2))


print("NO" if set(input()).isdisjoint(set(input())) else "YES")


set1, set2 = set(input()), set(input())
print("YES" if set2 <= set1 else "NO")

set1, set2, set3 = set(input().split()), set(input().split()), set(input().split())
set12 = set1 & set2 - set3
print(*(sorted(map(int, set12), reverse = True)))


set1, set2, set3 = set(input().split()), set(input().split()), set(input().split())
set4 = set1 & set2 & set3 # Находим значения которые повторяются сразу у ТРЕХ детёнышей
set_full = set1 | set2 | set3 # Находим общий список оценок
set_full.difference_update(set4) # Из общего списка оценок убрать значения которые повторяются сразу у троих
print(*(sorted(map(int, set_full))))



set1, set2, set3 = set(input().split()), set(input().split()), set(input().split())
print(*(sorted(map(int, (set1 | set2 | set3) - (set1 & set2 & set3)))))

set1, set2, set3 = set(input().split()), set(input().split()), set(input().split())
print(*(sorted(map(int, set3 -set2 - set1), reverse = True)))



set1, set2, set3 = set(input().split()), set(input().split()), set(input().split())
set_all = {'0','1','2','3','4','5','6','7','8','9','10'}
print(*sorted(map(int, set_all - set1 - set2 - set3)))


digits = {int(c) for c in input()}



items = [10, '30', 30, 10, '56', 34, '12', 90, 89, 34, 45, '67', 12, 10, 90, 23, '45', 56, '56', 1, 5, '6', 5]
set1 = {int(c) for c in items}
print(*sorted(set1))


words = ['Plum', 'Grapefruit', 'apple', 'orange', 'pomegranate', 'Cranberry', 'lime', 'Lemon', 'grapes', 'persimmon', 'tangerine', 'Watermelon', 'currant', 'Almond']
myset = {item.lower()[0] for item in words}
print(*sorted(myset))


sentence = '''My very photogenic mother died in a freak accident (picnic, lightning) when I was three, and, save for a pocket of warmth in the darkest past, nothing of her subsists within the hollows and dells of memory, over which, if you can still stand my style (I am writing under observation), the sun of my infancy had set: surely, you all know those redolent remnants of day suspended, with the midges, about some hedge in bloom or suddenly entered and traversed by the rambler, at the bottom of a hill, in the summer dusk; a furry warmth, golden midges.'''
myset = {word.lower().strip('.,():;') for word in sentence.split()}
print(*sorted(myset))



sentence = '''My very photogenic mother died in a freak accident (picnic, lightning) when I was three, and, save for a pocket of warmth in the darkest past, nothing of her subsists within the hollows and dells of memory, over which, if you can still stand my style (I am writing under observation), the sun of my infancy had set: surely, you all know those redolent remnants of day suspended, with the midges, about some hedge in bloom or suddenly entered and traversed by the rambler, at the bottom of a hill, in the summer dusk; a furry warmth, golden midges.'''

myset = {word.lower().strip('.,():;') for word in sentence.split() if len(word.lower().strip('.,():;')) < 4}
print(*sorted(myset))


files = ['python.png', 'qwerty.py', 'stepik.png', 'beegeek.org', 'windows.pnp', 'pen.txt', 'phone.py', 'book.txT', 'board.pNg', 'keyBoard.jpg', 'Python.PNg', 'apple.jpeg', 'png.png', 'input.tXt', 'split.pop', 'solution.Py', 'stepik.org', 'kotlin.ko', 'github.git']
myset = {word.lower() for word in files if word.lower()[-4:] == '.png'}
print(*sorted(myset))


set1 = frozenset('beegeek')
set2 = frozenset('stepik')

set3 = set1 & set2


dict1 = {'beegeek':2018}


my_dict = dict()

{'Canada': 'Ottawa', 'United States': 'Washington, D.C.', 'Mexico': 'Mexico City'}


stuff = {1: 'ааа', 2: 'ббб', 3: 'ввв'}
print(stuff[3])

my_dict = dict([('first', 1), ('second', 2), ('third', 3)])

print(my_dict)


my_dict = dict.fromkeys(['a', 'b', 'c'], -1)

print(my_dict['b'])


my_dict = dict.fromkeys(['a', 'b', 'c'], -1)
print(my_dict['d'])


my_dict = {1: [0, 1], 2: [2, 3], 3: [4, 5]}
print(my_dict[2][1])




int_dict = {2: 'two', 5: 'five', 7: 'seven', 9: 'nine'}
str_dict = {'three': 3, 'seven': 7, 'nine': 9}



Вы можете использовать методы строк strip() и replace() для удаления пробелов и замены двойных пробелов на одиночные.

Вот обновленный код, который решает эту задачу:

scss

alphabet = list('абвгдеёжзийклмнопрстуфхцчшщъыьэюя')
word = input().lower().strip() + ' запретил букву '

for letter in alphabet:
    if letter in word:
        print(word + letter)
        word = word.replace(letter, '').replace('  ', ' ')

word = word.replace('  ', ' ')
print(word)



set1 = {'Yellow', 'Orange', 'Black'}
set2 = {'Orange', 'Blue', 'Pink'}
set3 = set2.difference(set1)


set1 = {'Yellow', 'Orange', 'Black'}
set2 = {'Orange', 'Blue', 'Pink'}
set1.difference_update(set2)


myset = {'Yellow', 'Orange', 'Black'}

myset.update(['Blue', 'Green', 'Red', 'Orange'])
print(myset)
