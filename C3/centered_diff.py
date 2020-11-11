#Escribir una función para diferenciación numérica
from math import exp, log, cos, pi
#a) Función que devuelva la aproximación f'(x)=(f(x+h)-f(x-h))/2h

#Definir la función 
def diff(f,x,h=1E-5):
    df=(f(x+h)-f(x-h))/(2*h)     #Calcular la derivada
    return df

#Definimos la función cuadrática
def quad(x):
    q=2*x**2+3*x+2
    return q

#Definimos la función exp(-2x^2)
def exp2(x):
    e=exp(-2*x**2)
    return e

#Definir función test
def test_diff():
    x=5                             #x de prueba
    f=quad()                        #f de prueba
    tol=1E-9                        #Tolerancia
    expected = 23                   #Valor teórico de la derivada en x=4
    computed = diff(f,x)            #Valor obtenido con la función diff
    success  = abs(expected-computed) < tol         #Caso exitoso
    msg      = '(computed) %g != %g (expected)' %\
        (computed,expected)         #Mensaje para caso exitoso
    assert success, msg             #Desplejar el mensaje si el caso no es exitoso
    

#definir la función application
def application():
    #Para e^x en x=0
    print('e^x,x=0')
    e=diff(exp,0,h=0.01)
    error1=abs(e-1)
    print('df/dx=',e,'error=',error1)
    print()
    
    #Para cos(x) en x=2pi
    print('cos(x),x=2pi')
    e2=diff(cos,2*pi,h=0.01)
    error2=abs(e2-0)
    print('df/dx=',e2,'error=',error2)
    print()
    
    #Para ln(x) en x=1
    print('ln(x),x=1')
    e3=diff(log,1,h=0.01)
    error3=abs(e3-1)
    print('df/dx=',e3,'error=',error3)
    print()   
    
    print('e^(-2x^2),x=2pi')
    e4=diff(exp2,0,h=0.01)
    error4=abs(e4-0)
    print('df/dx=',e4,'error=',error4)
    print()
    
    