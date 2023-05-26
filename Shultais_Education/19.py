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


myset = {'Yellow', 'Orange', 'Black'}
print(myset[1])


set1 = {10, 20, 30, 40, 50}
set2 = {60, 70, 10, 30, 40, 80, 20, 50}
print(set1.issubset(set2))
print(set2.issuperset(set1))


myset = {'Yellow', 'Orange', 'Black'}
myset.discard('Blue')
print(myset)


set1 = {'p', 'a', 't', 'f'}
set2 = {'a', 't', 'f'}
print(set1 - set2)


n, m, k, p = int(input()), int(input()), int(input()), int(input())
print(n-(m+k-p))


lst = [i for i in input().split()]
print(len(lst) - len(set(lst)))


n = int(input())
lst = [input() for _ in range(n +1)]
print("OK" if len(set(lst)) == n + 1 else "REPEAT")


m, n = int(input()), int(input())
set1 = [input() for _ in range(m)]
set2= [input() for _ in range(n)]
for i in set2:
    print("YES" if i in set1 else "NO")


set1, set2 = set(input().split()), set(input().split())
if len(set2 & set1) != 0:
    print(*sorted(set2 & set1, reverse = True, key = int))
else:
    print("BAD DAY")

set1, set2 = set(input().split()), set(input().split())
if len(set2 & set1) == len(set1):
    print("YES")
else:
    print("NO")



set1, set2 = set(input().split()), set(input().split())
if set2 == set1:
    print("YES")
else:
    print("NO")


m = int(input())
n = int(input())
set1 = set([input() for _ in range(m)])
set2 = set([input() for _ in range(n)])
print(len(set1-set2))


m = int(input())
n = int(input())
set1 = set([input() for _ in range(m)])
set2 = set([input() for _ in range(n)])
set3 = set1.symmetric_difference(set2)
if len(set3) != 0:
    print(len(set3))
else:
    print("NO")



set1, set2 = set(input().split()), set(input().split())
set3 = set1 | set2
print(*sorted(set3))



m = int(input())
n = int(input())
list1 = [input() for _ in range(m + n)]
set1 = set(list1)
if m + n - 2*(len(list1) - len(set1)) != 0:
    print(m + n - 2*(len(list1) - len(set1)))
else:
    print("NO")



# Вводим количество уроков
m = int(input())

# Вводим количество учеников на первом уроке и создаем множество учеников, посетивших первый урок
n = int(input())
set1 = set(input().strip() for _ in range(n))

# Создаем пустое множество для последующих операций
empty_set = set()

# Если урок был один, выводим отсортированный список учеников, которые были на нем
if m == 1:
    for student in sorted(set1):
        print(student)

# Если уроков больше одного, то...
else:
    # Перебираем все уроки, начиная со второго
    for i in range(1, m):
        # Вводим количество учеников на i-ом уроке и создаем множество учеников, которые были на нем
        n = int(input())
        set2 = set(input().strip() for _ in range(n))
        # Находим учеников, которые были на первом и i-ом уроке
        set1.intersection_update(set2)
        # Очищаем множество set2
        set2.clear()

    # Выводим отсортированный список учеников, которые были на всех уроках
    for student in sorted(set1):
        print(student)


m = int(input())
n = int(input())
list1 = [input() for _ in range(m + n)]
set1 = set(list1)
if m + n - 2*(len(list1) - len(set1)) != 0:
    print(m + n - 2*(len(list1) - len(set1)))
else:
    print("NO")




stuff = {1:'ааа', 2:'ббб', 3:'ввв', 4:'ггг'}

print(len(stuff))


dict1 = {'key1':1, 'key2':2}
dict2 = {'key2':2, 'key1':1}

print(dict1 == dict2)


my_dict = {'foo': 100, 'bar': 200, 'baz': 300}

print(my_dict['bar':'baz'])




my_dict = {1: [0, 1], 2: [2, 3], 3: [4, 5]}
for k in my_dict:
    print(k)


my_dict = {1: [0, 1], 2: [2, 3], 3: [4, 5]}
for k in my_dict.values():
    print(k)


users = [{'name': 'Todd', 'phone': '551-1414', 'email': 'todd@gmail.com'},
         {'name': 'Helga', 'phone': '555-1618', 'email': 'helga@mail.net'},
         {'name': 'Olivia', 'phone': '449-3141', 'email': ''},
         {'name': 'LJ', 'phone': '555-2718', 'email': 'lj@gmail.net'},
         {'name': 'Ruslan', 'phone': '422-145-9098', 'email': 'rus-lan.cha@yandex.ru'},
         {'name': 'John', 'phone': '233-421-32', 'email': ''},
         {'name': 'Lara', 'phone': '+7998-676-2532', 'email': 'g.lara89@gmail.com'},
         {'name': 'Alina', 'phone': '+7948-799-2434', 'email': 'ali.ch.b@gmail.com'},
         {'name': 'Robert', 'phone': '420-2011', 'email': ''},
         {'name': 'Riyad', 'phone': '128-8890-128', 'email': 'r.mahrez@mail.net'},
         {'name': 'Khabib', 'phone': '+7995-600-9080', 'email': 'kh.nurmag@gmail.com'},
         {'name': 'Olga', 'phone': '6449-314-1213', 'email': ''},
         {'name': 'Roman', 'phone': '+7459-145-8059', 'email': 'roma988@mail.ru'},
         {'name': 'Maria', 'phone': '12-129-3148', 'email': 'm.sharapova@gmail.com'},
         {'name': 'Fedor', 'phone': '+7445-341-0545', 'email': ''},
         {'name': 'Tim', 'phone': '242-449-3141', 'email': 'timm.ggg@yandex.ru'}]

result = [user['name'] for user in users if user['phone'].endswith('8')]

print(*sorted(result))




users = [{'name': 'Todd', 'phone': '551-1414', 'email': 'todd@gmail.com'},
         {'name': 'Helga', 'phone': '555-1618', 'email': 'helga@mail.net'},
         {'name': 'Olivia', 'phone': '449-3141', 'email': ''},
         {'name': 'LJ', 'phone': '555-2718', 'email': 'lj@gmail.net'},
         {'name': 'Ruslan', 'phone': '422-145-9098', 'email': 'rus-lan.cha@yandex.ru'},
         {'name': 'John', 'phone': '233-421-32', 'email': ''},
         {'name': 'Lara', 'phone': '+7998-676-2532', 'email': 'g.lara89@gmail.com'},
         {'name': 'Alina', 'phone': '+7948-799-2434', 'email': 'ali.ch.b@gmail.com'},
         {'name': 'Robert', 'phone': '420-2011', 'email': ''},
         {'name': 'Riyad', 'phone': '128-8890-128', 'email': 'r.mahrez@mail.net'},
         {'name': 'Khabib', 'phone': '+7995-600-9080', 'email': 'kh.nurmag@gmail.com'},
         {'name': 'Olga', 'phone': '6449-314-1213', 'email': ''},
         {'name': 'Roman', 'phone': '+7459-145-8059', 'email': 'roma988@mail.ru'},
         {'name': 'Maria', 'phone': '12-129-3148', 'email': 'm.sharapova@gmail.com'},
         {'name': 'Fedor', 'phone': '+7445-341-0545', 'email': ''},
         {'name': 'Tim', 'phone': '242-449-3141', 'email': 'timm.ggg@yandex.ru'}]
list1 = []
for k in users:
    if k['phone'][-1] == '8':
        list1.append(k['name'])
print(*sorted(list1))



users = [{'name': 'Todd', 'phone': '551-1414', 'email': 'todd@gmail.com'},
         {'name': 'Helga', 'phone': '555-1618'},
         {'name': 'Olivia', 'phone': '449-3141', 'email': ''},
         {'name': 'LJ', 'phone': '555-2718', 'email': 'lj@gmail.net'},
         {'name': 'Ruslan', 'phone': '422-145-9098', 'email': 'rus-lan.cha@yandex.ru'},
         {'name': 'John', 'phone': '233-421-32', 'email': ''},
         {'name': 'Lara', 'phone': '+7998-676-2532', 'email': 'g.lara89@gmail.com'},
         {'name': 'Alina', 'phone': '+7948-799-2434'},
         {'name': 'Robert', 'phone': '420-2011', 'email': ''},
         {'name': 'Riyad', 'phone': '128-8890-128', 'email': 'r.mahrez@mail.net'},
         {'name': 'Khabib', 'phone': '+7995-600-9080', 'email': 'kh.nurmag@gmail.com'},
         {'name': 'Olga', 'phone': '6449-314-1213', 'email': ''},
         {'name': 'Roman', 'phone': '+7459-145-8059'},
         {'name': 'Maria', 'phone': '12-129-3148', 'email': 'm.sharapova@gmail.com'},
         {'name': 'Fedor', 'phone': '+7445-341-0545', 'email': ''},
         {'name': 'Tim', 'phone': '242-449-3141', 'email': 'timm.ggg@yandex.ru'}]

list1 = []
for k in users:
    if not k.get('email'):
        list1.append(k['name'])
print(*sorted(list1))



d = {
    0: "zero",
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine"
}
number = list(input())
for k in number:
    print(d[int(k)], end= ' ')


d = {
'CS101': (3004,'Хайнс','8:00'),
'CS102': (4501,'Альварадо','9:00'),
'CS103': (6755,'Рич','10:00'),
'NT110': (1244,'Берк','11:00'),
'CM241': (1411,'Ли','13:00')
}
course = input()

print(course + ":", end = " ")
print(*d[course], sep = ", ")



d={".":'1', ",":'11', "?":'111', "!":'1111', ":":'11111',
    "A":'2', "B":'22', "C":'222',
    "D":'3', "E":'33', "F":'333',
    "G":'4', "H":'44', "I":'444',
    "J":'5', "K":'55', "L":'555',
    "M":'6', "N":'66', "O":'666',
    "P":'7', "Q":'77', "R":'777', "S": '7777',
    "T":'8', "U":'88', "V":'888',
    "W":'9', "X":'99', "Y":'999', "Z": '9999',
    " ":'0'
}

phrase = input().upper().replace('"', '')
for i in phrase:
    print(d[i], end = "")



letters = [c for c in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789']
morse = ['.-', '-...', '-.-.', '-..', '.', '..-.', '--.', '....', '..', '.---', '-.-', '.-..', '--', '-.', '---', '.--.', '--.-', '.-.', '...', '-', '..-', '...-', '.--', '-..-', '-.--', '--..', '-----', '.----', '..---', '...--', '....-', '.....', '-....', '--...', '---..', '----.']

phrase = list(input().upper())
for i in phrase:
    if i in letters:
        print(morse[letters.index(i)], end = " ")


letters = [c for c in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789']
morse = ['.-', '-...', '-.-.', '-..', '.', '..-.', '--.', '....', '..', '.---', '-.-', '.-..', '--', '-.', '---', '.--.', '--.-', '.-.', '...', '-', '..-', '...-', '.--', '-..-', '-.--', '--..', '-----', '.----', '..---', '...--', '....-', '.....', '-....', '--...', '---..', '----.']
mydict = dict(zip(letters, morse))
word = input().upper()

for c in word:
    if c in mydict:
        print(mydict[c], end=' ')



numbers = [9, 8, 32, 1, 10, 1, 10, 23, 1, 4, 10, 4, 2, 2, 2, 2, 1, 10, 1, 2, 2, 32, 23, 23]

result = {}
for num in numbers:
    if num not in result:
        result[num] = 1
    else:
        result[num] += 1



# упрощаем


numbers = [9, 8, 32, 1, 10, 1, 10, 23, 1, 4, 10, 4, 2, 2, 2, 2, 1, 10, 1, 2, 2, 32, 23, 23]

result = {}
for num in numbers:
    result[num] = result.get(num, 0) + 1



get()
update()
pop()
popitem()
clear()
copy()
items()
keys()
values()
получает значение в словаре по ключу
объединяет словари
возвращает значение по указанному ключу, удаляя из словаря пару (ключ, значение)
возвращает последнюю добавленную пару (ключ, значение), удаляя её из словаря
удаляет все элементы из словаря
создает копию словаря
возвращает элементы словаря в виде пар (ключ, значение)
возвращает список ключей словаря
возвращает список значений словаря



dct = {'понедельник': 1, 'вторник': 2, 'среда': 3}
print(dct.get('понедельник', 'Не найдено'))


dct = {'понедельник': 1, 'вторник': 2, 'среда': 3}
print(dct.get('пятница', 'Не найдено'))


student = {'name': 'Rosaly',
           'class': 10,
           'marks': 75}

studet.clear()


student = {'name': 'Rosaly',
           'class': 10,
           'marks': 75}

student.clear()
print(student)


del student
print(student)
