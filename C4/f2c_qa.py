#Hacer un programa interactivo que pida temperatura en Fahrenheit y convierta a celcius

import sys
#Pedir temperatura en ºF
f=float(input('Ingrese temperatura en  ºF '))

#Convertir ºF a ºC
C=5*(f-32)/9

#Imprimir el resultado
print('%s ºF  son %.2f ºC' %(f,C))
