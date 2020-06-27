#Tabla de conversión de Fahrenheit-Celcius con F=1,10,20,...,100
#Queremos una función que tome valores en ºF y nos de el equivalente en ºC


f=0                     #Temperatura inicial en ºF       

L=[]

F=[]                    #lista que almacena valores de F

C=[]                    #lista que almacena valores de C

C2=[]                    #lista que almacena valores de C^

#Implementamos ciclo while 
while (f<=100): 
   c=5*(f-32)/9                              #Conversión de ºF a ºC
   c2 = (f-30)/2                             #Conversión aproximada 
   F.append(f)
   C.append(round(c,2))
   C2.append(round(c2,2))
   f=f+10 

L.append(F)
L.append(C)
L.append(C2)

print('F|','| C     |','C^')
for j in range(11):
        print(L[0][j],'|' ,L[1][j],'|',L[2][j])
        