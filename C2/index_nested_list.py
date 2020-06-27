q = [["a",'b','c'],['d','e','f'],['g','h']]     #Definir la lista

#a) 

#extraer la letra a

print(q[0][0])

#extraer l lista ['d','e','f']

print(q[1])

#Extraer h
print(q[-1][-1])

#extraer la letra d
print(q[1][0])
#explicar por qué q[-1][-2] tiene valor g
print(q[-1][-2]) #Nos devuelve g porque este es el penúltimo valor de la última lista

#b) qué tipo de objetos son i y j?
for i in q:
    for j in range(len(i)):
        print(i[j])
#i es una lista y j un número entero