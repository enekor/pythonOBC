from functools import reduce

lista = [1,2,3,4,5,6,7,8,9,10,11,12,13,14]

pares = filter(lambda x: x%2 == 0, lista)
suma = reduce(lambda x,y: x+y, pares)

print(suma)