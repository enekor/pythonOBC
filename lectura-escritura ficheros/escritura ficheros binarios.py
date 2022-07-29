import pickle

class juguete:
    nombre = ''
    precio = 0.0

    def __init__(self,name, price) -> None:
        self.nombre = name
        self.precio = price

    def get_nombre(self):
        return self.nombre
    
j = juguete('dinosaurio',145.7)
f = open('.\lectura-escritura ficheros\mificherobinario.bin','wb') #b porque es un archivo binario
pickle.dump(j,f) #dump escribe el objeto en el archivo

#por alguna razon me esta dando fallo en el load, pero deberia funcionar

#archivo = open('.\lectura-escritura ficheros\mificherobinario.bin','rb')
#dino = pickle.load(archivo)
#print(dino.get_nombre())