#Дополните приведенный код, используя генератор, так, чтобы получить словарь result,
# состоящий из всех элементов словаря months , в которых ключ и значение поменялись местами.

months = {1: 'January', 2: 'February', 3: 'March', 4: 'April', 5: 'May', 6: 'June', 7: 'July', 8: 'August', 9: 'September', 10: 'October', 11: 'November', 12: 'December'}
result = {months[i] : i for i in months}

####
#В переменной s хранится строка пар число:слово. Дополните приведенный код, используя
# генератор, чтобы получить словарь result , в котором числа будут ключами, а слова – значениями.
s = '1:men 2:kind 90:number 0:sun 34:book 56:mountain 87:wood 54:car 3:island 88:power 7:box 17:star 101:ice'
result = {int(i.split(":")[0]) : i.split(":")[1] for i in s.split()}


####
numbers = [34, 10, 4, 6, 10, 23, 90, 100, 21, 35, 95, 1, 36, 38, 19, 1, 6, 87, 1000, 13456, 360]
def divv(i):
    list1 = []
    for k in range(1, i+1):
        if i % k == 0:
            list1.append(k)
    return list1
result = {i : divv(i) for i in numbers}
print(result)


#####
words = ['hello', 'bye', 'yes', 'no', 'python', 'apple', 'maybe', 'stepik', 'beegeek']
result = {i: [ord(t) for t in i] for i in words}

#####
letters = {0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E', 5: 'F', 6: 'G', 7: 'H', 8: 'I', 9: 'J', 10: 'K', 11: 'L', 12: 'M', 13: 'N', 14: 'O', 15: 'P', 16: 'Q', 17: 'R', 18: 'S', 19: 'T', 20: 'U', 21: 'V', 22: 'W', 23: 'X', 24: 'Y', 26: 'Z'}
remove_keys = [1, 5, 7, 12, 17, 19, 21, 24]
result = {i : letters[i] for i in letters if i not in remove_keys}

#####


students = {'Timur': (170, 75), 'Ruslan': (180, 105), 'Soltan': (192, 68), 'Roman': (175, 70), 'Madlen': (160, 50), 'Stefani': (165, 70), 'Tom': (190, 90), 'Jerry': (180, 87), 'Anna': (172, 67), 'Scott': (168, 78), 'John': (186, 79), 'Alex': (195, 120), 'Max': (200, 110), 'Barak': (180, 89), 'Donald': (170, 80), 'Rustam': (186, 100), 'Alice': (159, 59), 'Rita': (170, 80), 'Mary': (175, 69), 'Jane': (190, 80)}
result = {i : students[i] for i in students if (students[i][0] > 167 and students[i][1] < 75)}

#####
tuples = [(1, 2, 3), (4, 5, 6), (7, 8, 9), (10, 11, 12), (13, 14, 15), (16, 17, 18), (19, 20, 21), (22, 23, 24), (25, 26, 27), (28, 29, 30), (31, 32, 33), (34, 35, 36)]
result = {i[0]: (i[1],i[2]) for i in tuples}


#####
student_ids = ['S001', 'S002', 'S003', 'S004', 'S005', 'S006', 'S007', 'S008', 'S009', 'S010', 'S011', 'S012', 'S013']
student_names = ['Camila Rodriguez', 'Juan Cruz', 'Dan Richards', 'Sam Boyle', 'Batista Cesare', 'Francesco Totti', 'Khalid Hussain', 'Ethan Hawke', 'David Bowman', 'James Milner', 'Michael Owen', 'Gary Oldman', 'Tom Hardy']
student_grades = [86, 98, 89, 92, 45, 67, 89, 90, 100, 98, 10, 96, 93]

result = [{i: {j: k}} for i, j, k in zip(student_ids, student_names, student_grades)] # для соединения используем функцию ZIP

#####
student_ids = ['S001', 'S002', 'S003', 'S004', 'S005', 'S006', 'S007', 'S008', 'S009', 'S010', 'S011', 'S012', 'S013']
student_names = ['Camila Rodriguez', 'Juan Cruz', 'Dan Richards', 'Sam Boyle', 'Batista Cesare', 'Francesco Totti', 'Khalid Hussain', 'Ethan Hawke', 'David Bowman', 'James Milner', 'Michael Owen', 'Gary Oldman', 'Tom Hardy']
student_grades = [86, 98, 89, 92, 45, 67, 89, 90, 100, 98, 10, 96, 93]

result = [{student_ids[i]: {student_names[i] : student_grades[i]}} for i in range(len(student_ids))] # вариант без ZIP

#####
import random

random.seed(17)   # явно устанавливаем начальное значение для генератора случайных чисел

for _ in range(10):
    print(random.randint(1, 100))

######
import random
num = random.randint(1, 118)

#####
import random
num = random.random()

####
import random
num = random.uniform()

#####
import random
num = random.randrange(115)

#####
import random
num = random.randrange(9, 81)

#####
import random
num = random.randrange(15, 50, 5)

#####
import random
n = int(input())    # количество попыток
for _ in range(n):
    print("Орел" if random.randint(0, 1) else "Решка")

#####
import random
n = int(input())    # количество попыток
for _ in range(n):
    print(random.randint(1, 6))

#####
import random
length = int(input())    # длина пароля
for _ in range(length):
    print((chr(random.choice([random.randint(65,90), random.randint(97,122)]))), end = '')

#####
import random
set1 = set()
while len(set1) < 7:
    set1.add(random.randint(1, 49))
print(*sorted(set1))

#####
import random
numbers = [1, 2, 3, 5, 7]
num = random.choice(numbers)

#####
import random
numbers = list(range(2, 10, 2))
num = random.choice(numbers)

#####
import random
numbers = [1, 2, 4, 6, 7, 9]
rand_numbers = random.sample(numbers, 3)

#####
from random import randint
def generate_ip():
    return f"{randint(0, 255)}.{randint(0, 255)}.{randint(0, 255)}.{randint(0, 255)}"
print(generate_ip())

#####
from random import randrange as rr
def generate_ip():
    return f'{rr(255)}.{rr(255)}.{rr(255)}.{rr(255)}'
print(generate_ip())



#####
import random
matrix = [[1, 2, 3, 4],
          [5, 6, 7, 8],
          [9, 10, 11, 12],
          [13, 14, 15, 16]]
random.shuffle(matrix)
print(matrix)

######
import random
matrix = list("0123456789")
for i in range(6):
    random.shuffle(matrix)
    print(*matrix, sep='')


######
import random
lst = []
while len(lst) < 100:
    i = str(random.randrange(1, 10)) + str(''.join(random.sample(list("0123456789"), 6)))
    if i not in lst:
        lst += [i]
print(*lst, sep = "\n")

#####
from random import sample as r
print(*r(range(int(1e6), int(1e7)), 100), sep='\n')

#####
import random
word = list(input())
random.shuffle(word)
print("".join(word))

#####

import random
lst = [random.randint(1, 75) for i in range(75)]
set1 = set(lst)
k= 0
for i in range(5):
    for j in range(5):
        if (i ==2 and j == 2):
            print("0".ljust(3), end="")
        else:
            print(str(list(set1)[k]).ljust(3), end="")
            k += 1
    print()

#####

import random
n = int(input())
lst = [input() for _ in range(n)]
for i in range(n):
    print(f"{i} - {random.choice(lst[1:])}")
    lst = lst[1:] + [i]

#####
import random
lst1 = [input() for _ in range(int(input()))]
lst2 = lst1.copy()
flag = 0
while flag != 1:
    random.shuffle(lst2)
    flag = 1
    for i in range(len(lst1)):
        if lst1[i] == lst2[i]:
            flag = 0
for i in range(len(lst1)):
    print(lst1[i], '-', lst2[i])


######
import string, random
def generate_password(length):
    symbols = "lI1oO0"
    st = string.ascii_letters + string.digits
    for i in symbols:
        st = st.replace(i,"")
    password = ""
    for i in range(length):
        password += random.choice(st)
    return password

def generate_passwords(count, length):
    for i in range(count):
        print(generate_password(length))

n, m = int(input()), int(input())
generate_passwords(n, m)

######
data = [
    'a',
    'b',
    {
        'foo': 1,
        'bar':
        {
            'x' : 10,
            'y' : 20,
            'z' : 30
        },
        'baz': 3
    },
    'c',
    'd'
]

######

my_dict = {'C1': [10, 20, 30, 7, 6, 23, 90], 'C2': [20, 30, 40, 1, 2, 3, 90, 12], 'C3': [12, 34, 20, 21], 'C4': [22, 54, 209, 21, 7], 'C5': [2, 4, 29, 21, 19], 'C6': [4, 6, 7, 10, 55], 'C7': [4, 8, 12, 23, 42], 'C8': [3, 14, 15, 26, 48], 'C9': [2, 7, 18, 28, 18, 28]}
my_dict = {i : [j for j in my_dict[i] if j < 21] for i in my_dict}

######

emails = {'nosu.edu': ['timyr', 'joseph', 'svetlana.gaeva', 'larisa.mamuk'],
          'gmail.com': ['ruslan.chaika', 'rustam.mini', 'stepik-best'],
          'msu.edu': ['apple.fruit', 'beegeek', 'beegeek.school'],
          'yandex.ru': ['surface', 'google'],
          'hse.edu': ['tomas-henders', 'cream.soda', 'zivert'],
          'mail.ru': ['angel.down', 'joanne', 'the.fame.moster']}
lst = []
for i in emails:
    for j in emails[i]:
        lst += [str(j) + "@" + str(i)]
print(*sorted(lst), sep = '\n')

#####
dnk = input()
dict1 = {'G' : 'C', 'C' : 'G', 'T' : 'A', 'A' : 'U'}
rnk = ''
for i in dnk:
    rnk += dict1[i]
print(rnk)

######
lst = input().split()
dict1 = {}
for i in lst:
    if i in dict1:
        dict1[i] += 1
    else:
        dict1[i] = 1
    print(dict1[i], end=" ")

#####
lst = list(input())
d = {
    1: "AEILNORSTU",
    2: "DG",
    3: "BCMP",
    4: "FHVWY",
    5: "K",
    8: "JX",
    10: "QZ"
}
summ = 0
for i in lst:
    for q in d:
        if i in d[q]:
            summ += q
print(summ)

#####

def restore_access():
    s = {'write': 'W', 'read': 'R','execute': 'X'}
    n = int(input())
    files = {}
    for _ in range(n):
        file, permissions = input().split(' ', 1)
        files[file] = set(permissions)

    m = int(input())
    for _ in range(m):
        operation, file = input().split()
        if s[operation] in files[file]:
            print("OK")
        else:
            print("Access denied")

restore_access()

######
def count_items():
    n = int(input())
    data = {}
    buyers = set()
    for _ in range(n):
        buyer, item, quantity = input().split()
        buyers.add(buyer)
        if buyer not in data:
            data[buyer] = {}
        if item not in data[buyer]:
            data[buyer][item] = 0
        data[buyer][item] += int(quantity)

    buyers = sorted(buyers)
    for buyer in buyers:
        print(f"{buyer}:")
        items = sorted(data[buyer])
        for item in items:
            print(f"{item} {data[buyer][item]}")

count_items()


#####

import string, random
def generate_password(length):
    symbols = "lI1oO0"
    st1 = string.ascii_uppercase
    st2 = string.ascii_lowercase
    st3 = string.digits
    for i in symbols:
        st1 = st1.replace(i,"")
        st2 = st2.replace(i, "")
        st3 = st3.replace(i, "")
    password = random.choice(st1) + random.choice(st2) + random.choice(st3)
    for i in range(length - 3):
        password += random.choice(st1 + st2 + st3)
    return password

def generate_passwords(count, length):
    for i in range(count):
        print(generate_password(length))

n, m = int(input()), int(input())
generate_passwords(n, m)

######


import string, random
def generate_password(length):
    symbols = "lI1oO0"
    st1 = string.ascii_uppercase
    st2 = string.ascii_lowercase
    st3 = string.digits
    for i in symbols:
        st1 = st1.replace(i,"")
        st2 = st2.replace(i, "")
        st3 = st3.replace(i, "")
    password = random.choice(st1) + random.choice(st2) + random.choice(st3)
    for i in range(length - 3):
        password += random.choice(st1 + st2 + st3)
    return password

def generate_passwords(count, length):
    for i in range(count):
        print(generate_password(length))

n, m = int(input()), int(input())
generate_passwords(n, m)

#####
def restore_access():
    s = {'write': 'W', 'read': 'R','execute': 'X'}
    n = int(input())
    files = {}
    for _ in range(n):
        file, permissions = input().split(' ', 1)
        files[file] = set(permissions)

    m = int(input())
    for _ in range(m):
        operation, file = input().split()
        if s[operation] in files[file]:
            print("OK")
        else:
            print("Access denied")

restore_access()

######

import random

n = 10**6       # количество испытаний
k = 0
s0 = 16
for _ in range(n):
    x = random.uniform(-2, 2)
    y = random.uniform(-2, 2)

    if x**3 + y**4 + 2 >= 0 and 3*x + y**2 <= 2:
        k += 1

print((k/n)*s0)

######

import random

n = 10**6       # количество испытаний
k = 0
s0 = 4
for _ in range(n):
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)

    if x**2 + y**2 <= 1:
        k += 1

print((k/n)*s0)

######
from decimal import *
from math import *

num1 = Decimal('1.44')
num2 = Decimal('0.523')

print(sqrt(num1))
print(sin(num2))
print(log(num1 + num2))


######
from decimal import *
from math import *
num1 = Decimal('1.44')
num2 = Decimal('0.523')

print(sqrt(num1))
print(sin(num2))
print(log(num1 + num2))

######
num = 0.1 + 0.1 + 0.1

if num == 0.3:
    print('YES')
else:
    print('NO')

#####

from decimal import *

num = Decimal('-1.4568769017')
num_tuple = num.as_tuple()

print(num_tuple.sign)
print(num_tuple.digits)
print(num_tuple.exponent)


#####

from decimal import *

print(getcontext())

######

from decimal import *

getcontext().prec = 3      # устанавливаем точность в 3 знака

num = Decimal('3.1415')

print(num)
print(num * 1)
print(num * 2)
print(num / 2)

#####

from decimal import *

getcontext().prec = 4                    # устанавливаем точность числа

num = Decimal('3.1415926535')

print(num.quantize(Decimal('1.000')))    #  округление до 3 цифр в дробной части
print(num.quantize(Decimal('1.00')))     #  округление до 2 цифр в дробной части
print(num.quantize(Decimal('1.0')))      #  округление до 1 цифр в дробной части


#####
from decimal import *

num = Decimal('-1.4568769017')
num_tuple = num.as_tuple()

print(num_tuple.sign)
print(num_tuple.digits)
print(num_tuple.exponent)


#####
from decimal import *

num = Decimal(0.1) + Decimal(0.1) + Decimal(0.1) - Decimal(0.3)

if num == 0:
    print('YES')
else:
    print('NO')

#####

from decimal import *

num = Decimal('0.1') + Decimal('0.1') + Decimal('0.1') - Decimal('0.3')

if num == 0:
    print('YES')
else:
    print('NO')


######

from decimal import *
s = '0.77 4.03 9.06 3.80 7.08 5.88 0.23 4.65 2.79 0.90 4.23 2.15 3.24 8.57 0.10 8.57 1.49 5.64 3.63 8.36 1.56 6.67 1.46 5.26 4.83 7.23 1.22 1.02 7.82 9.97 5.40 9.79 9.82 2.78 2.96 0.07 1.72 7.24 7.84 9.23 1.71 6.24 5.78 5.37 0.03 9.60 8.86 2.73 5.83 6.50'
slw = list(map(Decimal, s.split(" ")))
print(min(slw) + max(slw))

######

from decimal import Decimal as D
s = '9.73 8.84 8.92 9.60 9.32 8.97 8.53 1.26 6.62 9.85 1.85 1.80 0.83 6.75 9.74 9.11 9.14 5.03 5.03 1.34 3.52 8.09 7.89 8.24 8.23 5.22 0.30 2.59 1.25 6.24 2.14 7.54 5.72 2.75 2.32 2.69 9.32 8.11 4.53 0.80 0.08 9.36 5.22 4.08 3.86 5.56 1.43 8.36 6.29 5.13'
sn = [D(i) for i in s.split(" ")]
sorted_sn = sorted(sn, reverse = True)
print(sum(sorted_sn))
print(*sorted_sn[:5])

#####
from decimal import *
#num = Decimal(input())
num = sorted(input().replace(".","").replace("-","")) # работаем со строкой, сортируем, превращая ее в список

####
from decimal import *
n = Decimal(input())
print(n.exp() + n.ln() + n.log10() + n.sqrt())

######
from fractions import Fraction

num1 = Fraction(5, 10)
num2 = Fraction('75/100')
num3 = Fraction('0.25')

print(num1, num2, num3, sep='\n')

#####
from fractions import Fraction
num1 = Fraction('3/8')
num2 = Fraction('1/2')
print(num1 ** num2)


#####
from fractions import Fraction
import math

print('PI =', math.pi)

num = Fraction(str(math.pi))

print('No limit =', num)

for d in [1, 5,  50, 90, 100, 500, 1000000]:
    limited = num.limit_denominator(d)
    print(limited)


######
from fractions import *

num = Fraction(7, 71)

if num * 71 == 7:
    print('YES')
else:
    print('NO')


######
from fractions import Fraction

numbers = ['6.34', '4.08', '3.04', '7.49', '4.45', '5.39', '7.82', '2.76', '0.71', '1.97', '2.54', '3.67', '0.14', '4.29', '1.84', '4.07', '7.26', '9.37', '8.11', '4.30', '7.16', '2.46', '1.27', '0.29', '5.12', '4.02', '6.95', '1.62', '2.26', '0.45', '6.91', '7.39', '0.52', '1.88', '8.38', '0.75', '0.32', '4.81', '3.31', '4.63', '7.84', '2.25', '1.10', '3.35', '2.05', '7.87', '2.40', '1.20', '2.58', '2.46']
for num in numbers:
    print(f"{num} = {Fraction(num)}")


#####
from fractions import Fraction

s = '0.78 4.3 9.6 3.88 7.08 5.88 0.23 4.65 2.79 0.90 4.23 2.15 3.24 8.57 0.10 8.57 1.49 5.64 3.63 8.36 1.56 6.67 1.46 5.26 4.83 7.13 1.22 1.02 7.82 9.97 5.40 9.79 9.82 2.78 2.96 0.07 1.72 7.24 7.84 9.23 1.71 6.24 5.78 5.37 0.03 9.60 8.86 2.73 5.83 6.50 0.123 0.00021'

s_list = list(map(Fraction, s.split(" ")))
print(max(s_list) + min(s_list))


#####
from fractions import Fraction as F
print(F(int(input()), int(input())))

######
from fractions import Fraction as F
a = input()
b = input()
print(f"{a} + {b} = {F(a) + F(b)}")
print(f"{a} - {b} = {F(a) - F(b)}")
print(f"{a} * {b} = {F(a) * F(b)}")
print(f"{a} / {b} = {F(a) / F(b)}")

######
from fractions import Fraction as F
basel_series_size = int(input())
basel_series = [F(1, i * i) for i in range(1, basel_series_size + 1)]
# последовательность Базеля это серия обратных квадратов: 1/1, 1/4, 1/9, 1/25.. 1/n*n
print(sum(basel_series))

######
from fractions import Fraction as F
n = int(input())
s = 0
for i in range(1,n+1):
    s += F(1, i ** 2)
print(s)


######
from math import factorial
from fractions import Fraction as F
print(sum([F(1, factorial(i)) for i in range(1, int(input()) + 1)]))

######

from math import gcd
from fractions import Fraction as F
n, lst = int(input()), []
for i in range(1, n + 1):
    if gcd(i, n-i) == 1 and i < n-i:
        lst += [F(i, n-i)]
print(lst[-1])


#####

from math import gcd
from fractions import Fraction as F
n, lst = int(input()), []
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if gcd(i, j) == 1 and i != j and j > i:
            lst += [(F(i, j))]
print(*sorted(lst), sep = "\n")

#####
z1 = -3 + 2j              # создание на основе литерала
z2 = complex(6, -8)       # z2 = 6 - 8j
z3 = complex(0, 2.5)      # z3 = 2.5j
z4 = complex(5, 0)        # z4 = 5 + 0j
z5 = complex('3+4j')      # создание на основе строки

print(z1, z2, z3, z4, z5, sep='\n')


######
z1 = 5 + 7j
z2 = 1j
z3 = -3 + 5J
z4 = 1.5 + 3.2j

print(z1, z2, z3, z4, sep='\n')
print(type(z1))


######
