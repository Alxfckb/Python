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
T=0

#inicializar la listas para almacenar t y y
vt=[]
vy=[]

#Generar los valores con un loop for
for i in range(n+1):
    
    T=(t*i)                          #Generar cada instante d tiempo
    y=(v*T-(1/2)*g*T**2)             #Calcular la posición
    vt.insert(i,round(T,3)) 
    vy.insert(i,round(y,3)) 
    
print('   t','  y(t)')
for i in range(n+1):
    print('%5.1f %5.1f' %(vt[i],vy[i]))
