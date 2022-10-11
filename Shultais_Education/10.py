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
