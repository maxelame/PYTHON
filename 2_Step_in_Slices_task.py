# Напишите программу, которая получает из первого аргумента командной строки строку вида "aAbBcCdDeEfFgG".
# Далее программа должна преобразовать исходные данные в строку вида "abcdefgABCDEFG"
# и вывести результат. То есть сперва нужно поставить символы, которые стоят на нечетных позициях, а затем на четных.

import sys
text = sys.argv[1]
print(text[0::2]+text[1::2])