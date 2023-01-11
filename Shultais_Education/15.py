a, b = int(input()), int(input())
print(a+b, a-b, a*b, a/b, a//b, a%b, (a**10 + b**10)**0.5, sep = "\n")


print(len(input().split()))


symbols = ["Обезьяна", "Петух", "Собака", "Свинья", "Крыса", "Бык", "Тигр", "Заяц", "Дракон", "Змея", "Лошадь", "Овца"]
print(symbols[int(input()) % 12])


num = input()
if len(num) == 6:
    num2 = num[5:0:-1]
    print(int(num[0] + num2))
else:
    print(int(num[::-1]))


s = input()
print(int(s[:-5] + s[-5:][::-1]))



x = int(input())
print('{0:,}'.format(x))



num = int(input())
print(f'{num:,}')



x = int(input())
print('{0:,}'.format(x)) # {0:,} - указываем запятую в качестве разделителя разрядов



from random import *

answer = ["Бесспорно", "Предрешено", "Никаких сомнений", "Определённо да", "Можешь быть уверен в этом", "Мне кажется - да",
     "Вероятнее всего", "Хорошие перспективы", "Знаки говорят - да", "Да", "Пока неясно, попробуй снова",
     "Спроси позже",
     "Лучше не рассказывать", "Сейчас нельзя предсказать", "Сконцентрируйся и спроси опять", "Даже не думай",
     "Мой ответ - нет", "По моим данным - нет", "Перспективы не очень хорошие", "Весьма сомнительно"]
while True:
    b = input('Спрашивай что хочешь? ')
    print('!!!', choice(answer), '!!!')
    print()
    if int(input('Если у тебя ещё есть вопрос нажми "1" если нет нажми "0" ')):
        continue
    else:
        print('!!! Ну,ты если че заходи !!!')
        break



n, k = int(input()), int(input())
a = 0
for i in range(1, n + 1):
    a = (a + k) % i
print(a +1)



c1, c2, c3, c4 = 0,0,0,0
for i in range(int(input())):
               x, y = list(map(int, input().split()))
               if (x > 0 and y > 0):
                   c1 += 1
               elif (x < 0 and y > 0):
                    c2 += 1
               elif (x < 0 and y < 0):
                    c3 += 1
               elif (x > 0 and y < 0):
                    c4 += 1
print(f"Первая четверть: {c1}")
print(f"Вторая четверть: {c2}")
print(f"Третья четверть: {c3}")
print(f"Четвертая четверть: {c4}")





numbers = [int(n) for n in input().split()]
counter = 0

for i in range(1, len(numbers)):
    if numbers[i] > numbers[i - 1]:
        counter += 1

print(counter)



num_list = list(map(int, input().split()))
counter, counter_max, previous_num = 0, 0, num_list[0]
for i in num_list[1:]:
    if i > previous_num:
        counter += 1
        if counter > counter_max:
            counter_max = counter
    previous_num = i
print(counter_max)


s_list = [int(i) for i in input().split()]
for k in range(0, len(s_list) - 1, 2):
    s_list[k], s_list[k + 1] =  s_list[k + 1], s_list[k]
print(*s_list, sep = " ")



sp = [i for i in input().split()]
last = sp.pop()
sp.insert(0, last)
print(*sp)

print(len(set(input().split()))) # формируем список, спомощью метода SET делаем уникальным (убираем повторы), LEN - возвращает длину



n = int(input())
sp = [int(input()) for i in range(n)]
num = int(input())
flag = "НЕТ"
for i in range(len(sp)):
    for j in range(i + 1, len(sp)):
        if sp[i] * sp[j] == num:
            flag = "ДА"
print(flag)



# выяснить, является ли заданное число произведением двух любых чисел из списка
n=int(input())
spis=[int(input()) for _ in range(n)]
number=int(input())

temp=[[spis[i]*spis[j] for j in range(i+1,len(spis))] for i in range(len(spis)-1)] # создали набор списков,
# содержащих произведение элементов между собой
mass=list(set([j for i in temp for j in i])) #распаковали эти списки внутри набора и из этого набора
# взяли только те элементы, что не повторяются

print('ДА' if number in mass else 'НЕТ')


timur_input, ruslan_input  = input(), input()
def game(a, b):
    if (a == 'камень' and b == "ножницы") or (a == 'ножницы' and b == "бумага") or (a == 'бумага' and b == "камень"):
        return "Тимур"
    elif (b == 'камень' and a == "ножницы") or (b == 'ножницы' and a == "бумага") or (b == 'бумага' and a == "камень"):
        return "Руслан"
    else:
        return "ничья"
print(game(timur_input, ruslan_input))



x, y = input(), input()
var = ['камень', 'ножницы', 'бумага']
ans = ['ничья', 'Руслан', 'Тимур', 'Руслан', 'Тимур']
print(ans[var.index(x) - var.index(y)])



x, y = input(), input()
var = ['камень', 'ножницы', 'бумага']
ans = ['ничья', 'Руслан', 'Тимур', 'Руслан', 'Тимур']
print(ans[var.index(x) - var.index(y)])


x, y = input(), input()
var = ['камень', 'ножницы', 'бумага']
ans = ['ничья', 'Руслан', 'Тимур', 'Руслан', 'Тимур']
print(ans[var.index(x) - var.index(y)])


s = input()
counter, counter_max = 0, 0
for i in s:
    if i == "Р":
        counter += 1
        if counter > counter_max:
            counter_max = counter
    else:
        counter = 0
print(counter_max)


print(len(max(input().split("О"), key=len)))


import re
pattern = "anton"
result = [i+1 for i in range(int(input())) if re.findall(r'\w*a\w*n\w*t\w*o\w*n\w*', input())]
print(*result)



numbers = [-6, -8, 0, 1, 3, 8, -7, 12, 17, 24, 25, 3, 5, 1]
res = 0
for num in numbers:
    res += (num % 2 == 1) and (num > 1)
print(res)


print(bool('abc'))


print(bool(list(range(10))))


# объявление функции
def func(num1, num2):
    return num1 % num2 == 0

# считываем данные
num1, num2 = int(input()), int(input())

# вызываем функцию
if func(num1, num2):
    print("делится")
else:
    print("не делится")



# объявление функции
def func(num1, num2):
    return num1 % num2 == 0

# считываем данные
num1, num2 = int(input()), int(input())

# вызываем функцию
if func(num1, num2):
    print("делится")
else:
    print("не делится")



numbers = [10, 20, 30, 40, 50, 60, 70, 80]
print(numbers[2:5])
print(numbers[:4])
print(numbers[3:])
