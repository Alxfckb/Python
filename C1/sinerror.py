
#Codigo principal
    #x=1; 
    #print ('sin(%g)=%g' % (x, sin(x))
#Error 1: no se ha importado alguna librería ni las funciones correspondientes
#Código corregido
from math import sin
x=1

print('sin(%g) = %g' % (x,sin(x)))
print(sin(x))
