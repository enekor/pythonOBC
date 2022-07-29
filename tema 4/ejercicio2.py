inicio = 1
final = 20
impares = []

for numero in range(inicio,final):
    if(numero%2 != 0):
        impares.append(numero)

print(impares)