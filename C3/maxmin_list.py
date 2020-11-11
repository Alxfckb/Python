#Encontrar máximos en un lista
def mymax(a):  
    mmx=a[0]                                #Fijar el primer máximo como el primer elemento de la lista a
#Encontrar y almacenar máximos no globales hasta encontrar el global   
    for i in range(len(a)-1):
        if mmx<=a[i+1:][0]:                     
            mmx=a[i+1:][0]                  # reemplaza y almacena los máximos que encuentra
    return mmx


def mymin(a):                   
    mnx=a[0]                                #Fijar el primer mínimo como el pimer elemento de a
#Encontrar y almacenar mínimos no globales hasta encontrar el global
    for i in range(len(a)-1):
        if mnx>=a[i+1:][0]:
            mnx=a[i+1:][0]                  #Reemplazar y almacenar los mínimos que encuentra
    return mnx
    


