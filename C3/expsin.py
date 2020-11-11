#Importar sin, exp, pi de math
from math import sin, exp, pi

#Definir la función g(t)
def g(t):
     r=exp(-t)*sin(pi*t)    #calcular el valor de la función en t
     print( 'h(%.1f)=%.1f' % (t,r)) #imprimir h(t)=r
     
g(1)                        #Calcular g(1) y g(0)
g(0)