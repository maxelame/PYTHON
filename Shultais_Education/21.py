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


