#Implementar la función gaussiana
from math import exp,sqrt,pi

#Definir la función
def gauss(x,m,s):
    f=1/(sqrt(2*pi)*s)* exp((-1/2)*((x-m)/s)**2)
    return f


n=5                     #n de prueba
m=0                     #m de prueba
s=2                     #s de prueba
h=(10*s)/(n-1)          #tamaño de los intervalos
X=[(m-5*s)+i*h for i in range(n)]           #Generar valores para x
print('    x   ','   G')

for i in range(n):
    x=X[i]
    print('%5d %f' %(x,gauss(x,m,s)))       #Valuar la función e imprimir la tabla
    