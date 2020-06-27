#Tabla de y(t) vs t

#Definir las constantes
g=9.8 #m/s^2

#Pedir el valor de la velocidad incial
v=float(input('Ingrese la velocidad inicial ' ))

#Pedir el número de intervalos que se desean
n=int(input('Ingrese el número de intervalos que se desean '))

#Definir el tamaño de cada intervalo de tiempo
t=(2*v/g)/n

#Incializar la variable donde se almacenarán los tiempos
dT=0

print('   t','  y(t)')

#Generar los valores con un ciclo for
for i in range(n+1):
    dT=t*i                       #Generar cada instante de tiempo
    y=v*dT-(1/2)*g*dT**2         #Calcular la posición
    print('%5.1f %5.1f'  %(dT,y))    #Imprimir t vs y(t)

print()
print()
#b) hacer lo mismo pero con un loop while

#Reiniciamos i
i=0
print('   t','  y(t)')
#dentro del while hacemos lo mismo que en el for
while (dT<=2*v/g): 
       y=v*dT-(1/2)*g*dT**2 
       print('%5.1f %5.1f'  %(dT,y))
       dT=t*i
       i=i+1

