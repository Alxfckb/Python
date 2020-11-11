#Encontrar máximos y mínimos de una función
from math import cos, pi

#Definir la función
def maxmin(f,a,b,n=1000):
    
    h=(b-a)/(n-1)                           #Tamaño de cada intervalo
    maxmin=[]                               #Inicializar lista que almacena valores de f(x)
    
    for i in range(n):
        maxmin.append(f(a+i*h))             #Agregar valores generados a la lista maxmin
    
    MAX=max(maxmin)                         #Extraer el máximo de la lista
    MIN=min(maxmin)                         #Extraer el mínimo de la lista 
    return MAX , MIN

#Definir función test
def test_maxmin():
    a=pi/2                            #x de prueba
    b=2*pi
    f=cos                             #f de prueba
    tol=1E-9                          #Tolerancia
    expectedMAX = 1                   #Valor teórico del maximo de coseno
    expectedMIN = -1                  #Valor teórico del minimo de coseno  
    computedMAX = maxmin(f,a,b)[0]    #Máximo obtenido con maxmin        
    computedMIN = maxmin(f,a,b)[1]    #Mínimo obtenido con maxmin
    
    successMAX  = abs(expectedMAX-computedMAX) < tol         #Caso de máximo exitoso 
    successMIN  = abs(expectedMIN-computedMIN) < tol         #Caso de mínimo exitoso   
    
    msgMAX      = '(computed max) %g != %g (expected max)' %\
        (computedMAX,expectedMAX)         #Mensaje para caso máximo exitoso
    msgMIN      = '(computed min) %g != %g (expected min)' %\
        (computedMIN,expectedMIN)         #Mensaje para caso mínimo exitoso    
   
    assert successMAX, msgMAX             #Desplejar el mensaje si el caso no es exitoso
    assert successMIN, msgMIN             #Desplejar el mensaje si el caso no es exitoso
    
