import time

FIN = 19
hora = time.localtime().tm_hour

def me_voy_ya_a_casa():
    if hora < FIN:
        cuanto_queda = FIN - hora
        print("aun quedan",cuanto_queda,"horas")
    elif hora > FIN:
        pasas = hora - FIN
        print("te has pasado",pasas,"horas de las 19:00")
    else:
        print("son las 19:00, es hora de irse!")

if __name__ == "__main__":
    me_voy_ya_a_casa()