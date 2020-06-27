#Este programa calcula el interés simple de un capital inicial de 1000$ durante 3 años al 5%

#Definir el capital inicial
A=1000

#Definir el periodo de tiempo en años
n=3

#Definir el porcentaje de interes
p=5

#Definir la ecuación de interes simple
cf= A * (1 + p/100)** n

#Calcular el crecimiento del capital inicial
g=cf-A

#imprimir el capital final
print('El crecimiento que tienen', A , '$ en ', n , 'años es  %3.2f' %g, '$' )

