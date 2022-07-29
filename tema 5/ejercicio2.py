
def es_primo(numero):
    for n in range(2, numero):
        if numero % n == 0:
            return False
    return True

print(es_primo(34))
print(es_primo(7))