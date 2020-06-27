#Este programa va a calcular la aproximación de la función escalón por series de Fourier para n=1,2,3,4
#Con T=2pi y para alphas distintos

#Importar sin y pi de math e importar sys para leer datos en terminal
from math import sin, pi
import sys

#Pedir t,a,T en terminal
t= float(sys.argv[1])*pi
T= float(sys.argv[2])*pi
a= float(sys.argv[3])

a2=1/4
T=2*pi
#Para S(alphaT;n) n=1, alpha=0.01 y T=2pi
s=4.00/pi * (1/((2*1)-1)) * sin((2*(2-1)*pi*a*t)/T)
print(s)

#Para S(alphaT;n) n=2, alpha= 0.01 y T=2pi
s = s + 4.00/pi * (1/((2*2)-1)) * sin((2*((2*2)-1)*pi*a*t)/T)
print (s)

#Para S(alphaT;n) n=3, alpha= 0.01 y T=2pi
s = s + 4.00/pi * (1/((2*3)-1)) * sin((2*((2*3)-1)*pi*a*t)/T)
print(s)

#Para S(alphaT;n) n=4, alpha= 0.01 y T=2pi
s = s + 4.00/pi * (1/((2*4)-1)) * sin((2*((2*4)-1)*pi*a*t)/T)
print(s)

#Con a=0.01 obtuvimos s=0.3156105797446717 mientras con a=0.25 tuvimos s=0.9215829085702131