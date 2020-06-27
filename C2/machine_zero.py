eps = 1.0  #Se inicializa eps

while (1.0 != 1.0 + eps):  #Se pide repetir el ciclo hasta que 1.0 sea distinto de 1.0+eps
     
    print('........',eps)  #Se imprime eps
    eps = eps/2.0           #eps se dive entre 2 y se almacena su nuevo valor
        
print('final eps:',eps)    #Se imprime el último valor que tomó eps

#Sí, eps=1.1102230246251565e-16 funciona igual a tener el último valor de eps=0 
