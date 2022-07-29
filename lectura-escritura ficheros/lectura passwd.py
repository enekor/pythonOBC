def main():
    usuarios = listarUsuarios()
    for usuario in usuarios:
        print(f'usuario: {usuario}')

def listarUsuarios():
    f = open('/etc/passwd','r') #r porque solo quiero lectura, mirar documentacion para los diferentes tipos
    datos = f.readlines()
    f.close() #buena practica cerrar el fichero al terminar de usarlo

    resultado = []

    for linea in datos:
        if (linea[0] == '#' or linea[0] == '_'): #se salta las lineas que sean de comentario o de usuarios de procesos (virtuales)
            continue

        partes = linea.split(':')
        resultado.append(partes[0])

    return resultado

if __name__ == '__main__':
    main()