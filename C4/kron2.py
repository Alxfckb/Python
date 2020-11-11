#Función general que calcula el producto de Kronecker

def escal(x,y):
    if type(x)==float or type(x)==int:
        esy=[]
        for i in range(len(y)):
            for j in range(len(y[i])):
                esy.append(x*y[i][j])
        return esy
    
    
    
def kron(A,B):
#Extraer dimensiones de las matrices    
    m=len(A);       p=len(B)
    n=len(A[1]);    q=len(B[1])
    
    #Inicializar matriz de kronecker
    l=[]
    k=[]
    
    for row in A:
        for a in row:
            
            l.append(escal(a,B))
   
    L=[ [l[i][:q],l[i][q:]] for i in range(len(l))]       
    return L


