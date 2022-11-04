languages = ['Chinese', 'Spanish', 'English', 'Hindi', 'Arabic', 'Bengali', 'Portuguese', 'Russian', 'Japanese', 'Lahnda']
print(languages[::-1])

#################
languages = ['Chinese', 'Spanish', 'English', 'Hindi', 'Arabic', 'Bengali', 'Portuguese', 'Russian', 'Japanese', 'Lahnda']

for i in range(0, len(languages) // 2):
    languages[i], languages[-(i + 1)] = languages[-(i + 1)], languages[i]

print(languages)


numbers1 = [1, 2, 3]
numbers2 = [6]
numbers3 = [7, 8, 9, 10, 11, 12, 13]

print(numbers1 * 2 + numbers2 * 9 + numbers3)



numbers = [2, 6, 3, 14, 10, 4, 11, 16, 12, 5, 4, 16, 1, 0, 8, 16, 10, 10, 8, 5, 1, 11, 10, 10, 12, 0, 0, 6, 14, 8, 2, 12, 14, 5, 6, 12, 1, 2, 10, 14, 9, 1, 15, 1, 2, 14, 16, 6, 7, 5]
print(len(numbers)) # Вывел длину списка;
print(numbers[-1]) #Вывел последний элемент списка;
print(numbers[::-1]) #Вывел список в обратном порядке (вспоминаем срезы);
if 15 in numbers and 17 in numbers:
    print("YES")
else:
    print("NO") #Вывел YES если список содержит числа 5 и 17, и NO в противном случае;
del numbers[0]
del numbers[-1]
print(numbers)#Вывел список с удаленным первым и последним элементами.



n, s = int(input()), []
for _ in range(n):
    s.append(input())
print(s)


n = int(input())
s = []
for i in range(1, n + 1):
  num = input()
  s += [num]
print(s)


list = []
for _ in range(int(input())):
    list.append(input())
print(list)


s = []
for i in range(26):
  s.append(chr(97 + i) * (i + 1))
print(s)


s = []
for _ in range(int(input()):
               x = int(input())
               s.append(x ** 3)
print(s)



s = []
for _ in range(int(input())):
  s.append(int(input()) ** 3)
print(s)


print([int(input()) ** 3 for _ in range(int(input()))])



n = int(input())
s = []
for i in range(1, n + 1):
    if n % i == 0:
        s.append(i)
print(s)


def list_of_dividers(number):
    list = []
    for i in range(1, number + 1):
        if number % i == 0:
            list.append(i)
    return list


print(list_of_dividers(int(input())))


n = int(input())
previous_x = int(input())
s = []
for i in range(1, n):
    x = int(input())
    s.append(x + previous_x)
    previous_x = x
print(s)


n = int(input())
s = []
while n > 0:
    s.append(int(input()))
    n -= 1
s1 = [s[i]+s[i+1] for i in range(len(s)-1)]

print(s1)




_range = int(input())
mylist = []
a, b = 0, int(input())
for i in range(1, _range):
    a, b = b, int(input())
    mylist.append(a + b)
print(mylist)




n = int(input())
l, s = [], []
for i in range(n):
    l.append(int(input()))
    if i > 0:
        s.append(l[i] + l[i - 1])
print(s)


n, s = int(input()), []
for i in range(n):
    s.append(int(input()))
print(s[::2])


n, s = int(input()), []
for i in range(n):
    s.append(int(input()))
del s[1::2]
print(s)

print([int(input()) for i in range(int(input()))][::2])



n = int(input())
s = []
for _ in range(n):
    s.append(input())
k = int(input())
for i in s:
    if len(i) >= k:  #игнорируем строки меньше чем k
        print(i[k-1], end = "") # забираем k-ый элемент строки i[k-1]



_list, k = [input() for _ in range(int(input()))], int(input())
for i in _list:
    if len(i) >= k:
        print(i[k-1], end='')


n = int(input())
s = []
for _ in range(n):
    s.extend(list(input()))
print(s)




numbers = [1, 78, 23, -65, 99, 9089, 34, -32, 0, -67, 1, 11, 111]
print(sum([i ** 2 for i in numbers]))

numbers = [1, 2]
summ = 0
for i in numbers:
    summ += i ** 2
print(summ)


numbers = [1, 78, 23, -65, 99, 9089, 34, -32, 0, -67, 1, 11, 111]

for i in range(len(numbers)):
	numbers[i] = numbers[i] ** 2

print(sum(numbers))



n, s, f = int(input()), [], []
for _ in range(n):
    x = int(input())
    s.append(x)
    f.append(x ** 2 + 2 * x + 1)
print(*s, sep = "\n")
print()
print(*f, sep = "\n")




#Обожаю генераторы!
#Meowmeow!


_list = [int(input()) for _ in range(int(input()))]
print(*_list, sep='\n', end='\n\n')
print(*[i**2+i*2+1 for i in _list], sep='\n')


n, s, min_index, max_index = int(input()), [], -1, -1
for i in range(n):
    s.append(int(input()))
for k in range(len(s)):
    if s[k] == min(s):
        min_index = k
del s[min_index]
for k in range(len(s)):
    if s[k] == max(s):
        max_index = k
del s[max_index]
print(*s, sep = "\n")


lst = [int(input()) for _ in range(int(input()))]
del lst[lst.index(max(lst))]
del lst[lst.index(min(lst))]
print(*lst, sep='\n')


n = int(input())
sp = []
for i in range(n):
    a = int(input())
    sp.append(a)
del sp[sp.index(max(sp))]
del sp[sp.index(min(sp))]
print(*sp, sep = '\n')


n = int(input())
sp = []
for i in range(n):
    a = int(input())
    sp.append(a)
del sp[sp.index(max(sp))]
del sp[sp.index(min(sp))]
print(*sp, sep = '\n')




s = [int(input()) for _ in range(int(input()))]
s = [int(input()) for _ in range(int(input()))]

s.remove(max(s)), s.remove(min(s))
print(*s, sep='\n')

n = int(input())
k = []
s = [input() for _ in range(n)]
for i in s:
    if i not in k:
        k.append(i)
print(*k, sep = "\n")

print(*{input(): 0 for _ in range(int(input()))}, sep='\n')



lst = [input() for _ in range(int(input()))]
s = input()
for c in lst:
    if s.lower() in c.lower():
        print(c)



a=int(input())
s=[]
g=[]
for i in range (a):
    b=input()
    s.append(b)
k=input()
k=k.lower()
for j in s:
    if k in j.lower():
        g.append(j)
print(*g, sep=("\n"))


s = [input() for _ in range(int(input()))]
word = input()
for i in s:
    if word.lower() in i.lower(): print(i)



s = [input() for _ in range(int(input()))]
search = [input() for _ in range(int(input()))]
result = []
for i in s:
    flag = 1
    for j in search:
        if j.lower() not in i.lower():
            flag = 0
    if flag == 1:
        print(i)

google, search = [], []  # Создаём списки выражений и запросов
count = 0  # Создаём счётчик
for _ in range(int(input())):  # Считываем количество выражений
    google.append(input())  # Считываем выражения
for _ in range(int(input())):  # Считываем количество запросов
    search.append(input())  # Считываем запросы

for i in google:  # Начинаем новый цикл (проходимся по выражениям)
    for j in search:  # Вложенный цикл (проходимся по запросам)
        if j.lower() in i.lower():  # Если запрос присутствует в выражении
            count += 1  # К счётчику добавляем единицу
            if count == len(search):  # Если количество запросов равно количеству совпадений:
                print(i)  # Печатаем выражение по этому индексу
    count = 0  # Счётчик обнуляем



ss = [input() for _ in range(int(input()))]
reqs = [input().lower() for _ in range(int(input()))]
print(*[s for s in ss if all(req in s.lower() for req in reqs)], sep='\n')


lst = [input() for _ in range(int(input()))]
qwe = [input() for _ in range(int(input()))]
for c in lst:
    flag = True
    for s in qwe:
        if s.lower() not in c.lower():
            flag = False
    if flag:
        print(c)


s1 = [input() for _ in range(int(input()))]
s2 = [input() for _ in range(int(input()))]
for i in range(len(s1)-1, -1, -1):
    k = True
    for j in s2:
        if j.lower() not in s1[i].lower(): k = False
    if k == False: s1.remove(s1[i])

print(*s1, sep='\n')



s = [int(input()) for _ in range(int(input()))]
for i in s:
    if i < 0:
        print(i)
for i in s:
    if i == 0:
        print(i)
for i in s:
    if i > 0:
        print(i)


n = int(input())
Negatives = []
Zeros = []
Positives = []
for i in range(n):
    a = int(input())
    if a<0:
        Negatives.append(a)
    elif a==0:
        Zeros.append(a)
    elif a>0:
        Positives.append(a)
print(*Negatives, sep='\n')
print(*Zeros, sep='\n')
print(*Positives, sep='\n')
