#Aproximar pi
#Importar las funciones sin, cos y pi
from math import sin, cos, pi
from pathlength import pathlength as pl



x=[]
y=[]
#Generar valores de x y y
for k in range(2,11):
    n=2**k
    for i in range(n+1):
                X=(1/2)*cos(2*pi*i/n)         #Calcular valores de x
                Y=(1/2)*sin(2*pi*i/n)         #Calcular valores de y
                x.append(X)                   #Almacenar valores en lista x    
                y.append(Y)                   #Almacenar valores en lista y
    print('n=',n,'   ','pi=',pl(x,y), 'error=',pi-pl(x,y)) #Imprimir
    #Reiniciar listas 
    x=[]                                       
    y=[]            
    
    
   






