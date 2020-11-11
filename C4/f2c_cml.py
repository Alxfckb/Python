import sys
#Pedir temperatura en ºF
f=float(sys.argv[1])

#Convertir ºF a ºC
C=5*(f-32)/9

#Imprimir el resultado
print('%s ºF son %.2f ºC' %(f,C))
