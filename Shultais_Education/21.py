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

