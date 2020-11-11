#Función que devuelve las raices de una ec. cuadrática
#Importar la función raiz cuadrada
import numpy as np
from numpy.lib.scimath import sqrt

#a)

#Definir la función que calcula raices de ec. cuadráticas
def roots(a,b,c):
    dis = b**2-4*a*c            #Calcular el discriminante

    if dis>=0:                  #Caso de raices reales
        x1=(-b+sqrt(dis))/(2*a) #Calcular primera raiz
        x2=(-b-sqrt(dis))/(2*a) #Calcular segunda raiz
        return x1 , x2
        
    
        
    elif dis<0:                 #Caso de raices complejas  
        x1=(-b+sqrt(dis))/(2*a) #Calcular primera raiz
        x2=x1.conjugate()            #Calcular segunda raiz
        return x1 , x2
        
        
        
#b)
#Definir función de raices reales
def test_roots_float():
        if type(roots(1,2,1)[1])==np.float64 and type(roots(1,2,1)[0])==np.float64: #Chequeamos que las raices sean de tipo float
                  print('float!') #mensaje de confirmación
        else:
            print('not float')    #Mensaje de negación
            
            
#Definir función de prueba para raices complejas
def test_roots_complex():
    if type(roots(1,0,1)[1])==np.complex128 and type(roots(1,0,1)[0])==np.complex128: #Chequeamos que las raices sean de tipo complex
        print('complex!')                       #mensaje de confirmación
    else:
        print('not complex')                    #Mensaje de negación
            
    