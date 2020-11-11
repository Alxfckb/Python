#Aproximar una función con una suma de senos
from math import sin,pi
#a)

#Definir funcion que calcula la serie de Fourier
def S(t,n,T):
    s=0
    for i in range(1,n+1):
        s+=(1/(2*i-1))*sin(((4*i-2)*pi*t)/T)
    return (4/pi)*s

#b) escribir función escalón

#Definir la función 
def f(t,T):
    if 0<t<T/2:
        return 1
    
    elif t==T/2:
        return 0
    
    elif T/2<t<T:
        return -1

a=[0.01,0.25,0.49]           #Definir lista con valores alpha que usaremos en f(t) y S(t;n)
n=[1,3,5,10,30,100]          #Definir lista con valores n que usaremos en f(t) y S(t;n)
T=2*pi                       #Periodo de la función

for j in range(3):
    print('---------')
    print('alpha=',a[j])            #indicar qué valor de alpha se está usando
    for i in range(6):
        print('n=',n[i],'f(t)-S(t;n)=', f(a[j]*T,T)- S(a[j]*T,n[i],T),sep='  ') #Indicar n y calcular el error
        print()
        
#Conforme n crece, el error se hace más pequeño, el menor error obtenido fue con alpha=0.25 y n=100

        
    
        
        