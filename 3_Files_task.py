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












