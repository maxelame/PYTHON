numbers = (3, 5, 7, 9)

colors = ('red', 'green', 'blue')
colors[0] = 'black'
print(colors)

numbers = (1, [2, 3], 4)
numbers[1][0] = 17
print(numbers)


countries = ('Russia', 'Argentina', 'Spain', 'Slovakia', 'Canada', 'Slovenia', 'Italy')
last = countries[-1]
print(last)

primes = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71)
print(primes[:6])


countries = ('Russia', 'Argentina', 'Slovakia', 'Canada', 'Slovenia', 'Italy', 'Spain', 'Ukraine', 'Chile', 'Cameroon')
print(countries[2:])


countries = ('Russia', 'Argentina', 'Slovakia', 'Canada', 'Slovenia', 'Italy', 'Spain', 'Ukraine', 'Chile', 'Cameroon')
print(countries[:countries.index('Ukraine')])


countries = ('Russia', 'Argentina', 'Slovakia', 'Canada', 'Slovenia', 'Italy', 'Spain', 'Ukraine', 'Chile', 'Cameroon')
print(countries[3:-2])

countries = ('Russia', 'Argentina', 'Slovakia', 'Canada', 'Slovenia', 'Italy', 'Spain', 'Ukraine', 'Chile', 'Cameroon')
print(countries[3:-2])


countries = ('Romania', 'Poland', 'Estonia', 'Bulgaria', 'Slovakia', 'Slovenia', 'Hungary')
number = len(countries)
print(number)


numbers = (12.5, 3.1415, 2.718, 9.8, 1.414, 1.1618, 1.324)
print(max(numbers) + min(numbers))


countries = ('Russia', 'Argentina', 'Spain', 'Slovakia', 'Canada', 'Slovenia', 'Italy', 'Spain', 'Ukraine', 'Chile', 'Spain', 'Cameroon')
number = countries.count("Spain")
print(number)


numbers1 = (1, 2, 3)
numbers2 = (6,)
numbers3 = (7, 8, 9, 10, 11, 12, 13)
print(numbers1 * 2 + numbers2 * 9 + numbers3)

city_name = input()
city_year = int(input())
city = (city_name, city_year)
print(city)

tuples = [(), (), ('',), ('a', 'b'), (), ('a', 'b', 'c'), (1,), (), (), ('d',), ('', ''), ()]
non_empty_tuples = [i for i in tuples if len(i) != 0]

print(non_empty_tuples)


tuples = [(10, 20, 40), (40, 50, 60), (70, 80, 90), (10, 90), (1, 2, 3, 4), (5, 6, 10, 2, 1, 77)]
new_tuples = [i[:-1] + (100,) for i in tuples]
print(new_tuples)


tuples = [(10, 20, 40), (40, 50, 60), (70, 80, 90), (10, 90), (1, 2, 3, 4), (5, 6, 10, 2, 1, 77)]
new_tuples = [i[:-1] + (100,) for i in tuples]
print(new_tuples)

poets = [
    ('Есенин', 13),
    ('Тургенев', 14),
    ('Маяковский', 28),
    ('Лермонтов', 20),
    ('Фет', 15)]

for i in range(len(poets)):
    for j in range(i+1, len(poets)):
        if poets[i][1] > poets[j][1]:
            poets[i], poets[j] = poets[j], poets[i]

print(poets[0])
print(poets[-1])


poets = [
    ('Тургенев', 14),
    ('Есенин', 13),
    ('Маяковский', 28),
    ('Фет', 15),
    ('Лермонтов', 20)]

for i in range(len(poets)):
    for j in range(i+1, len(poets)):
        if poets[i] > poets[j]:
            poets[i], poets[j] = poets[j], poets[i]

print(poets[0])
print(poets[-1])



numbers = (2, 3, 5, 7, -11, 13, 17, 19, 23, 29, 31, -6, 41, 43, 47, 53, 59, 61, -96, 71, 1000, -1)
result = 1
for i in numbers:
    result *= i
print(result)


from functools import reduce
numbers = (2, 3, 5, 7, -11, 13, 17, 19, 23, 29, 31, -6, 41, 43, 47, 53, 59, 61, -96, 71, 1000, -1)
print(reduce(lambda a, b: a * b, numbers))

data = 'Python для продвинутых!'
print(tuple(data))


poet_data = ('Пушкин', 1799, 'Санкт-Петербург')
poet_data_list = list(poet_data)
poet_data_list[2] = "Москва"
poet_data = tuple(poet_data_list)

print(poet_data)


poet_data = ('Пушкин', 1799, 'Санкт-Петербург')
poet_data = poet_data[:-1]+('Москва',)

print(poet_data)


poet_data = ('Пушкин', 1799, 'Санкт-Петербург')
poet_data = tuple(('Пушкин', 1799, 'Москва'))

print(poet_data)


numbers = ((10, 10, 10, 12), (30, 45, 56, 45), (81, 80, 39, 32), (1, 2, 3, 4), (90, 10))
print([sum(i)/len(i) for i in numbers])


a, b, c = int(input()), int(input()), int(input())
print((-b/(2*a), (4*a*c - b ** 2)/(4*a)))


a, b, c = 10, 20, 30
c, b, a = a + b, b*2, a + b + c
print(a, b, c)


points = [('матан', 100), ('линал', 98), ('ангем', 90)]
subject, value = points[1]
print(subject, value)



notes = ('Do', 'Re', 'Mi', 'Fa', 'Sol', 'La', 'Si')
do, re, mi, *tail = notes
print(tail)
#  ['Fa', 'Sol', 'La', 'Si']


notes = ('Do', 'Re', 'Mi', 'Fa', 'Sol', 'La', 'Si')
do, re, *tail, si = notes
print(tail)
# ['Mi', 'Fa', 'Sol', 'La']


n = int(input())
f1, f2, f3 = 1, 1, 1
for i in range(n):
    print(f1, end = " ")
    f1, f2, f3 = f2, f3, f1 + f2 + f3


tpl = (100)
print(tpl * 2)
# 200

tpl = (100,)
print(tpl * 2)
# (100, 100)


tpl = (10, 20, 30, 40, 50, 60, 70, 80)
print(tpl[2:5], tpl[:4], tpl[3:])
#  (30, 40, 50) (10, 20, 30, 40) (40, 50, 60, 70, 80)

tpl = (100, 200, 300, 400, 500)
print(tpl[-2])
print(tpl[-4:-1])
# 400
#(200, 300, 400)

a, b, *c = range(7)


n = int(input())
f1, f2, f3 = 1, 1, 1
for i in range(n):
    print(f1, end = " ")
    f1, f2, f3 = f2, f3, f1 + f2 + f3



points = [('матан', 100), ('линал', 98), ('ангем', 90)]
subject, value = points[1]
print(subject, value)


poets = [
    ('Тургенев', 14),
    ('Есенин', 13),
    ('Маяковский', 28),
    ('Фет', 15),
    ('Лермонтов', 20)]

for i in range(len(poets)):
    for j in range(i+1, len(poets)):
        if poets[i] > poets[j]:
            poets[i], poets[j] = poets[j], poets[i]

print(poets[0])
print(poets[-1])


points = [('матан', 100), ('линал', 98), ('ангем', 90)]
subject, value = points[1]
print(subject, value)



points = [('матан', 100), ('линал', 98), ('ангем', 90)]
subject, value = points[1]
print(subject, value)


numbers = (3, 5, 7, 9)

colors = ('red', 'green', 'blue')
colors[0] = 'black'
print(colors)

numbers = (1, [2, 3], 4)
numbers[1][0] = 17
print(numbers)

n, m, k, x, y, z = ((int(input()) for _ in range(6)))
print((m-x-y) + (n-x) + (k-y) + x + y + z)

n, m, k, x, y, z = int(input()), int(input()), int(input()), int(input()), int(input()), int(input())
def command(n, m, k, x, y, z):
    return n + m - x -y + k + z
print(command(n, m, k, x, y, z)



n, m, k, x, y, z, t, a = (int(input()) for _ in range(8))
res1 = 2*(x+y+z) - 3*(n+m+k) + 3*t
print(res1)
res2 = 2*(n+m+k) - (x+y+z) - 3*t
print(res2)
print(a- (res1 + res2  +t))



n, m, k, x, y, z, t, a = (int(input()) for _ in range(8))
res1 = 2*(x+y+z) - 3*(n+m+k) + 3*t
print(res1)
res2 = 2*(n+m+k) - (x+y+z) - 3*t
print(res2)
print(a- (res1 + res2  +t))


myset = set('ъъъ эээ ююю яяя')


myset = set('aaabcccc    11222')


myset = set([1, 2, 3, '1', '2', '3'])

myset = set([1, 2, 2, 3, 4, 4, 4])
print(len(myset))


numbers = {20, 6, 8, 18, 18, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 12, 8, 8, 10, 4, 2, 2, 2, 16, 20}
average = sum(numbers)/len(list(numbers))

print(average)


myset1 = set([1, 2, 3, 4, 5])
myset2 = set('12345')

print(myset1 == myset2)



numbers = {9089, -67, -32, 1, 78, 23, -65, 99, 9089, 34, -32, 0, -67, 1, 11, 111, 111, 1, 23}
summ = 0
for i in numbers:
    summ += i ** 2
print(summ)


fruits = {'apple', 'banana', 'cherry', 'avocado', 'pineapple', 'apricot', 'banana', 'avocado', 'grapefruit'}
sorted_fruits = sorted(fruits, reverse = True)
print(*sorted_fruits, sep = "\n")

print(len(set(input())))



s = input()
if len(s) == len(set(s)):
    print("YES")
else:
    print("NO")


a = input()
print(('NO','YES')[len(a) == len(set(a))])



s = input()
print('YES' if len(set(s)) == len(s) else 'NO')


print('YES' if len(a:= input())==len(set(a)) else 'NO')


s1, s2 = input(), input()
print("YES" if len(set(s1+s2)) == 10 else "NO")


s1, s2 = [input() for _ in "00"]
print("YES" if set(s1) == set(s2) else "NO")


print('YES' if set(input()) == set(input()) else 'NO')


print(('NO', 'YES')[set(input()) == set(input())])


s = input().split()
print(('NO', 'YES')[set(s[0]) == set(s[1]) == set(s[2])])

myset.add(item)




myset = set()
for i in range(10):
    if i % 2 == 0:
        myset.add('even')
    else:
        myset.add('odd')
print(len(myset))



myset = set('python')
item = myset.pop()
print(item, len(myset))


myset = set()

item = myset.pop()
print(item)




list_1 = [input().lower() for _ in range(int(input()))]
for i in list_1:
    print(len(set(i)))

list_1 = [input().lower() for _ in range(int(input()))]
s = ""
for i in list_1:
    s += i
print(len(set(s)))
