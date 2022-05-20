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










