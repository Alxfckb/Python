#Programa que devuelve números impares

#Inicializamos la variable n, el iterador i y k que será el número impar
n=int(input('ingrese un número entero'))
i=0
k=0
#Escribimos el ciclo while que utilizaremos
while (k < n-1):
    k = 2*i + 1 #generamos números impares
    i=i+1 #aumentamos a i en una unidad
    print(k) #imprimimos el número impar