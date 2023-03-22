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
