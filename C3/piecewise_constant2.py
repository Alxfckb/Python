#Aplicar funciones indicadoras
from indicator_func import I

#Definir función
def f(x,data):
    X=[]
    V=[]
    for i in range(len(data)):
        X.append(data[i][0])
        V.append(data[i][1])

    for j in range(len(X)-1):
        f=V[j]*I(x,X[j],X[j+1])   
    return f



