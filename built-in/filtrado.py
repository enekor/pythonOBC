from unittest import result


nombres = ['pepe','juan','pedro','isabel','maria','poltergeist']

def filtro(x):
    if str(x).startswith('p'):
         return True
    return False

resultado = filter(filtro,nombres)
print(list(resultado))