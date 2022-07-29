def main():
    fichero_w = open("mifichero.txt",'w')
    fichero_r = open('mifichero.txt','r')

    lineas = ['una linea bonita','salto de linea incorporado\n','otra linea mas']

    escribir_lineas(fichero_w,lineas)
    leer_lineas(fichero_r)

def escribir_lineas(fichero,lineas):
    for linea in lineas:

        if not linea.endswith('\n'):
            linea += '\n'

        fichero.write(linea)

    fichero.close()

def leer_lineas(fichero):
    lineas = fichero.readlines()
    for linea in lineas:
        print(linea)

if __name__ == '__main__':
    main()