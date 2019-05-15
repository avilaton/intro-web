#! /usr/bin/env python3

# Generar la salida
file = open('cgi-bin/index.html')
template = file.read()
file.close()

alumnos = ['Gaston', 'Verónica', 'Jerónimo']

item = '<li>{alumno}</li>'
items = ""
for alumno in alumnos:
    items += item.format(alumno=alumno)
body = "<ul>{items}</ul>".format(items=items)
html = template.format(body=body)

print("Content-Type: text/html\n")
print()
print(html)
