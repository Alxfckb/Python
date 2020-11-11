#Encontrar trios de caracteres

#Definir función
def count_substr(srt,subs):
    count=0       
    n=len(subs)                  #Inicializar contador
    for i in range(len(srt)-1): 
        if srt[i:n+i]==subs:        #Buscar trios iguales en cada trio adyacente de la cadena
            count+=1      
    
    print (count)                   #Imprimir cuántos tríos se encontraron
    
    
