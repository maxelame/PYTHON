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


count = 0
for i in input().split():
    if i == 'a' or i == 'A' or i == 'an' or i == 'An' or i == 'the' or i == 'The':
        count += 1
print(f"Общее количество артиклей: {count}")


s = input().lower().split()
k = ['a', 'an', 'the']
count = 0
for a in k:
  count += s.count(a)
print('Общее количество артиклей:', count)


print('Общее количество артиклей:',len([word for word in input().lower().split() if word in ['a', 'an', 'the']]))



n = int(input()[1:])
s_list = [input() for i in range(n)]
l = []
for t in s_list:
    if "#" in t:
        l.append(t.split("#")[0].rstrip())
    else:
        l.append(t.rstrip())
print(*l, sep = "\n")



print(*map(lambda i: i.split('#')[0].rstrip(), __import__('sys').stdin.read().splitlines()[1:]), sep='\n')



n = input()
for _ in range(int(n[1:])):
    s = input()
    if '#' in s:
        s = s[:s.find('#')]
    print(s.rstrip())



s_list = list(map(int, input().split()))
s_list.sort()
print(*s_list, sep = " ")
s_list.sort(reverse = True)
print(*s_list, sep = " ")



keywords = ['False', 'True', 'None', 'and', 'with', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'try', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'while', 'yield']
new_keywords = [s[1:] for s in keywords]
print(new_keywords)


keywords = ['False', 'True', 'None', 'and', 'with', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'try', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'while', 'yield']

lengths = [len(s) for s in keywords]

print(lengths)




keywords = ['False', 'True', 'None', 'and', 'with', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'try', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'while', 'yield']
new_keywords = [s for s in keywords if len(s) >= 5]
print(new_keywords)


palindromes = [i for i in range(100, 1000) if str(i) == str(i)[::-1]]
print(palindromes)

n = int(input())
s_list = [i ** 2 for i in range(1, n + 1)]
print(*s_list, sep = "\n")


ist_square = [i**2 for i in range(1, int(input()) + 1)]
for b in list_square:
    print(b)


print(*[int(i) ** 3 for i in input().split()])

n = input().split()
list = [print(int(n[i])**3, end =' ') for i in range(len(n))]



print(*input().split(), sep = "\n")



digit = [i for i in list(input()) if i in '0123456789']
print(*digit, sep = '')


print(*[i[k] for i in input().split() for k in range(len(i)) if i[k].isdigit() == True], sep='')



[print(d, end='') for d in input() if d.isdigit()]


print(*[int(i) ** 2 for i in input().split() if int(i) % 2 == 0 and (int(i) ** 2) % 10 != 4])



print(*list(filter(lambda x: x % 10 != 4, [int(i)**2 for i in input().split() if int(i) % 2 == 0])))



a = [17, 24, 91, 96, 67, -27, 79, -71, -71, 58, 48, 88, 88, -16, -78, 96, -76, 56, 92, 1, 32, -17, 36, 88, -61, -97, -37, -84, 50, 47, 94, -6, 52, -76, 93, 14, -32, 98, -65, -16, -9, -68, -20, -40, -71, 93, -91, 44, 25, 79, 97, 0, -94, 7, -47, -96, -55, -58, -78, -78, -79, 75, 44, -56, -41, 38, 16, 70, 17, -17, -24, -83, -74, -73, 11, -26, 63, -75, -19, -13, -51, -74, 21, -8, 21, -68, -66, -84, -95, 78, 69, -29, 39, 38, -55, 7, -11, -26, -62, -84]

n = len(a)

for i in range(n - 1):
    for j in range(n - i - 1):
        if a[j] > a[j + 1]:
            a[j], a[j + 1] = a[j + 1], a[j]

print(a)



a = [17, 24, 91, 96, 67, -27, 79, -71, -71, 58, 48, 88, 88, -16, -78, 96, -76, 56, 92, 1, 32, -17, 36, 88, -61, -97, -37, -84, 50, 47, 94, -6, 52, -76, 93, 14, -32, 98, -65, -16, -9, -68, -20, -40, -71, 93, -91, 44, 25, 79, 97, 0, -94, 7, -47, -96, -55, -58, -78, -78, -79, 75, 44, -56, -41, 38, 16, 70, 17, -17, -24, -83, -74, -73, 11, -26, 63, -75, -19, -13, -51, -74, 21, -8, 21, -68, -66, -84, -95, 78, 69, -29, 39, 38, -55, 7, -11, -26, -62, -84]
flag = False
n = len(a)

for i in range(n - 1):
    for j in range(n - i - 1):
        if a[j] > a[j + 1]:
            a[j], a[j + 1] = a[j + 1], a[j]
            flag = True
    if flag == False:
        break

print(a)


a = [17, 24, 91, 96, 67, -27, 79, -71, -71, 58, 48, 88, 88, -16, -78, 96, -76, 56, 92, 1, 32, -17, 36, 88, -61, -97, -37, -84, 50, 47, 94, -6, 52, -76, 93, 14, -32, 98, -65, -16, -9, -68, -20, -40, -71, 93, -91, 44, 25, 79, 97, 0, -94, 7, -47, -96, -55, -58, -78, -78, -79, 75, 44, -56, -41, 38, 16, 70, 17, -17, -24, -83, -74, -73, 11, -26, 63, -75, -19, -13, -51, -74, 21, -8, 21, -68, -66, -84, -95, 78, 69, -29, 39, 38, -55, 7, -11, -26, -62, -84]

s, b = len(a), []

while s != 0:
    b.append(min(a))
    a.remove(b[-1])
    s -=1
print(b)

a = [17, 24, 91, 96, 67, -27, 79, -71, -71, 58, 48, 88, 88, -16, -78, 96, -76, 56, 92, 1, 32, -17, 36, 88, -61, -97,
     -37, -84, 50, 47, 94, -6, 52, -76, 93, 14, -32, 98, -65, -16, -9, -68, -20, -40, -71, 93, -91, 44, 25, 79, 97, 0,
     -94, 7, -47, -96, -55, -58, -78, -78, -79, 75, 44, -56, -41, 38, 16, 70, 17, -17, -24, -83, -74, -73, 11, -26, 63,
     -75, -19, -13, -51, -74, 21, -8, 21, -68, -66, -84, -95, 78, 69, -29, 39, 38, -55, 7, -11, -26, -62, -84]

n = len(a)
swap = True  # задаём сигнальную метку

for i in range(n - 1):

    if swap == False:  # если по окончании внешнего цикла сигнальная метка приняла значение False, т.е. ни одного обмена не было произведено, тогда программа прерывается
        break

    for j in range(n - i - 1):
        if a[j] > a[j + 1]:
            a[j], a[j + 1] = a[j + 1], a[j]

            swap = True  # если в данном внутреннем цикле была произведена хотя бы одна перестановка во внутреннем цикле, сигнальная метка принимает значение True
        else:
            False  # если в данном внутреннем цикле не было произведено ни одной перестановки, сигнальная метка сохраняет значение False

print(a)




a = [78, -32, 5, 39, 58, -5, -63, 57, 72, 9, 53, -1, 63, -97, -21, -94, -47, 57, -8, 60, -23, -72, -22, -79, 90, 96, -41, -71, -48, 84, 89, -96, 41, -16, 94, -60, -64, -39, 60, -14, -62, -19, -3, 32, 98, 14, 43, 3, -56, 71, -71, -67, 80, 27, 92, 92, -64, 0, -77, 2, -26, 41, 3, -31, 48, 39, 20, -30, 35, 32, -58, 2, 63, 64, 66, 62, 82, -62, 9, -52, 35, -61, 87, 78, 93, -42, 87, -72, -10, -36, 61, -16, 59, 59, 22, -24, -67, 76, -94, 59]

n = len(a)

for i in range(n):
    k = min(a[:n])
    a.append(k)
    a.remove(k)
    n -= 1

print(a)



a = [78, -32, 5, 39, 58, -5, -63, 57, 72, 9, 53, -1, 63, -97, -21, -94, -47, 57, -8, 60, -23, -72, -22, -79, 90, 96, -41, -71, -48, 84, 89, -96, 41, -16, 94, -60, -64, -39, 60, -14, -62, -19, -3, 32, 98, 14, 43, 3, -56, 71, -71, -67, 80, 27, 92, 92, -64, 0, -77, 2, -26, 41, 3, -31, 48, 39, 20, -30, 35, 32, -58, 2, 63, 64, 66, 62, 82, -62, 9, -52, 35, -61, 87, 78, 93, -42, 87, -72, -10, -36, 61, -16, 59, 59, 22, -24, -67, 76, -94, 59]

# реализация алгоритма сортировки выбором

print([a.pop(a.index(min(a))) for i in range(len(a))])


a = [78, -32, 5, 39, 58, -5, -63, 57, 72, 9, 53, -1, 63, -97, -21, -94, -47, 57, -8, 60, -23, -72, -22, -79, 90, 96, -41, -71, -48, 84, 89, -96, 41, -16, 94, -60, -64, -39, 60, -14, -62, -19, -3, 32, 98, 14, 43, 3, -56, 71, -71, -67, 80, 27, 92, 92, -64, 0, -77, 2, -26, 41, 3, -31, 48, 39, 20, -30, 35, 32, -58, 2, 63, 64, 66, 62, 82, -62, 9, -52, 35, -61, 87, 78, 93, -42, 87, -72, -10, -36, 61, -16, 59, 59, 22, -24, -67, 76, -94, 59]

n = len(a)

for i in range(n - 1):
    max_i = a.index(max(a[: n - i]))
    a[max_i], a[n - i - 1] = a[n - i - 1], a[max_i]

print(a)
