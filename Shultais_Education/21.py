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
