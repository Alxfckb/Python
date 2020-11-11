#Deducir la fórmula para la regla del punto medio y probarla para las funciones probamos con trapezint

from math import sin, cos , pi
#Definir la función
def midpointint(f,a,b,n):
    h=(b-a)/n                   #Tamaño de las bases de los rectángulos
    s=0                         #Inicializar la variable donde se almacenan y suman las alturas de los rectángulos
    for i in range(n-1):
        s+=f(a+i*h+(1/2)*h)     #Sumar las alturas
    I=h*s                       #Calcular el área de los rectángulos 
    return I

def test_midpointint(arg):
     if arg=='test1':
         
        print('CON LA FUNCIÓN trapezint')
            
        print('Int(0,pi)cos x=',midpointint(cos,0,pi,1))
        print('error= %f' %abs(midpointint(cos,0,pi,1)-0))
        
        print()
        
        print('Int(0,pi/2)cos x=',midpointint(cos,0,pi/2,1))
        print('error=%f ' %abs(midpointint(cos,0,pi/2,1)-1))
        
        print()
        print('Int(0,pi)sin(x)=',midpointint(sin,0,pi,1))
        print('error=%f ' %abs(midpointint(sin,0,pi,1)-2))
        
        print()
        print('Int(0,pi/2)sin(x)=',midpointint(sin,0,pi/2,1))
        print('error=%f ' %abs(midpointint(sin,0,pi/2,1)-1))
        
        print()
    
     elif arg=='test10':
        
        print('CON LA FUNCIÓN trapezint')
            
        print('Int(0,pi)cos x=',midpointint(cos,0,pi,10))
        print('error= %f' %abs(midpointint(cos,0,pi,10)-0))
        
        print()
        
        print('Int(0,pi/2)cos x=',midpointint(cos,0,pi/2,10))
        print('error=%f ' %abs(midpointint(cos,0,pi/2,10)-1))
        
        print()
        print('Int(0,pi)sin(x)=',midpointint(sin,0,pi,10))
        print('error=%f ' %abs(midpointint(sin,0,pi,10)-2))
        
        print()
        print('Int(0,pi/2)sin(x)=',midpointint(sin,0,pi/2,10))
        print('error=%f ' %abs(midpointint(sin,0,pi/2,10)-1))
        
        print()

#Para n=1 el error es máximo con la regla del punto máximo