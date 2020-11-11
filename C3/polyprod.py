#Crear una función que calcule el valor de f(x) en un punto, basado en el teorema fundamental del álgebra

#Definir la función
def poly(x,roots):
    p=1                         #Inicializamos la variable para almacenar valores de restas
    for r in range(len(roots)):
        p=p*(x-roots[r])        #Hacer cada resta y multiplicarla por la antrerior
    print(p)                    #Imprimir el valor del polinomio valuado
    
print('testing poly(1,[1j,-j])')
poly(1,[1j,-1j])
    
    
    
        
     
        