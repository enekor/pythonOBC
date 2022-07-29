numeros = [1,2,3,4,5,6,7,8,9,10]

def cuadradomasuno(x):
    return (x**2)+1

resultado = map(cuadradomasuno,numeros)
print(list(resultado))