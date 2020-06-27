#Tabla de conversión de Fahrenheit-Celcius con F=1,10,20,...,100
#Queremos una función que tome valores en ºF y nos de el equivalente en ºC

#Inicializamos F
F=0
#Implementamos ciclo while 
while (F<100): 
    
   C=5*(F-32)/9 #Conversión de ºF a ºC
   F=F+10 #Aumentamos a F en 10 unidades cada vez que se repita esta línea 
   print(F,'ºF------> %3.2f '%C,'ºC')