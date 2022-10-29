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
