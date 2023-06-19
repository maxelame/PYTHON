#Дополните приведенный код, используя генератор, так, чтобы получить словарь result,
# состоящий из всех элементов словаря months , в которых ключ и значение поменялись местами.

months = {1: 'January', 2: 'February', 3: 'March', 4: 'April', 5: 'May', 6: 'June', 7: 'July', 8: 'August', 9: 'September', 10: 'October', 11: 'November', 12: 'December'}
result = {months[i] : i for i in months}

####
#В переменной s хранится строка пар число:слово. Дополните приведенный код, используя
# генератор, чтобы получить словарь result , в котором числа будут ключами, а слова – значениями.
s = '1:men 2:kind 90:number 0:sun 34:book 56:mountain 87:wood 54:car 3:island 88:power 7:box 17:star 101:ice'
result = {int(i.split(":")[0]) : i.split(":")[1] for i in s.split()}


####
