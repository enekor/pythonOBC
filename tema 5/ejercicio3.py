
def es_bisiesto(año):
    if año % 4 == 0 and (año % 100 != 0 or año % 400 == 0):
        return True
    return False

print(es_bisiesto(2022))
print(es_bisiesto(2000))