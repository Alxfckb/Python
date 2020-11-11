#Encontrar el error en un programa
'''
def f(x,m,n,r,s):
    return expsin(x,r,m)+expsin(x,s,n)

x=2.5
print(f,x,0.1,0.2,1,1)

from math import exp, sin
def expsin(x, p, q):
    return exp(p*x)*sin(q*x)


Error 1: importar funciones después de hacerlas usado en el código
Error 2: definir expsin después de haberla usado
'''
#Código corregido 

from math import exp, sin
def expsin(x, p, q):
    return exp(p*x)*sin(q*x)

def f(x,m,n,r,s):
    v=expsin(x,r,m)+expsin(x,s,n)
    return v

x=2.5
print (f(x,0.1,0.2,1,1))
