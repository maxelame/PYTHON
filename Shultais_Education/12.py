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
