def f_min(self, start, end):
    minim = self[start]
    min_idx = start
    for idx in range(start, end):
        if self[idx] < minim:
            minim = self[idx]
            min_idx = idx
    return min_idx

def select_sort(self):
    i = 0
    arr_size  = len(self)
    while i < arr_size:
        min_idx = f_min(self, i, arr_size)
        self[min_idx], self[i] = self[i], self[min_idx]
        i += 1
    return self

a = [78, -32, 5, 39, 58, -5, -63, 57, 72, 9, 53, -1, 63, -97, -21, -94, -47, 57, -8, 60, -23, -72, -22, -79, 90, 96, -41, -71, -48, 84, 89, -96, 41, -16, 94, -60, -64, -39, 60, -14, -62, -19, -3, 32, 98, 14, 43, 3, -56, 71, -71, -67, 80, 27, 92, 92, -64, 0, -77, 2, -26, 41, 3, -31, 48, 39, 20, -30, 35, 32, -58, 2, 63, 64, 66, 62, 82, -62, 9, -52, 35, -61, 87, 78, 93, -42, 87, -72, -10, -36, 61, -16, 59, 59, 22, -24, -67, 76, -94, 59]

print(select_sort(a))



# объявление функции
def draw_box():
    print("*" * 10)
    for i in range(12):
        print("*        *")
    print("*" * 10)

# основная программа
draw_box()  # вызов функции



# объявление функции
def draw_triangle():
    for i in range(10):
        print("*" * (i+1))

# основная программа
draw_triangle()  # вызов функции



def draw_box(height, width):
    height = 2
    width = 10
    for i in range(height):
        print('*' * width)

n = 5
m = 7
draw_box(n, m)
print(n, m)



# объявление функции
def draw_triangle(fill, base):
    for i in range(1, int(base / 2) +2):
        print(fill * i)
    for i in range(int(base / 2), 0, -1):
        print(fill * i)
# считываем данные
fill = input()
base = int(input())

# вызываем функцию
draw_triangle(fill, base)
