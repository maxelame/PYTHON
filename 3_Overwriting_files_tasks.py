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

'''Очищаем файл

Рядом с программой находится файл index.html.
Напишите код, который очистит содержимое этого файла.

После того как программа выполнится, система сама откроет файл index.html и проверит его содержимое.'''

new_file = open ("index.html", "w", encoding = "utf8")
new_file.close()

'''Годовой отчет

Рядом с программой находятся 4 файла: q1.txt, q2.txt, q3.txt и q4.txt.
Каждый файл содержит целое число — квартальную прибыль компании.

Напишите программу, которая читает все квартальные отчеты, суммирует результат и сохраняет его в файл year.txt.

После того как программа выполнится, система сама откроет файл year.txt и проверит его содержимое.
 '''


file_q1 = open ("q1.txt", "r" , encoding = "utf8")
q1 = file_q1.read()
file_q1.close()
file_q2 = open ("q2.txt", "r" , encoding = "utf8")
q2 = file_q2.read()
file_q2.close()
file_q3 = open ("q3.txt", "r" , encoding = "utf8")
q3 = file_q3.read()
file_q3.close()
file_q4 = open ("q4.txt", "r" , encoding = "utf8")
q4 = file_q4.read()
file_q4.close()
q = int(q1) +int(q2)+ int(q3)+ int(q4)
file_year = open ("year.txt", "w", encoding = "utf8")
file_year.write(str(q) +"\n")
file_year.close()




