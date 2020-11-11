#Implementar la función adaptativa del trapecio 

#Importar las funciones que usaremos
from math import sin,cos, pi, sqrt
import trapezint as tpz

#Definir la función
def adaptative_trapezint(f,a,b,eps=1E-5):   
    global n        
    ah=(b-a)/20                         #h estimado para encontrar el máximo de f''(x)
    l=[]                                #Inicializar una lista para almacenar valores de f''(x)
    for i in range(20):
        d=(f(a+i*ah+ah)-2*f(a+i*ah)+f(a+i*ah-ah))/ah**2 #Calcular valores de f''(x)
        l.append(abs(d))                                #Añadir los valores de |f''(x)| a la lista
    
    maxi=max(l)                                         #Escoger el valor máximo en la lista
         
    h=sqrt(12*eps)*((b-a)*maxi)**(-1/2)                 #Calcular h para integrar
    n = int((b-a)/h)                                    #Calcular n para integrar
    return tpz.trapezint(f, a, b, n)                    #Calcular la integral


#Pruebas 
'''
print('CON LA FUNCIÓN adaptative_trapezint')
    
print('Int(0,pi)cos x=',adaptative_trapezint(cos,0,pi))
print('error= ', abs((adaptative_trapezint(cos,0,pi)-0)),'n=',n)

print()

print('Int(0,pi/2)cos x=',adaptative_trapezint(cos,0,pi/2))
print('error= ', abs((adaptative_trapezint(cos,0,pi/2)-1)),'n=',n)

print()
print('Int(0,pi)sin(x)=',adaptative_trapezint(sin,0,pi))
print('error= ' ,abs((adaptative_trapezint(sin,0,pi)-2)),'n=',n)

print()
print('Int(0,pi/2)sin(x)=',adaptative_trapezint(sin,0,pi/2))
print('error= ' ,abs((adaptative_trapezint(sin,0,pi/2)-1)),'n=',n)
'''
 


