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
