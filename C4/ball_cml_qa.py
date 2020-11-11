#Programa de caida libre que pide v0 y t al usuario
#Importar sys

import sys

try:
    v0=float(sys.argv[1])
    
#Caso en el que el usuario no da valores a v0  
except IndexError:
    print('Se esperaban valores para v0 en terminal')
    v0=float(input('Ingrese v0: '))
    
try: 
    t=float(sys.argv[2])
#Caso en el que el usuario no da valores para t
except IndexError:
    print('Se esperaban valores para t en terminal')
    t=float(input('Ingrese t: '))


g=9.81

#Calcular la posición
y=v0*t - 0.5*g*t**2

print(round(y,2))


