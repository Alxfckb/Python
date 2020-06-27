#Alex Alvarado
#Queremos el producto de Kronecker entre dos matrices arbitrarias

#Eligiendo dos matrices arbitrarias de 2x2 
m1=[[1,2],[3,4]]
m2=[[0,5],[6,7]]

#Inicializando el producto de Kronecker (kron)
kron=[ [ [[0,0],[0,0]],[[0,0],[0,0]] ] , [ [[0,0],[0,0]] , [[0,0],[0,0]]] ]

#Definir el producto de kronecker
                
for i in range(2):
    for j in range(2):
        for k in range(2):
            for n in range(2):
                kron[i][j][k][n] = m1[i][j] * m2[k][n] #Esto se justificará en otro archivo
for i in range(2):
    print(kron[i])
