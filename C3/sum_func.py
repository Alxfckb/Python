#Hacer una función que sume 1/k 1<=k<=M

#Definir la función
def Sum(m):
    s=0                    #Inicializar variable que almacena sumas
    for i in range(m):   
        s+=1/(i+1)         #Efectuar y almacenar suma 
    return s           
  
    
#Definir función de testeo 
def test_sum_1k():
    tol = 0.0001                     #Declaramos un tolerancia ridículamente pequeña
    assert abs(Sum(3)-1.83333) < tol   #Hacemos el test 

