#Calcular el área de un polígono

#Definir la función
def polygon_area(x,y):
    ind=[]                          #Inicializar lista de indices
    #Generar lista con índices 1,2,...,n,0 
    for i in range(len(x)):
        s=i+1                       #Generar índices desde 1 a n
        ind.append(s)               #Agregar los índices a la lista
        if s>len(x)-2:
            s=s-(len(x)-1)          #Generar el último índice
            ind.append(s)           #Agregar el índice a la lista
            break
    #Calcular el área
    XY=0                            #Inicializar la variable que almacenará los términos x0y1+x1y2+...
    YX=0                            #Inicializar la variable que almacenará x0y1+x1y2+...
    for j in range(len(x)):
        k=ind[j] 
        XY+=x[j]*y[k]               #Almacenar y sumar los términos x0y1+x1y2+...
        YX+=y[j]*x[k]               #Almacenar y sumar los términos x0y1+x1y2+...
    A=(1/2)*abs(XY-YX)              #Calcular el área
    return A

