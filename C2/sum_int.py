#Este programa va a sumar n enteros luego vamos a comparar esto con la fórmula de gauss

#Pedimos un número entero que será el límite superior de la suma
n=int(input('Ingrese un número entero '))
#inicializamos el iterador
i=0
#inicializamos la variable donde almacenaremos la suma
s=0

#implementamos ciclo while
while(i <= n):
    s = s + i #hacemos la suma
    i=i+1
    
print(s)  #imprimimos el resultado final
G = n*(n+1)//2 #Esta operación da el valor de la sumatoria por la fórmula de Gauss
print('G =',G) #imprimirmos el valor de la suma por Gauss

