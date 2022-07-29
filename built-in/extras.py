from getpass import getpass

#zip
nombres = ['Juan','Pepe']
apellidos = ['Garcia','Romero']

print(list(zip(nombres,apellidos))) #[('Juan', 'Garcia'), ('Pepe', 'Romero')]

#any,all

lista = [True, False, 3==2, 5==5]
print(any(lista)) #True porque minimo una es True
print(all(lista)) #False porque tienen que ser todas True

#round

a = 6.7
b = 4.2

print(round(a)) #7
print(round(b)) #4

#min

numeros = [3,4,5,2,7,8,9]
print(min(numeros)) #2

#pow

print(pow(2,4)) # == 2**4 == 16

#sorted

letras = ['z','a','u']
print(list(sorted(letras))) #['a', 'u', 'z']

#input de passwd

#passwd = getpass('passwd: ')
#print(passwd)