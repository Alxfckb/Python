#Hacer una función que integre por el método del trapecio

#Importar cos, sin y pi
from math import sin, cos, pi

#Definir la función
def trapezint(f,a,b):
    I=((b-a)/2)*(f(a)+f(b))         #Escribir la fórmula de la aproximación
    return I                        #Imprimir el valor de la aproximación

'''
#Pruebas con trapezint
print('CON LA FUNCIÓN trapezint')
    
print('Int(0,pi)cos x=',trapezint(cos,0,pi))
print('error= %f' %abs(trapezint(cos,0,pi)-0))

print()

print('Int(0,pi/2)cos x=',trapezint(cos,0,pi/2))
print('error=%f ' %abs(trapezint(cos,0,pi/2)-1))

print()
print('Int(0,pi)sin(x)=',trapezint(sin,0,pi))
print('error=%f ' %abs(trapezint(sin,0,pi)-2))

print()
print('Int(0,pi/2)sin(x)=',trapezint(sin,0,pi/2))
print('error=%f ' %abs(trapezint(sin,0,pi/2)-1))

print()
'''

#b) Hacer otra función con el método del trapecio, esta vez con dos trapezoides

#Definir la función
def trapezint2(f,a,b):
    p=(b-a)/2                       #Tamaño de cada intervalo
    I=(p/2)*(f(a)+f(b)+2*f(a+p))    #Aproximación de la integral
    return I

#Pruebas con trapezint2
'''
print('CON LA FUNCIÓN trapezint2')

print('Int(0,pi)cos x=',trapezint2(cos,0,pi))
print('error= %f' %abs(trapezint2(cos,0,pi)-0))

print()

print('Int(0,pi/2)cos x=',trapezint2(cos,0,pi/2))
print('error=%f ' %abs(trapezint2(cos,0,pi/2)-1))

print()
print('Int(0,pi)sin(x)=',trapezint2(sin,0,pi))
print('error=%f ' %abs(trapezint2(sin,0,pi)-2))

print()
print('Int(0,pi/2)sin(x)=',trapezint2(sin,0,pi/2))
print('error=%f ' %abs(trapezint2(sin,0,pi/2)-1))

#d)Implementar la aproximación con n trapezoides
'''
#Definir la función
def trapezint(f,a,b,n):
    p=(b-a)/n                   #Tamaño de cada intervalo
    sm=0                        #Inicializar la variable que almacena las sumas
    for i in range(n-1):
        sm+=f(a+(i+1)*p)        #Hacer las sumas del término f(x_i)    
    I=(p/2)*(f(a)+f(b))+p*sm    #Ensamblar toda la integral
    return I

#e)Escribir una función de prueba para probar la función trapezint()

#Definir la función
def test_trapezint():
    print('Int(0,2pi)cos(x)=',trapezint(cos,0,2*pi,5))
    print('Error=',abs(0-trapezint(cos,0,2*pi,5)))
    
    
    

    
        
        
        