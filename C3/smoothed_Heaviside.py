#Implementar la versión suave de la función Heaviside
from math import sin,pi

#Definir la función
def H_eps(x,eps=0.01):
    if x<-eps:
        return 0
    if -eps<=x<=eps:
        return 1/2 + x/(2*eps)+ sin(pi*x/eps)/(2*pi)
    if x>eps:
        return 1
    
#Definir función test
def test_H_eps():
    x1=-0.02
    x2=-0.01
    x3=0
    x4=0.01
    x5=1
    #Probar que H_eps(x) funcione
    assert H_eps(x1) == 0
    assert H_eps(x2) == 1/2 + x2/(2*0.01)+ sin(pi*x2/0.01)/(2*pi)
    assert H_eps(x3) == 1/2
    assert H_eps(x4) == 1/2 + x4/(2*0.01)+ sin(pi*x4/0.01)/(2*pi)
    assert H_eps(x5) == 1