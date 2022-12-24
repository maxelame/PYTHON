a, b = int(input()), int(input())
print(a+b, a-b, a*b, a/b, a//b, a%b, (a**10 + b**10)**0.5, sep = "\n")


print(len(input().split()))


symbols = ["Обезьяна", "Петух", "Собака", "Свинья", "Крыса", "Бык", "Тигр", "Заяц", "Дракон", "Змея", "Лошадь", "Овца"]
print(symbols[int(input()) % 12])
