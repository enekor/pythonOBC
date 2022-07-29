from mailbox import NoSuchMailboxError


class Alumno:
    _nombre = ""
    _nota = 0

    def __init__(self,nombre,nota) -> None:
        self._nombre = nombre
        self._nota = nota

    def is_aprobado(self):
        if self._nota >= 5:
            return True
        return False

    def mi_nombre(self):
        return self._nombre

    def mi_nota(self):
        return self._nota

def ha_aprobado(alumno):
        
    if alumno.is_aprobado():
        print(alumno.mi_nombre(), "ha aprobado con un", alumno.mi_nota())
    else:
        print(alumno.mi_nombre(), "ha suspendido con un", alumno.mi_nota())

a = Alumno("Joel",7)
a2 = Alumno("Juan",4)

ha_aprobado(a)
ha_aprobado(a2)
