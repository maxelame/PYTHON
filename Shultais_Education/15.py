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
