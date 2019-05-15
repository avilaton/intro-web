#! /usr/bin/env python3

import sqlite3


# Conseguir los datos
DATABASE_URL = 'cgi-bin/escuela.sqlite'
connection = sqlite3.connect(DATABASE_URL)
query_string = "SELECT usuario FROM alumnos WHERE NOT admin"
query = connection.execute(query_string)

alumnos = list(query)


# Generar la salida
file = open('cgi-bin/index.html')
template = file.read()
file.close()

item = '<li>{alumno}</li>'
items = ""
for alumno in alumnos:
    items += item.format(alumno=alumno)
body = "<ul>{items}</ul>".format(items=items)
html = template.format(body=body)

print("Content-Type: text/html\n")
print()
print(html)
