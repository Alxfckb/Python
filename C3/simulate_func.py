#Explicar qué imprimiría el programa

def a(x):
    q=2
    x=3*x
    return q+x  

def b(x):
    global q 
    q+=x
    return q+x

q=0
x=3

print(a(x),b(x),a(x),b(x))
#Imprime (11,6,11,9) porque q es local en a, mientras en b es global. 
#El primer valor de b(x) se obtiene de tener q=0, cambiarlo a q=3 y retornar q+3=6
#El último valor de b(x) se obtiene de haber almacenado q=3, cambiarlo a q=3+3 y por último retornar q+3=9
