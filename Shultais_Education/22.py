is_non_negative_num = lambda x: x[0] != "-" and x.count('.') < 2 and x.upper() == x.lower()

print(is_non_negative_num('10.34ab'))
print(is_non_negative_num('10.45'))
print(is_non_negative_num('-18'))
print(is_non_negative_num('-34.67'))
print(is_non_negative_num('987'))
print(is_non_negative_num('abcd'))
print(is_non_negative_num('123.122.12'))
print(is_non_negative_num('123.122'))


#####
is_num = lambda x: x.count('-') < 2 and x.count('.') < 2 and x.upper() == x.lower() and x.rfind('-') <= 0

print(is_num('10.34ab'))
print(is_num('10.45'))
print(is_num('-18'))
print(is_num('-34.67'))
print(is_num('987'))
print(is_num('abcd'))
print(is_num('123.122.12'))
print(is_num('-123.122'))
print(is_num('--13.2'))


######
words = ['beverage', 'monday', 'abroad', 'bias', 'abuse', 'abolish', 'abuse', 'abuse', 'bid', 'wednesday', 'able', 'betray', 'accident', 'abduct', 'bigot', 'bet', 'abandon', 'besides', 'access', 'friday', 'bestow', 'abound', 'absent', 'beware', 'abundant', 'abnormal', 'aboard', 'about', 'accelerate', 'abort', 'thursday', 'tuesday', 'sunday', 'berth', 'beyond', 'benevolent', 'abate', 'abide', 'bicycle', 'beside', 'accept', 'berry', 'bewilder', 'abrupt', 'saturday', 'accessory', 'absorb']

a = sorted(words)
words_1 = list(filter(lambda x: len(x) == 6, a))
print(*words_1)


######

numbers = [46, 61, 34, 17, 56, 26, 93, 1, 3, 82, 71, 37, 80, 27, 77, 94, 34, 100, 36, 81, 33, 81, 66, 83, 41, 80, 80, 93, 40, 34, 32, 16, 5, 16, 40, 93, 36, 65, 8, 19, 8, 75, 66, 21, 72, 32, 41, 59, 35, 64, 49, 78, 83, 27, 57, 53, 43, 35, 48, 17, 19, 40, 90, 57, 77, 56, 80, 95, 90, 27, 26, 6, 4, 23, 52, 39, 63, 74, 15, 66, 29, 88, 94, 37, 44, 2, 38, 36, 32, 49, 5, 33, 60, 94, 89, 8, 36, 94, 46, 33]

num_1 = list(filter(lambda x: x % 2 == 0 or x <= 47, numbers))
num_2 = list(map(lambda x: x//2 if x % 2 == 0 else x, num_1))

print(*num_2)


#####

data = [(19542209, 'New York'), (4887871, 'Alabama'), (1420491, 'Hawaii'), (626299, 'Vermont'), (1805832, 'West Virginia'), (39865590, 'California'), (11799448, 'Ohio'), (10711908, 'Georgia'), (10077331, 'Michigan'), (10439388, 'Virginia'), (7705281, 'Washington'), (7151502, 'Arizona'), (7029917, 'Massachusetts'), (6910840, 'Tennessee')]

for pop, city in sorted(data, key=lambda x: x[1][-1], reverse=True):
    print(f'{city}: {pop}')

#####

data = [(19542209, 'New York'), (4887871, 'Alabama'), (1420491, 'Hawaii'), (626299, 'Vermont'), (1805832, 'West Virginia'), (39865590, 'California'), (11799448, 'Ohio'), (10711908, 'Georgia'), (10077331, 'Michigan'), (10439388, 'Virginia'), (7705281, 'Washington'), (7151502, 'Arizona'), (7029917, 'Massachusetts'), (6910840, 'Tennessee')]

data_1 = sorted(data, key = lambda x: x[1][-1], reverse = True)
print(*list(map(lambda x: f"{x[1]}: {x[0]}", data_1)),sep = "\n")


#####

data = ['год', 'человек', 'время', 'дело', 'жизнь', 'день', 'рука', 'раз', 'работа', 'слово', 'место', 'лицо', 'друг', 'глаз', 'вопрос', 'дом', 'сторона', 'страна', 'мир', 'случай', 'голова', 'ребенок', 'сила', 'конец', 'вид', 'система', 'часть', 'город', 'отношение', 'женщина', 'деньги']

data_1 = sorted(data, key = lambda x:(len(x), str(x)))
print(*data_1)

#####

mixed_list = ['tuesday', 'abroad', 'abuse', 'beside', 'monday', 'abate', 'accessory', 'absorb', 1384878, 'sunday', 'about', 454805, 'saturday', 'abort', 2121919, 2552839, 977970, 1772933, 1564063, 'abduct', 901271, 2680434, 'bicycle', 'accelerate', 1109147, 942908, 'berry', 433507, 'bias', 'bestow', 1875665, 'besides', 'bewilder', 1586517, 375290, 1503450, 2713047, 'abnormal', 2286106, 242192, 701049, 2866491, 'benevolent', 'bigot', 'abuse', 'abrupt', 343772, 'able', 2135748, 690280, 686008, 'beyond', 2415643, 'aboard', 'bet', 859105, 'accident', 2223166, 894187, 146564, 1251748, 2851543, 1619426, 2263113, 1618068, 'berth', 'abolish', 'beware', 2618492, 1555062, 'access', 'absent', 'abundant', 2950603, 'betray', 'beverage', 'abide', 'abandon', 2284251, 'wednesday', 2709698, 'thursday', 810387, 'friday', 2576799, 2213552, 1599022, 'accept', 'abuse', 'abound', 1352953, 'bid', 1805326, 1499197, 2241159, 605320, 2347441]
print(max(mixed_list, key = lambda x: x if type(x) == int else 0))

######

mixed_list = ['beside', 48, 'accelerate', 28, 'beware', 'absorb', 'besides', 'berry', 15, 65, 'abate', 'thursday', 76, 70, 94, 35, 36, 'berth', 41, 'abnormal', 'bicycle', 'bid', 'sunday', 'saturday', 87, 'bigot', 41, 'abort', 13, 60, 'friday', 26, 13, 'accident', 'access', 40, 26, 20, 75, 13, 40, 67, 12, 'abuse', 78, 10, 80, 'accessory', 20, 'bewilder', 'benevolent', 'bet', 64, 38, 65, 51, 95, 'abduct', 37, 98, 99, 14, 'abandon', 'accept', 46, 'abide', 'beyond', 19, 'about', 76, 26, 'abound', 12, 95, 'wednesday', 'abundant', 'abrupt', 'aboard', 50, 89, 'tuesday', 66, 'bestow', 'absent', 76, 46, 'betray', 47, 'able', 11]
print(*sorted(mixed_list, key = lambda x: (type(x) == str, x)))


######

print(*list(map(lambda x: 255 - x, list(map(int, input().split())))))

######

from functools import reduce

def evaluate(coefficients, x):
    # Функция для вычисления значения многочлена
    polynomial = lambda acc, coef: acc * x + coef
    result = reduce(polynomial, coefficients)
    return result

# Считываем коэффициенты многочлена
coefficients = list(map(int, input().split()))

# Считываем значение аргумента
x = int(input())

# Выводим результат
print(evaluate(coefficients, x))


######

print(all([True, True, True]))     #  возвращает True, так как все значения списка равны True
print(all([True, True, False]))    #  возвращает False, так как не все значения списка равны True

######

numbers = [17, 90, 78, 56, 231, 45, 5, 89, 91, 11, 19]

result = all(map(lambda x: True if x > 10 else False, numbers))

if result:
    print('Все числа больше 10')
else:
    print('Хотя бы одно число меньше или равно 10')


######

numbers = [1, 2, 3, 4, 5, 6]

for index, elem in enumerate(numbers):
    if elem % 2 == 0:
        numbers[index] *= 2

print(numbers)

######

numbers = [10, 30, 20, 50, 40, 60, 70, 80]

total = 0
for index, number in enumerate(numbers, 1):
    if index % 2 == 0:
        total += number
print(total)

######

list1 = [1, 2, 3, 4, 5]
list2 = [5, 4, 3, 2, 1]

result = 0
for x, y in zip(list1, list2):
    result += x*y
print(result)

#####


rint(sum(map(lambda x,y: x*y , list1,list2)))
print(sum(x*y for x,y in zip(list1,list2)))
print(sum([x*y for x,y in zip(list1,list2)]))

######

def ignore_command(command):
    ignore = ['alias', 'configuration', 'ip', 'sql', 'select', 'update', 'exec', 'del', 'truncate']
    return any(map(lambda x: x in command, ignore))


#####

def ignore_command(command):
    ignore = ['alias', 'configuration', 'ip', 'sql', 'select', 'update', 'exec', 'del', 'truncate']
    return any(i in command for i in ignore)

######

countries = ['Russia', 'USA', 'UK', 'Germany', 'France', 'India']
capitals = ['Moscow', 'Washington', 'London', 'Berlin', 'Paris', 'Delhi']
population = [145_934_462, 331_002_651, 80_345_321, 67_886_011, 65_273_511, 1_380_004_385]
for country, capital, population in zip(countries, capitals, population):
    print(f"{capital} is the capital of {country}, population equal {population} people.")

######


User avatar
Максим Кункевич
2 секунды назад

.
Верное решение #1107857615
Python 3.10

xxxx_list = list(map(lambda x: True if x.isdigit() and 0<=int(x) <=255 else False, input().split(".")))
print(all(xxxx_list))

######
a = int(input())
b = int(input())

def check(num):
    digits = set(str(num))
    return all(int(digit) != 0 and num % int(digit) == 0 for digit in digits)

result = [str(i) for i in range(a, b+1) if check(i) and '0' not in str(i)]
print(' '.join(result))

#####

def check(num):
    return all(map(lambda x: int(x) and num % int(x) == 0, str(num)))
print(*list(filter(lambda x: check(x), range(int(input()), int(input())+ 1))))

#####

a, b = int(input()), int(input())

for i in range(a, b + 1):
    # создаем кортеж со всеми цифрами числа
    digits = tuple(map(int, str(i)))

    # проверяем, что число не содержит 0 и делится на все свои цифры
    if 0 not in digits and all(map(lambda cur_digit: i % cur_digit == 0, digits)):
        print(i, end=" ")
######

s = input()
print("NO" if any([len(s) < 7, s.isupper(), s.islower(), s.isdigit(), s.isalpha()]) else "YES")

#####


n = int(input())
result = []

for _ in range(n):
    k = int(input())
    grades = [int(input().split()[1]) for _ in range(k)]
    result.append(any(grade == 5 for grade in grades))

print('YES' if all(result) else 'NO')
