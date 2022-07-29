import _thread as t
import time

def hora_actual(nombre,segundos):
    time.sleep(segundos)
    print(f'hola {nombre} - {time.ctime(time.time())}')
    

t.start_new_thread(hora_actual,('pepe',1))
t.start_new_thread(hora_actual,('juan',4))

while True:
    time.sleep(0.1)