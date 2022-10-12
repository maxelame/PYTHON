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
