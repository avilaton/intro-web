#! /usr/bin/env python3

# Generar la salida
file = open('cgi-bin/index.html')
template = file.read()
file.close()

print("Content-Type: text/html\n")
print()
print(template)
