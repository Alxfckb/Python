#Importar la función ln de math
from math import log, pi 

#Definir cada constante
M=67 #g
p= 1.038 #g/cm^3
c=3.7 #g^-1 K^-1
K= 5.4*10**(-3) #W cm^-1 K-1
Tw=100 #K
To=4#K
To2=20 #K
Ty=70#K

#No es necesario pasar de ºC a K porque es una relación lineal y el cociente dentro del ln es adimensional

#calcular los tiempos de cocción
t = (((M**(2/3))*c*p**(1/3)) / ((K*(pi**2))*(4*pi/3)**(2/3)) )* log(0.76 * (To-Tw)/(Ty-Tw))

t2 = (((M**(2/3))*c*p**(1/3)) / ((K*(pi**2))*(4*pi/3)**(2/3)) )* log(0.76 * (To2-Tw)/(Ty-Tw))
#imprimir los tiempos de cocción

print('El tiempo de cocción de un huevo  a 4ºC es t= %3.2f' %t,'s')
print ('El tiempo de cocción de un huevo a 20ºC es t2= %3.2f ' %t2, 's') 