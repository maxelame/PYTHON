######
def fancy(length, char1='-', char2='*'):
    return (char1 + char2) * length + char1


print(fancy(char2='!'))

######

def matrix(n =1,m = 0, a = 0):
    if n == 1 and not m:
        m = 1
    elif n != 1 and not m:
        m = n
    return [[a]*m for _ in range(n)]

######
def f(n=3):
    return n + 7


print(f(f(f())))

#####
def func(x, y, *args):


#####

def func(x, y, *args):
    return len(args)


print(func(10, 20, 30, 40, 50, 60))


#####

def func(*args):
    return max(args) + min(args)


print(func(10, 15, *[31, 42, 5, 1], *(17, 28, 19, 100), 13, 12))

######

func(5, 6, 13, 17, 56)
func(2, 7)

######

def count_args(*args):
  return len(args)

print(count_args([], (''), 'a', False))

######

def sq_sum(*args):
    return sum([m ** 2 for m in args])

######

def sq_sum(*a):
    return sum(map(lambda i: i*i, list(a)))

#####

def sq_sum(*args) -> int | float:
    return sum(map(lambda i: i*i, args))


#####

def mean(*args):
    s = [i for i in args if type(i) in [int, float]]
    return (float(0) if len(s) == 0 else float(sum(s)/len(s)))

######

def greet(x, *args):
    str1 = "Hello, " + x
    for i in args:
        str1 += " and " + i
    return str1


######



def greet(name, *args):
    return f'Hello, {" and ".join((name,) + args)}!'

#####

def print_products(*args):
    list1 = []
    for i in args:
        if type(i) in [str] and len(i) != 0:
            list1.append(i)
    if len(list1) == 0:
        print("Нет продуктов")
    else:
        for i in range(1, len(list1) + 1):
            print(f"{i}) {list1[i-1]}")


#####
def info_kwargs(*kwargs):
    for key, value in sorted(kwargs.items()):
        print(f"{key}: {value}")


info_kwargs(first_name='Timur', last_name='Guev', age=28, job='teacher')
