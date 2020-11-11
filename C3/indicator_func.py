#Implementar una función indicadora
from heaviside import H 
#Definir la función
def I(x,L,R):
    if L<=x<=R:
        return 1
    else:
        return 0

#Hacer implementación en términos de la función Heaviside
def I2(x,L,R):
    I=H(x-L)*H(R-x)
    return I

#Definir función test
def test_I():
    L=2
    R=4
    x1=1
    x2=2
    x3=(L+R)/2
    x4=R
    x5=5

#Probar distintos valores en ambas funciones
    assert I(x1,L,R)==I2(x1,L,R)==0
    assert I(x2,L,R)==I2(x2,L,R)==1
    assert I(x3,L,R)==I2(x3,L,R)==1
    assert I(x4,L,R)==I2(x4,L,R)==1
    assert I(x5,L,R)==I2(x5,L,R)==0
    