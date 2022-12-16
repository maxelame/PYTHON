# объявление функции
def is_prime(num):
    counter = 0
    for i in range(1, num + 1):
        if num % i == 0:
            counter += 1
    if counter > 2 or num == 1:
        return False
    else:
        return True

# считываем данные
n = int(input())

# вызываем функцию
print(is_prime(n))



# объявление функции
def is_prime(num):
    return len([i for i in range(1, num+1) if num % i == 0]) == 2

# считываем данные
n = int(input())

# вызываем функцию
print(is_prime(n))




def is_prime(num):
    counter = 0
    for i in range(1, num + 1):
        if num % i == 0:
            counter += 1
    if counter > 2 or num == 1:
        return False
    else:
        return True


def get_next_prime(num):
    if is_prime(num):
        num += 1
    while not is_prime(num):
        num += 1
    return num


# считываем данные
n = int(input())

# вызываем функцию
print(get_next_prime(n))


# объявление функции
def is_password_good(password):
    if len(password) > 7 and not password.isupper() and not password.islower() and password.isalnum() and not password.isdigit() and not password.isalpha():
        return True
    else:
        return False


# считываем данные
txt = input()

# вызываем функцию
print(is_password_good(txt))






# объявление функции
def is_one_away(word1, word2):
    if len(word1) == len(word2):
        counter = 0
        for i in range(len(word1)):
            if word1[i] != word2[i]:
                counter += 1
        if counter == 1:
            return True
        else:
            return False
    else:
        return False
# считываем данные
txt1 = input()
txt2 = input()
# вызываем функцию
print(is_one_away(txt1, txt2))





# объявление функции
def is_palindrome(text):
    s_list = list(text.lower())
    new_list = []
    for i in s_list:
        if i.isalpha():
            new_list.append(i)
    print(new_list)
    s = "".join(new_list)
    print(s)
    if s == s[::-1]:
        return True
    else:
        return False


# считываем данные
txt = "Standart - smallest, sell Amstrad nats."

# вызываем функцию
print(is_palindrome(txt))




User avatar
Комментарий закреплён
Тимур 👨‍🏫 Гуев
3 года назад

Сначала удаляем ненужные символы, затем строим срез, переворачивающий строку и проверяем на равенство:
Верное решение #191449702
Python 3

# объявление функции
def is_palindrome(text):
    symbols = [' ', ',', '.', '!', '?', '-']
    for c in symbols:
        text = text.replace(c, '')
    text = text.lower()
    return text == text[::-1]

# считываем данные
txt = input()

# вызываем функцию
print(is_palindrome(txt))




# объявление функции
def is_correct_bracket(text):
    while text.count("()") > 0:
        text = text.replace("()","")
    if len(text) != 0:
        return False
    else:
        return True
# считываем данные
txt = input()

# вызываем функцию
print(is_correct_bracket(txt))

# объявление функции
def is_valid_password(password):
    s = password.split(":")
    flag1, flag2, flag3, flag4 = 0, 0, 0, 0
    if len(s) == 3:
        flag1 = 1  # проидена проверка на наличие 3х чисел
    if s[0] == s[0][::-1]:
        flag2 = 1  # проидена проверка палиндром
    counter = 0
    for i in range(1, int(s[1]) + 1):
        if int(s[1]) % i == 0:
            counter += 1
    if counter == 2:
        flag3 = 1  # проидена проверка на простое число

    if int(s[2]) % 2 == 0:
        flag4 = 1  # проидена проверка на четность

    if flag1 * flag2 * flag3 * flag4 == 1:
        return True
    else:
        return False


# считываем данные
psw = input()

# вызываем функцию
print(is_valid_password(psw))



# объявление функции
def is_valid_password(password):
    pas = [int(i) for i in password.split(':')]
    a, b = str(pas[0]), len([i for i in range(1, pas[1] + 1) if pas[1] % i == 0])
    return a == a[::-1] and b == 2 and pas[2] % 2 == 0 and len(pas) == 3

# считываем данные
psw = input()

# вызываем функцию
print(is_valid_password(psw))


# объявление функции
def is_correct_bracket(text):
    while "()" in text:
        text = text.replace("()", "")
    if text == "":
        return True
    return False


# считываем данные
txt = input()

# вызываем функцию
print(is_correct_bracket(txt))




def convert_to_python_case(text):
    s = list(text)
    string = s[0].lower()
    for i in s[1:]:
        if i.isupper():
            string += "_" + i.lower()
        else:
            string += i
    return string
# считываем данные
txt = input()

# вызываем функцию
print(convert_to_python_case(txt))



# объявление функции
def get_middle_point(x1, y1, x2, y2):
    return (x1 + x2)/2, (y1 + y2)/ 2

# считываем данные
x_1, y_1 = int(input()), int(input())
x_2, y_2 = int(input()), int(input())

# вызываем функцию
x, y = get_middle_point(x_1, y_1, x_2, y_2)
print(x, y)


# объявление функции
def get_middle_point(x1, y1, x2, y2):
    return (x1 + x2)/2, (y1 + y2)/ 2

# считываем данные
x_1, y_1 = int(input()), int(input())
x_2, y_2 = int(input()), int(input())

# вызываем функцию
x, y = get_middle_point(x_1, y_1, x_2, y_2)
print(x, y)

import math
def get_circle(radius):
    return 2*math.pi*radius, math.pi*radius**2

# считываем данные
r = float(input())

# вызываем функцию
length, square = get_circle(r)
print(length, square)




# объявление функции
def get_circle(radius):
    pi = __import__('math').pi
    return 2 * pi * radius, pi * radius ** 2

# считываем данные
r = float(input())

# вызываем функцию
length, square = get_circle(r)
print(length, square)



def get_circle(radius):
    from math import pi
    c = 2 * pi * radius
    s = pi * radius ** 2
    return (c, s)

r = float(input())
length, square = get_circle(r)
print(length, square)





from math import *
def solve(a, b, c):
    D = b ** 2 - 4*a*c
    if D < 0:
        return ("Нет корней")
    elif D == 0:
        return -b/(2*a), -b/(2*a)
    else:
        x1 = (-b-sqrt(D))/(2*a)
        x2 = (-b+sqrt(D))/(2*a)
        return min(x1, x2), max(x1,x2)

# считываем данные
a, b, c = int(input()), int(input()), int(input())

# вызываем функцию
x1, x2 = solve(a, b, c)
print(x1, x2)
