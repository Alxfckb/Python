#Método 1
s = 0
k = 1
M = 100
while (k<=M): #La sumatoria termina realmente en 100
    s+=1/k #k no estaba cambiando y siempre era menor a 100, entocnes el ciclo nunca acaba
    k=k+1
print('M=100--->','%.3f'%s)

#Método 2
M=3
k=1
s=0
while (k<=M):
    s+=1/k
    print ('M=',k,'%.3f'%s) 
    k+=1