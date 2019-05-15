#! /usr/bin/env python3

import cgi
import sqlite3

# Entender la entrada
form = cgi.FieldStorage()
search = form.getvalue('search', "")

# Conseguir los datos
DATABASE_URL = 'cgi-bin/escuela.sqlite'
connection = sqlite3.connect(DATABASE_URL)
query_string = "SELECT usuario FROM alumnos WHERE NOT admin"
query = connection.execute(query_string)

alumnos = [alumno[0] for alumno in query]


# Generar la salida
file = open('cgi-bin/index.html')
template = file.read()
file.close()

item = '<li>{alumno}</li>'
items = ""
for alumno in alumnos:
    items += item.format(alumno=alumno)
body = "<ul>{items}</ul>".format(items=items)
html = template.format(body=body, search=search)

print("Content-Type: text/html\n")
print()
print(html)
