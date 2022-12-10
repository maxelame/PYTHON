# объявление функции
def is_prime(num):
    counter = 0
    for i in range(1, num + 1):
        if num % i == 0:
            counter += 1
    if counter > 2 or num == 1:
        return False
    else:
        return True

# считываем данные
n = int(input())

# вызываем функцию
print(is_prime(n))



# объявление функции
def is_prime(num):
    return len([i for i in range(1, num+1) if num % i == 0]) == 2

# считываем данные
n = int(input())

# вызываем функцию
print(is_prime(n))




def is_prime(num):
    counter = 0
    for i in range(1, num + 1):
        if num % i == 0:
            counter += 1
    if counter > 2 or num == 1:
        return False
    else:
        return True


def get_next_prime(num):
    if is_prime(num):
        num += 1
    while not is_prime(num):
        num += 1
    return num


# считываем данные
n = int(input())

# вызываем функцию
print(get_next_prime(n))


# объявление функции
def is_password_good(password):
    if len(password) > 7 and not password.isupper() and not password.islower() and password.isalnum() and not password.isdigit() and not password.isalpha():
        return True
    else:
        return False


# считываем данные
txt = input()

# вызываем функцию
print(is_password_good(txt))






# объявление функции
def is_one_away(word1, word2):
    if len(word1) == len(word2):
        counter = 0
        for i in range(len(word1)):
            if word1[i] != word2[i]:
                counter += 1
        if counter == 1:
            return True
        else:
            return False
    else:
        return False
# считываем данные
txt1 = input()
txt2 = input()
# вызываем функцию
print(is_one_away(txt1, txt2))





# объявление функции
def is_palindrome(text):
    s_list = list(text.lower())
    new_list = []
    for i in s_list:
        if i.isalpha():
            new_list.append(i)
    print(new_list)
    s = "".join(new_list)
    print(s)
    if s == s[::-1]:
        return True
    else:
        return False


# считываем данные
txt = "Standart - smallest, sell Amstrad nats."

# вызываем функцию
print(is_palindrome(txt))




User avatar
Комментарий закреплён
Тимур 👨‍🏫 Гуев
3 года назад

Сначала удаляем ненужные символы, затем строим срез, переворачивающий строку и проверяем на равенство:
Верное решение #191449702
Python 3

# объявление функции
def is_palindrome(text):
    symbols = [' ', ',', '.', '!', '?', '-']
    for c in symbols:
        text = text.replace(c, '')
    text = text.lower()
    return text == text[::-1]

# считываем данные
txt = input()

# вызываем функцию
print(is_palindrome(txt))

