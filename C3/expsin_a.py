#Importar sin, exp, pi de math
from math import sin, exp, pi

#Definir la función g(t)
def h(t,a=10):
     r=exp(-a*t)*sin(pi*t)              #calcular el valor de la función en t
     print('h(%.1f)=%.1f' % (t,r))      #Imprimir (h(t)=r)
     
h(1)
h(0)