#Generar valores de los niveles de energía en un átomo
#parte a 
#Definir las constantes
m = 9.1094*10**(-31) #kg

e = 1.6022*10**(-19) #C

ep = 8.8542*10**(-12) #C^2s^2kg^-1m^-3

h = 6.6261*10**(-34) #Js

#inicializamos n
n=1

E1 = - m*e**4/((8*ep**2)* h**2) #Parte constante de la energía
print('n ', ' E ')

while(n <= 20): #Usamos un ciclo while
    E = 1/n**2 #Calculamos la parte variable de la energía
    Et = E1*E
    print(n , '%.3g'%Et) #Imprimir el valor de la energía
    n = n+1 
   
print()

#Parte b) 
#Inicializamos la matriz l
l=[ [0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0] ]

#Usar ciclo for para calcular delta E y asignarlo a la celda correspondiente
for i in range(5):
    for j in range(5):
        
        D= '%.3g'%(E1/(i+1)**2 - E1/(j+1)**2) #Hacemos el calculo de delta E
        
        l[i][j]=D #Asignar valores celdas

#imprimir la matriz l
for i in range(5):
    print (l[i])