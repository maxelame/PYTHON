s, count = input(), 0
for i in s:
    if i.islower(): # метод строк islower() проверяет в нижнем ли регистре буква, isupper() - в верхнем
        count += 1
print(count)

x = input()
counter_lower = 0
for char in x:
    if char != char.upper():
        counter_lower += 1
print(counter_lower)


s, cnt = input(), 0
for char in s:
    if char != char.upper():
        cnt += 1
print(cnt)


print(len(input().split()))


s = input()
print(s.count(" ") + 1)


g_code, count_A, count_G, count_C, count_T = input(), 0, 0, 0, 0
count_A = g_code.count("А") + g_code.count("а")
count_G = g_code.count("Г") + g_code.count("г")
count_C = g_code.count("Ц") + g_code.count("ц")
count_T = g_code.count("Т") + g_code.count("т")
print(f"Аденин: {count_A}")
print(f"Гуанин: {count_G}")
print(f"Цитозин: {count_C}")
print(f"Тимин: {count_T}")


s = input()

print("Аденин:", s.lower().count('а'))
print("Гуанин:",s.lower().count('г'))
print("Цитозин:",s.lower().count('ц'))
print("Тимин:",s.lower().count('т'))



s = input().upper()
print('Аденин:', s.count('А'))
print('Гуанин:', s.count('Г'))
print('Цитозин:', s.count('Ц'))
print('Тимин:', s.count('Т'))



n = int(input())
result = 0
for _ in range(n):
    s = input()
    counter = s.replace("11", "_").count("_")
    if counter > 2:
        result += 1
print(result)



n = int(input())
m=0
for i in range(n):
    if input().count('11')>=3:
        m+=1
print(m)



s, count = input(), 0
for i in s:
    if i.isdigit():
        count += 1
print(count)


import re
print(len(re.findall(r'\d', input())))


s = input()
count = 0
for i in range(len(s)):
    if s[i] in '0123456789':
        count += 1
print(count)


site = input()
if site.endswith((".com", ".ru")):
    print("YES")
else:
    print("NO")



site = input()
domen = site.endswith((".com", ".ru"))

if domen is True:
    print("YES")
else:
    print("NO")


s = input()
if s.endswith(".ru") or s.endswith(".com"):
    print("YES")
else:
    print("NO")


s = input()
print("YES" if  s.endswith(".ru") or s.endswith(".com") else "NO")




s = input()
if s.count("f") == 1:
    print(s.find("f"))
elif s.count("f") > 1:
    print(s.find("f"), s.rfind("f"))
else:
    print("NO")


n = str(input())
first = n.find('f')
last = n.rfind('f')
count = n.count('f')
if count == 1:
    print(first)

elif count >= 1:
    print(first,last)

else:
    print('NO')



s = input()
index_start = s.find("h")
index_stop = s.rfind("h")
print(s[:index_start] + s[index_stop + 1:])

s = 'In {0}, someone paid {1} {2} for two pizzas.'
"In 2010, someone paid 10k Bitcoin for two pizzas.» (без кавычек)"
print(s.format("2010", "10k", "Bitcoin"))


s = 'In {0}, someone paid {1} {2} for two pizzas.'
year = 2010
price = '10k'
curr = 'Bitcoin'
print(s.format(year, price, curr))


s = 2010
m = "10k"
b = "Bitcoin"
print(f'In {s}, someone paid {m} {b} for two pizzas.')


year = 2010
amount = '10K'
currency = 'Bitcoin'

print(f'In {year}, someone paid {amount} {currency} for two pizzas.')



n1, n2 = int(input()), int(input())
for i in range(n1, n2+1):
    print(chr(i), end = " ")


for i in input():
    print(ord(i), end = " ")


n, s = int(input()), input()
for i in s:
    if ord(i) - n >= 97:
        print(chr(ord(i) - n) ,end = "")
    if ord(i) - n < 97:
        print(chr(ord(i) + 26 - n) ,end = "")



n1, n2 = int(input()), int(input())
for i in range(n1, n2+1):
    print(chr(i), end = " ")


s = input()
for i in range(len(s)):
    if i % 3 != 0:
        print(s[i], end='')


s = input()
if s.count("f") == 0:
    print("-2")
elif s.count("f") == 1:
    print("-1")
else:
    s.replace("f", "!", 1)
    print(s.replace("f", "!", 1).find("f"))


s = input()
index1 = s.find("h")
index2 = s.rfind("h")
s1 = s[:index1]
s2 = s[index1: index2 + 1]
s2 = s2[::-1]
s3 = s[index2 + 1:]
print(s1+s2+s3)


n = int(input())
list_1 = []
for i in range(1, n + 1):
    list_1 += [i]
print(list_1)



n = int(input())
print (list(range(1,n+1)))


n = int(input())
s = []
for i in range(97, 97 + n):
    s += [str(chr(i))]
print(s)


n = int(input())
alphabet = 'abcdefghijklmnopqrstuvwxyz'
print(list(alphabet[:n]))



n = int(input())
abc = ""
for i in range(97, 97 + n):
    abc += chr(i)
print(list(abc))


print(list(map(chr, range(97, 97 + int(input())))))


primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71]

print(primes[16])


evens = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
average = sum(evens) / len(evens)

print(average)



rainbow = ['Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Indigo', 'Violet']
rainbow[3] = "Зеленый"
rainbow[-1] = "Фиолетовый"
print(rainbow)


rainbow = ['Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Indigo', 'Violet']
rainbow[3:7:3] = ['Зеленый', 'Фиолетовый']

print(rainbow)


rainbow = ['Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Indigo', 'Violet']


print([x.replace("Green", "Зеленый").replace("Violet", "Фиолетовый") for x in rainbow])
