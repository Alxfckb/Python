#Generar n+1 coordenadas igualmente espaciadas en un intervalo [a,b]
#Pedir lÃ­mites del intervalo
a=int(input('Ingrese el limite inferior del intervalo '))
b=int(input('Ingrese el limite superior del intervalo '))
n=int(input('el número de intervalos que desea '))

#Calcular la longitud de cada coordenada
h=(b-a)/n

#inicializar el iterador
i=0

#inicializar una lista
l=[]

#Generar coordenadas con un ciclo for
for i in range(n+1):
    x=a+h*i             #Generar cada punto
    l.insert(i,x)       #agragar cada punto a la lista
print(l)                #Imprimir
   
#List comprehension method 
 
#Generar lista con los puntos x_i, generados con un loop interno
l2=[a+h*i for i in range(n+1)]

print(l2)