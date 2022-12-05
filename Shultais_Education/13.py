def f_min(self, start, end):
    minim = self[start]
    min_idx = start
    for idx in range(start, end):
        if self[idx] < minim:
            minim = self[idx]
            min_idx = idx
    return min_idx

def select_sort(self):
    i = 0
    arr_size  = len(self)
    while i < arr_size:
        min_idx = f_min(self, i, arr_size)
        self[min_idx], self[i] = self[i], self[min_idx]
        i += 1
    return self

a = [78, -32, 5, 39, 58, -5, -63, 57, 72, 9, 53, -1, 63, -97, -21, -94, -47, 57, -8, 60, -23, -72, -22, -79, 90, 96, -41, -71, -48, 84, 89, -96, 41, -16, 94, -60, -64, -39, 60, -14, -62, -19, -3, 32, 98, 14, 43, 3, -56, 71, -71, -67, 80, 27, 92, 92, -64, 0, -77, 2, -26, 41, 3, -31, 48, 39, 20, -30, 35, 32, -58, 2, 63, 64, 66, 62, 82, -62, 9, -52, 35, -61, 87, 78, 93, -42, 87, -72, -10, -36, 61, -16, 59, 59, 22, -24, -67, 76, -94, 59]

print(select_sort(a))



# объявление функции
def draw_box():
    print("*" * 10)
    for i in range(12):
        print("*        *")
    print("*" * 10)

# основная программа
draw_box()  # вызов функции



# объявление функции
def draw_triangle():
    for i in range(10):
        print("*" * (i+1))

# основная программа
draw_triangle()  # вызов функции



def draw_box(height, width):
    height = 2
    width = 10
    for i in range(height):
        print('*' * width)

n = 5
m = 7
draw_box(n, m)
print(n, m)



# объявление функции
def draw_triangle(fill, base):
    for i in range(1, int(base / 2) +2):
        print(fill * i)
    for i in range(int(base / 2), 0, -1):
        print(fill * i)
# считываем данные
fill = input()
base = int(input())

# вызываем функцию
draw_triangle(fill, base)



# объявление функции
def print_fio(name, surname, patronymic):
    print(surname[0].upper(), name[0].upper(), patronymic[0].upper(), sep = "")

# считываем данные
name, surname, patronymic = input(), input(), input()

# вызываем функцию
print_fio(name, surname, patronymic)


# объявление функции
def print_digit_sum(num):
    sum = 0
    for i in list(str(num)):
        sum += int(i)
    print(sum)

# считываем данные
n = int(input())

# вызываем функцию
print_digit_sum(n)



def print_digit_sum(num):
    print(sum(int(i) for i in num))
n = input()
print_digit_sum(n)


def print_paris():
    print(s)
    s = 'I love Paris'

print_paris()






number = 101

def is_prime(num):
    flag = True
    for i in range(2, num):
        if num % i == 0:
            flag = False
            break
    if num != 1 and flag == True:
        print('Число', num, 'простое.')
    else:
        print('Число', num, 'составное.')


x = 17
y = int(input())
is_prime(x)
is_prime(y)
is_prime(number)



x = 5

def add():
    global x
    x = 3
    x = x + 5
    print(x)

add()
print(x)



def compute_hypotenuse(a, b):
    c = (a ** 2 + b ** 2) ** 0.5
    return c


def compute_average(numbers):
    return sum(numbers) / len(numbers)



def convert_to_miles(km):
    return km * 0.6214
num = int(input())
print(convert_to_miles(num))


def get_days(month):
    if month in [1,3,5,7,8,10,12]:
        return "31"
    elif month == 2:
        return "28"
    else:
        return "30"
num = int(input())
print(get_days(num))

# объявление функции
def get_factors(num):
    s = []
    for i in range(1, num + 1):
        if num % i == 0:
            s += [i]
    return s

# считываем данные
n = int(input())

# вызываем функцию
print(get_factors(n))


# объявление функции
def get_factors(num):
    return [i for i in range(1, num+1) if num % i == 0]

# считываем данные
n = int(input())

# вызываем функцию
print(get_factors(n))



def number_of_factors(num):
    return len([i for i in range(1, num + 1) if num % i == 0])
print(number_of_factors(int(input())))




# объявление функции
def number_of_factors(num):
    return len([i for i in range(1, num+1) if not (num % i)])

# считываем данные
n = int(input())

# вызываем функцию
print(number_of_factors(n))


# объявление функции
def get_factors(num):
    return [x for x in range(1, num + 1) if num % x == 0]


def number_of_factors(num):
    return len(get_factors(num))


# считываем данные
n = int(input())

# вызываем функцию
print(number_of_factors(n))



# объявление функции
def find_all(target, symbol):
    l = []
    for i in range(len(target)):
        if target[i] == symbol:
            l.append(i)
    return l
# считываем данные
s = input()
char = input()

# вызываем функцию
print(find_all(s, char))


# объявление функции
def merge(list1, list2):
    return sorted(list1 + list2, key = int)

# считываем данные
numbers1 = [int(c) for c in input().split()]
numbers2 = [int(c) for c in input().split()]

# вызываем функцию
print(merge(numbers1, numbers2))



n = int(input())
s = []
for i in range(n):
    s += list(map(int, input().split()))
s.sort()
print(*s, sep = " ")



# put your python code here
def quick_merge(list1, list2):
    result = []
    p1 = 0  # указатель на первый элемент списка list1
    p2 = 0  # указатель на первый элемент списка list2

    while p1 < len(list1) and p2 < len(list2):  # пока не закончился хотя бы один список
        if list1[p1] <= list2[p2]:
            result.append(list1[p1])
            p1 += 1
        else:
            result.append(list2[p2])
            p2 += 1

    if p1 < len(list1):   # прицепление остатка
        result += list1[p1:]
    if p2 < len(list2):
        result += list2[p2:]
    return result
n = int(input())
list1 = [int(c) for c in input().split()]
while n - 1 != 0:
    list2 = [int(c) for c in input().split()]
    list1 = quick_merge(list1, list2)
    n -= 1
print(*list1)


# put your python code here
arr =[];[arr.extend([int(c) for c in input().split()])  for i in range(int(input()))]; arr.sort(); print(*arr)


# объявление функции
def is_valid_triangle(side1, side2, side3):
    if side1 < side2 + side3 and side2 < side1 + side3 and side3 < side2 + side2:
        return True
    else:
        return False


# считываем данные
a, b, c = int(input()), int(input()), int(input())

# вызываем функцию
print(is_valid_triangle(a, b, c))
