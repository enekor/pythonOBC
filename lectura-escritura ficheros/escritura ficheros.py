def main():
    fichero = open('.\lectura-escritura ficheros\mifichero.txt','w') #w para escribir y sobreescribir lo ya escrio, a para añadir texto al ya existente
    lineas = ['una linea bonita','salto de linea incorporado\n','otra linea mas']
    escribir_lineas(fichero,lineas)

def escribir_lineas(fichero,lineas):
    for linea in lineas:

        if not linea.endswith('\n'):
            linea += '\n'

        fichero.write(linea)

    fichero.close()

if __name__ == '__main__':
    main()
