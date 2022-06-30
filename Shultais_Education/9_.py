'''Нечетные числа

Заполните список numbers нечетными числами от 11 до 27 включительно. Используйте цикл while.
 '''

numbers = []
j = 11
while j <=27:
    if j % 2 == 1:
        numbers.append(j)
    j += 1
print(numbers)





