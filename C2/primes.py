#Vamos a trabajar con una lista de números primos

#Definir la lista

n=[2,3,5,7,11,13]
#Recorrer la lista con un ciclo for
for i in range(len(n)):
    print(n[i]) #Imprimimps cada elemento de la lista
    
n.insert(6,17) #Añadimos un nuevo elemento a la lista de números primos
print(n) #imprimimos la nueva lista
