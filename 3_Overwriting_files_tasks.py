'''Создаем документ

Напишите программу, которая создает файл index.html и добавляет в него следующую строку:
<html><head></head><body></body></html>.

После того как программа выполнится, система сама откроет файл index.html и проверит его содержимое.
'''
new_file = open ("index.html", "w")
new_file.write("<html><head></head><body></body></html>")
new_file.close()

'''Заполняем шаблон

Рядом с программой находится файл template.txt, в котором хранится шаблон текста.
В шаблоне есть текст вида {{ name }}, который нужно заменить на реальное имя пользователя.

Напишите программу, которая принимает из первого аргумента командной строки имя пользователя, а затем подставляет его в шаблон и записывает результат в файл.

После того как программа выполнится, система сама откроет файл template.txt и проверит его содержимое.'''

import sys
name = str(sys.argv[1])
new_template = open ("template.txt","r", encoding = "utf8")
template = new_template.read()
template = template.replace("{{ name }}",name)
new_template.close()

new_template = open ("template.txt","w", encoding = "utf8")
new_template.write(template)
new_template.close()





