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
