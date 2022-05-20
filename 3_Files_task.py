'''Книги

Рядом с программой находится файл book.txt, в котором содержится название книги.
Напишите программу, которая читает файл и выводит его содержимое.
Пример использования в командной строке Windows:
> python program.py
> Название книги
 '''
book_file = open("book.txt" , encoding = "utf8")
book = book_file.read()
print(book)


 '''Язык

Рядом с программой находится файл language.txt, в котором содержится текст в кодировке cp1251.
Напишите программу, которая читает файл и выводит его содержимое.
Пример использования в командной строке Windows:
> python program.py
> English
 '''
language_file = open("language.txt" , encoding = "cp1251")
language = language_file.read()
print(language)

'''Годовая зарплата

Рядом с программой находится файл month_salary.txt, в котором хранится месячная зарплата.
Напишите программу, которая читает этот файл и выводит на его основе годовую зарплату.

Если в файле будет содержаться 10000, то программа должна отработать так:
> python program.py
> 120000'''

salary_file = open("month_salary.txt", encoding = "utf8")
salary = int(salary_file.read())
print(salary*12)

'''Первый шаблон

Рядом с программой находится файл template.txt, в котором хранится шаблон текста.
В шаблоне есть текст вида {{ name }}, который нужно заменить на реальное имя пользователя.

Напишите программу, которая принимает из первого аргумента командной строки имя пользователя, а затем подставляет его в шаблон и выводит результат.

Если в файле будет содержаться «Привет, {{ name }}!», то программа должна отработать так:
> python program.py Никита
> Привет, Никита!'''

import sys
name = str(sys.argv[1])
template_file = open("template.txt", encoding = "utf8")
template = (template_file.read())
template = template.replace("{{ name }}" , name)
print(template)










