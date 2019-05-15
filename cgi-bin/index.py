#! /usr/bin/env python3

# Generar la salida
file = open('cgi-bin/index.html')
template = file.read()
file.close()

body = ['Gaston', 'Verónica', 'Jerónimo']

html = template.format(body=body)

print("Content-Type: text/html\n")
print()
print(html)
