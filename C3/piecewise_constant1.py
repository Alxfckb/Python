#Implementar una función por trozos

#Definir la función
def piecewise(x,data):
    
    xlist=[]                            #Inicializar lista de x
    vlist=[]                            #Inicializar lista de v
    
    for i in range(len(data)):
        xlist.append(data[i][0])        #Agregar coordenadas x de data a la lista de x
        vlist.append(data[i][1])        #Agregar coordenadas v de data a la lista de v
        
    for i in range(len(data)) :
        if xlist[i]<=x< xlist[i+1]:     #Asignar valor a f(x) según el punto donde pida el usuario 
            return vlist[i]
        
#Definir función test
def test_piecewise():
      
    x1=2.9999   
    x2=1E-15
    x3=1.9999999
    data=[[0,1],[1,2],[2,3],[3,4]]                                                      
    #Pruebas con distintos valores de x                                 
    assert piecewise(x1,data)==3
    assert piecewise(x2,data)==1
    assert piecewise(x3,data)==2
   
        
    
    
    
    
    