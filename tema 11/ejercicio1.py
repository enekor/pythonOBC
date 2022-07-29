import sqlite3

conn = sqlite3.connect('miapp.db', isolation_level=None)
cursor = conn.cursor()
exits = False

def main():
    introduce_alumno()

    cursor.close()
    conn.close()


def introduce_alumno():
    identificador = int(input("Introduce el id"))
    nombre = input("introduce el nombre")
    apellido = input("Introduce el apellido")
    cursor.execute("CREATE TABLE if not exists Alumnos(id INT, nombre TEXT, apellido TEXT)")
    query = '''INSERT INTO Alumnos values (?, ?, ?)'''

    cursor.execute(query, (identificador, nombre, apellido))

    salir = input("Desea salir?")
    if salir == "Y":
        return True
        exit(0)
    else:
        introduce_alumno()


if __name__ == '__main__':
    main()