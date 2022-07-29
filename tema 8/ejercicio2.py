import pickle as binl

class vehiculo:
    marca = ''
    precio = 0.0

    def __init__(self,brand, price) -> None:
        self.marca = brand
        self.precio = price

    def get_nombre(self):
        return self.nombre
    
v = vehiculo('dinosaurio',145.7)
f = open('mivehiculo.bin','wb') 
binl.dump(v,f) 


archivo = open('mivehiculo.bin','rb')
coche = binl.load(archivo)
print(coche.get_nombre())