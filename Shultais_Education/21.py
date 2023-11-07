######
def fancy(length, char1='-', char2='*'):
    return (char1 + char2) * length + char1


print(fancy(char2='!'))

######

def matrix(n =1,m = 0, a = 0):
    if n == 1 and not m:
        m = 1
    elif n != 1 and not m:
        m = n
    return [[a]*m for _ in range(n)]

######
def f(n=3):
    return n + 7


print(f(f(f())))

#####
def func(x, y, *args):


#####

def func(x, y, *args):
    return len(args)


print(func(10, 20, 30, 40, 50, 60))


#####

def func(*args):
    return max(args) + min(args)


print(func(10, 15, *[31, 42, 5, 1], *(17, 28, 19, 100), 13, 12))

######

func(5, 6, 13, 17, 56)
func(2, 7)

######

def count_args(*args):
  return len(args)

print(count_args([], (''), 'a', False))

######

def sq_sum(*args):
    return sum([m ** 2 for m in args])

######

def sq_sum(*a):
    return sum(map(lambda i: i*i, list(a)))

#####

def sq_sum(*args) -> int | float:
    return sum(map(lambda i: i*i, args))


#####

def mean(*args):
    s = [i for i in args if type(i) in [int, float]]
    return (float(0) if len(s) == 0 else float(sum(s)/len(s)))

######

def greet(x, *args):
    str1 = "Hello, " + x
    for i in args:
        str1 += " and " + i
    return str1


######



def greet(name, *args):
    return f'Hello, {" and ".join((name,) + args)}!'

#####

def print_products(*args):
    list1 = []
    for i in args:
        if type(i) in [str] and len(i) != 0:
            list1.append(i)
    if len(list1) == 0:
        print("Нет продуктов")
    else:
        for i in range(1, len(list1) + 1):
            print(f"{i}) {list1[i-1]}")


#####
def info_kwargs(*kwargs):
    for key, value in sorted(kwargs.items()):
        print(f"{key}: {value}")


info_kwargs(first_name='Timur', last_name='Guev', age=28, job='teacher')


#####
#Парадигма программирования это совокупность идей и понятий, определяющих стиль написания компьютерных программ


#
#    Парадигмы программирования
#    Императивное программирование
#    Структурное программирование
#    Объектно-ориентированное программирование
#    Логическое программирование
#    Функциональное программирование


#Кто предложил парадигму структурного программирования? Эдсгер Дейкстра

#Язык Python является  мультипарадигменным языком программирования

#Функциональное программирование это это декларативная парадигма программирования


#Основные принципы функционального программирования это: неизменяемые переменные, рекурсии, функции высшегопордка, чистые функции, лямбда-выражения


s1 = 'python'
s2 = 'stepicon'
s3 = 'beegeek'

print(min(s1, s2, s3))
print(max(s1, s2, s3))

s1 = 'python'
s2 = 'stepicon'
s3 = 'beegeek'

print(min(s1, s2, s3, key=len))
print(max(s1, s2, s3, key=len))



def f(x):
    return x**2
g = f
print(f(3), g(5))



def f(x):
    return x**2
def g(x):
    return x**3
funcs = [f, g]
print(funcs[0](5), funcs[1](5))




def comparator(pair):
    return pair[1]
pairs = [(5, 4), (3, 2), (1, 7), (8, 2)]
pairs.sort(key=comparator)
print(pairs)




def comparator(pair):
    return pair[0] + pair[1]
pairs = [(5, 4), (3, 2), (1, 7), (8, 2)]
pairs.sort(key=comparator, reverse=True)
print(pairs)



words = ['this', 'is', 'a', 'test', 'of', 'sorting']
words.sort(key=len)
print(words)



def f1(x):
    return 2*x+1
def f2(x):
    return x**2
def f3(x):
    return -x**2+1
def f4(x):
    return x-3
funcs = [f1, f2, f3, f4]
i = int(input())
print(funcs[i](2))

#####
from statistics import mean # функция mean - соответствует среднему арифметическому
numbers = [(10, 10, 10), (30, 45, 56), (81, 39), (1, 2, 3), (12,), (-2, -4, 100), (1, 2, 99), (89, 9, 34), (10, 20, 30, -2), (50, 40, 50), (34, 78, 65), (-5, 90, -1, -5), (1, 2, 3, 4, 5, 6), (-9, 8, 4), (90, 1, -45, -21)]

numbers.sort(key=mean) # сортируем по среднему арифметическому

print(numbers[0])
print(numbers[-1])



points = [(-1, 1), (5, 6), (12, 0), (4, 3), (0, 1), (-3, 2), (0, 0), (-1, 3), (2, 0), (3, 0), (-9, 1), (3, 6), (8, 8)]

def direct(item):
    return (item[0]**2 + item[-1]**2) ** 0.5

points.sort(key=direct)

print(points)



numbers = [(10, 10, 10), (30, 45, 56), (81, 80, 39), (1, 2, 3), (12, 45, 67), (-2, -4, 100), (1, 2, 99), (89, 90, 34), (10, 20, 30), (50, 40, 50), (34, 78, 65), (-5, 90, -1)]
def func(item):
    return min(item) + max(item)
numbers.sort(key = func)

print(numbers)



athletes = [('Дима', 10, 130, 35), ('Тимур', 11, 135, 39), ('Руслан', 9, 140, 33), ('Рустам', 10, 128, 30), ('Амир', 16, 170, 70), ('Рома', 16, 188, 100), ('Матвей', 17, 168, 68), ('Петя', 15, 190, 90)]

n = int(input())
athletes.sort(key = lambda x: x[n-1])
for i in athletes:
    print(*i)


######
s_list = input().split()
print(*sorted(s_list, key = lambda x: sum(int(j) for j in x)))


#####
func_dict = {'квадрат': lambda x : x ** 2,
             'куб': lambda x : x ** 3,
             'корень': lambda x: x ** 0.5,
             'модуль': abs,
             'синус': math.sin}

#####

def high_order_function(func):
    return func(10)

def square(x):
    return x**2

def minus_one(x):
    return x - 1

num1 = high_order_function(square)
num2 = high_order_function(minus_one)

print(num1*num2)

#####


words = ['abba', 'qwerty', 'python', 'a', 'deed', 'nun', 'level', 'deified', 'bbbbb', 'mother', 'surface', 'sister']

words_len = map(len, words)
print(max(words_len))

#Функция map():

def map(function, items):
    result = []
    for item in items:
        result.append(function(item))
    return result


####s

def predicate(word):
    return word == word[::-1]


words = ['abba', 'qwerty', 'python', 'a', 'deed', 'nun', 'level', 'language', 'deified', 'bbbbb', 'mother', 'sister', 'surface', '1234321']
filtered = filter(predicate, words)
print(len(filtered))

####Функция filter():

def filter(function, items):
    result = []
    for item in items:
        if function(item):
            result.append(item)
    return result

######

numbers = [-2, 45, 45, -7, -45, 37, -42, 27, -58, -58, -12, -27, -49, -27, -56, 4, -99, -11, 86]

var1 = max(numbers, key=abs)
var2 = min(map(abs, numbers))

print(var1 + var2)

#Функция map():

def map(function, items):
    result = []
    for item in items:
        result.append(function(item))
    return result

####
def map(function, items):
    result = []
    for item in items:
        result.append(function(item))
    return result


numbers = [3.56773, 5.57668, 4.00914, 56.24241, 9.01344, 32.12013, 23.22222, 90.09873, 45.45, 314.1528, 2.71828, 1.41546]

numbers = map(lambda x: round(x, 2), numbers)
print(*numbers, sep = "\n")


#####


def map(function, items):
    result = []
    for item in items:
        result.append(function(item))
    return result


def filter(function, items):
    result = []
    for item in items:
        if function(item):
            result.append(item)
    return result


numbers = [1014, 1321, 675, 1215, 56, 1386, 1385, 431, 1058, 486, 1434, 696, 1016, 1084, 424, 1189, 475, 95, 1434, 1462, 815, 776, 657, 1225, 912, 537, 1478, 1176, 544, 488, 668, 944, 207, 266, 1309, 1027, 257, 1374, 1289, 1155, 230, 866, 708, 144, 1434, 1163, 345, 394, 560, 338, 232, 182, 1438, 1127, 928, 1309, 98, 530, 1013, 898, 669, 105, 130, 1363, 947, 72, 1278, 166, 904, 349, 831, 1207, 1496, 370, 725, 926, 175, 959, 1282, 336, 1268, 351, 1439, 186, 273, 1008, 231, 138, 142, 433, 456, 1268, 1018, 1274, 387, 120, 340, 963, 832, 1127]

numbers = filter(lambda x: x in range(102, 999, 5), numbers)

num_3 = map(lambda x: x ** 3, numbers)
print(*num_3, sep = "\n")


#####

def reduce(operation, items, initial_value):
    acc = initial_value
    for item in items:
        acc = operation(acc, item)
    return acc


numbers = [97, 42, 9, 32, 3, 45, 31, 77, -1, 11, -2, 75, 5, 51, 34, 28, 46, 1, -8, 84, 16, 51, 90, 56, 65, 90, 23, 35, 11, -10, 70, 90, 90, 12, 96, 58, -8, -4, 91, 76, 94, 60, 72, 43, 4, -6, -5, 51, 58, 60, 30, 38, 67, 62, 36, 72, 34, 82, 62, -1, 60, 82, 87, 81, -7, 57, 26, 36, 17, 43, 80, 40, 75, 94, 91, 64, 38, 72, 29, 84, 38, 35, 7, 54, 31, 95, 78, 27, 82, 1, 64, 94, 31, 29, -8, 98, 24, 61, 7, 73]

print(reduce(lambda x,y: x + y ** 2, numbers, 0))

#####

numbers = list(filter(lambda x: x % 7 == 0 and (13<x<99 or -99<x<-13), numbers))

print(sum(map(lambda x: x ** 2, numbers)))


#####

def func_apply(fun, lst):
    return list(map(fun, lst))


def increase(num):
    return num + 7


numbers = [1, 2, 3, 4, 5, 6]
new_numbers = map(increase, numbers)

for num in new_numbers:    #  итерируем циклом for
    print(num)
######

def func(elem):
    return elem >= 0


numbers = [-1, 2, -3, 4, 0, -20, 10]
positive_numbers = list(filter(func, numbers))  #  преобразуем итератор в список

print(positive_numbers)

