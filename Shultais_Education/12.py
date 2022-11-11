print(*[i[0]+"." for i in input().split()], sep="")

print("\n".join(input().split('\\'))) # не забываем, что одна \ это символ экранирования



print(*input().split(chr(92)), sep='\n')


s_list = input().split()
for i in s_list:
    print("+" * int(i))


print(*[int(char) * '+' for char in input().split()], sep='\n')


#####################
lst = map(int, input().split())  # такая нехитрая запись позволяет делать список из чисел, а не строк
print(*['+' * i for i in lst], sep='\n')
#####################


s_list = map(int, input().split("."))
for i in s_list:
    if i < 0 or i > 255:
        print("НЕТ")
        break
else:
    print("ДА")

for b in listig:
    if int(b) > 255:
        flag = False
if flag == True:
    print('ДА')
else:
    print('НЕТ')


text = input()
List = text.split('.')

for i in List:
    flag = False
    if 0 <= int(i) <= 255:
        flag = True
    else:
        break
if flag:
    print('ДА')
else:
    print('НЕТ')


s = input()
a = s.split('.')
flag = 'ДА'
for i in a:
    if not 0 <= int(i) <=255:
        flag = 'НЕТ'
        break
print(flag)


s = input().split('.')
for i in s:
    if int(i) > 255:
        print('НЕТ')
        break
else:
    print('ДА')


print(('НЕТ', 'ДА')[sum([int(n)<256 for n in input().split('.')]) == 4])


ip = input().split('.')
for i in ip:
    if int(i) not in range(0, 256):
        print('НЕТ')
        break
else:
    print('ДА')


s_list = list(input())
razdelitel = input()
print(razdelitel.join(s_list))


text, sep = input(), input()
List = sep.join(text).split()
print(*List)


s, c = list(input()), input()
print(c.join(s))


s = input()
print(input().join(s))


print(*[input().join(i) for i in input().split('.')], end=' ')



s_list = list(map(int, input().split()))
counter, t = 0, 0
for i in s_list[t:]:
    for j in s_list[t + 1:]:
        if i == j:
            counter += 1
    t += 1
print(counter)


m, counter = input().split(), 0
for i in range(len(m)):
    for j in range(i + 1, len(m)):
        if m[i] == m[j]:
            counter += 1
print(counter)


a = input().split()
s = 0
for i in range(len(a) - 1):
    s += a[i + 1:].count(a[i])
print(s)

s = input()
spisok = s.split(' ')
counter = 0
for i in spisok:
    spisok = spisok[1:]
    for j in spisok:
        if i == j:
            counter += 1

print(counter)




colors = ['Orange']
colors.append('Red')
colors.append('Blue')
colors.append('Green')
colors.insert(0, 'Violet')
colors.insert(2, 'Purple')

print(colors)



numbers = [8, 9, 10, 11]
numbers[1] = 17 #    Заменил второй элемент списка на 17;
numbers.extend([4, 6, 7]) #    Добавил числа 4, 5 и 6 в конец списка;
del numbers[0]#    Удалил первый элемент списка;
numbers *= 2 #    Удвоил список;
numbers.insert(3, 25)#    Вставил число 25 по индексу 3;
print(numbers) #    Вывел список, с помощью функции print()



numbers = [8, 9, 10, 11]
numbers[1] = 17 #    Заменил второй элемент списка на 17;
numbers.extend([4, 5, 6]) #    Добавил числа 4, 5 и 6 в конец списка;
del numbers[0]#    Удалил первый элемент списка;
numbers *= 2 #    Удвоил список;
numbers.insert(3, 25)#    Вставил число 25 по индексу 3;
print(numbers) #    Вывел список, с помощью функции print()


s_list = list(map(int, input().split()))
position_max= s_list.index(max(s_list))
position_min= s_list.index(min(s_list))
s_list[position_max], s_list[position_min] = s_list[position_min], s_list[position_max]
s_list = list(map(str, s_list))
print(" ".join(s_list))



m, l = input().split(), []
for i in m:
    l.append(int(i))
m_min, m_max = min(l), max(l)
m_min_i, m_max_i = l.index(min(l)), l.index(max(l))
l[m_min_i], l[m_max_i] = m_max, m_min
print(*l, sep=' ')

x = input().split()
int_x = [int(x) for x in x]  # преобразование в целое число

ma = max(int_x)
mi = min(int_x)

for i in range(len(int_x)):
    if int_x[i] == ma:
        int_x[i] = mi
    elif int_x[i] == mi:
        int_x[i] = ma

print(*int_x)



s = input().split()
s = [int(i) for i in s]
index_max = s.index(max(s))
index_min = s.index(min(s))
s[index_max], s[index_min] = s[index_min], s[index_max]
print(*s)



nums = [int(c) for c in input().split()]
max_i, min_i = nums.index(max(nums)), nums.index(min(nums))
nums[max_i], nums[min_i] = min(nums), max(nums)
print(*nums)
