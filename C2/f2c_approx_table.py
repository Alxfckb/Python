#Tabla de conversión de Fahrenheit-Celcius con F=1,10,20,...,100
#Queremos una función que tome valores en ºF y nos de el equivalente en ºC

#Inicializamos F
F=0
#Implementamos ciclo while 
print('F      ','C   ','   C^')
while (F<=100):     
   C=5*(F-32)/9                              #Conversión de ºF a ºC
   C2 = (F-30)/2                             #Conversión aproximada 
   print(F,' %3.2f '%C, ' %3.2f' %C2)        #Imprimir
   F=F+10 


