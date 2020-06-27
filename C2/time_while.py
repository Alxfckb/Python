import time 

t0= time.time()
while (time.time() - t0 > 10):
    print('.....I like while loops!')
    time.sleep(2)
print('oh no - the loop is over')

'''
-Este código imprime un texto hasta que la diferencia entre el tiempo en el que se 
ejecutó el programa y el tiempo que el programa lleva ejecutándose sea 10 segundos

-Cuando se cambia la condicion a > el loop jamás comienza porque la condición se evalúa rápido y no
permite que la diferencia sea mayor a 10 segundos

'''

