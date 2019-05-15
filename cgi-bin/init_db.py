import sqlite3

DATABASE_URL = 'cgi-bin/escuela.sqlite'

connection = sqlite3.connect(DATABASE_URL)

connection.executescript("""
CREATE TABLE alumnos (
    id INTEGER PRIMARY KEY NOT NULL,
    usuario TEXT NOT NULL,
    password TEXT NOT NULL,
    admin BOOLEAN DEFAULT FALSE
);

INSERT INTO alumnos (usuario, password, admin) VALUES 
('Gaston', 'super secreto que nadie sabe', 1),
('Vero', '123456', 0),
('Jerónimo', '123456', 0),
('Graciela', '123456', 0)
;
""")
connection.close()
