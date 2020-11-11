#Encontrar pares de caracteres

#Definir función
def count_pairs(dna,pair):
    count=0                         #Inicializar contador
    for i in range(len(dna)-1): 
        if dna[i:2+i]==pair:        #Buscar pares iguales en cada par adyacente de la cadena
            count+=1                #Contar pares encontrados
    print (count)                   #Imprimir cuántos pares se encontraron
