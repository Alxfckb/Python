#Calcular la longitud de una trayectoria
from math import sqrt
#Definir la función
def pathlength(x,y):
                         
    l=0
    if len(x)!=len(y):
        print('El número de elementos de x debe ser igual al de y')
    else:             
        for i in range(len(x)-1):
            X=(x[i+1]-x[i])**2     #Calcular la diferencia entre valores de x y elevar al cuadrado
            Y=(y[i+1]-y[i])**2     #Calcular la diferencia entre valores de u y elevar al cuadrado
            l+=sqrt((X+Y))         #Almacenar las sumas de los cuadrados 
        return l       #Devolver la longitud de la trayectoria
    
    
#Definir la función test

def test_pathlength():
    x=[0,1,2]
    y=[0,2,2]
    tol=1E-14
    expected = sqrt(6)
    computed = pathlength(x,y)
    success  = abs(expected-computed) < tol
    msg='computed length =%g != %g (expected)' % \
                (computed,expected)
    assert success,msg
    