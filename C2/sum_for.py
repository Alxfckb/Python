#Inicializamos nuestras variables
s = 0
k = 1
M = 100
for i in range(100): #diseñamos el ciclo for
     i=i+1  #cambiamos el valor de i para no dividir entre 0
     s+=1/i # almacenamos cada suma
print('M=100--->','%.3f'%s) #imprimimos el resultado final
