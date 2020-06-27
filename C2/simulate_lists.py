a = [1,3,5,7,11]
b = [13,17]
c = a + b #Esta línea une las dos listas anteriores
print(c)

b[0] = -1 #cambiamos el primer elemento de la lista b por -1 

d = [e+1 for e in a] #Crea una lista con elementos de a aumentados en una unidad

d.append(b[0] + 1) #Aumentamos en una unidad el primer elemento de b y lo añadimos a la lista d

d.append(b[-1] + 1)#Aumentamos en una unidad el último elemento de b y lo añadimos a la lista d

print (d[-2])#imprimimos el penúltimo elemento de d

print()

for e1 in a:
    for e2 in b:
        print(e1+e2) #sumamos todos los elementos de a con todos los de b y luego se imprime cada suma
