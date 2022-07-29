from functools import reduce

lista = [3,6,3,5,6,8,9,6,234,7]

def operacion(x,y):
    print(f'x:{x}, y:{y}')
    return (x*y)-(y-x)

res = reduce(operacion,lista)
print(res)