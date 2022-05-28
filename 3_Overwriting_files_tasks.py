'''Создаем документ

Напишите программу, которая создает файл index.html и добавляет в него следующую строку:
<html><head></head><body></body></html>.

После того как программа выполнится, система сама откроет файл index.html и проверит его содержимое.
'''
new_file = open ("index.html", "w")
new_file.write("<html><head></head><body></body></html>")
new_file.close()
