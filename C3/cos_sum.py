#Hacer una tabla de aproximaciones de cos(x)
from math import cos, pi

#Definir la función que aproxima al coseno
def co(x,n):
    c=1                                 #Dar C0
    for i in range(1,n+1):
       c+=-c*(x**2)/((4*i**2)-(2*i))    #Calcular la sumatoria
    return c


#Función que imprime tabla de error entre co y cos(x)
def errorcos():
    #Listas con valores de x y n
    X=[4*pi,6*pi,8*pi,10*pi]
    n=[5,25,50,100,200]
    
    #Incializar lista de filas de la tabla
    p=[]
    
    #Insertar elementos a la lista 
    for i in range (len(X)):
          p.append([round(X[i],1)])
          
          #Calcular errores e insertarlos en las sublistas
          for j in range(len(n)):  
              error=cos(X[i])-co(X[i],n[j])
              p[i].insert(j+1,error)
    
    #Imprimir tabla
    print('x  ','         5     ', '    25     ',  '       50     ', '     100    ',  '     200 ')  
   
    for i in range(len(p)):
        for j in range(6):
            print('%1.5g' %p[i][j],end='      ')
        print()
        print()
           
        ∫s