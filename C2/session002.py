# asigno elementos a la lista numeros
numeros = [5,4,3,2,1,0]

'''
# ciclo para imprimir elementos de la lista numeros
for i in range(6):
    print("numeros[", i,"] = ", numeros[i])
print()
# ciclo while para imprimir elementos de la lista numeros
i = 0
while (i < 6):
    print("numeros[", i,"] = ", numeros[i])
    i += 1
print()
i = 0
while (i <= 5):
    print("numeros[", i,"] = ", numeros[i])
    i += 1


# Implementando un vector en 8D como una lista
vector1 = [1,4,0,6,3.4,1,6.5,10.2]
vector2 = [12,24,34,654,23,6,92,1.7]

# implementando el producto punto entre dos vectores en 8D
productoPunto = 0
for i in range(8):
    # hacer el producto de las componentes vector1_i y vector2_i
    productoI = vector1[i]*vector2[i]
    print(productoI)

    # sumar todos los productos
    productoPunto = productoPunto + productoI

print()
print(productoPunto)
'''

# Implementando una matrix
identidad = [[1,0,0],[0,1,0],[0,0,1]]


for i in range(3):
    print(identidad[i])

# Implementando listas de listas
pauli = [[[0, 1], [1, 0]], [[0, (-1j)], [1j, 0]], [[1, 0], [0, -1]]]


matrizDePrueba = [[1,2,3],[4,5,6],[7,8,9]]

resultado = [[0,0,0],[0,0,0],[0,0,0]]
for i in range(3):
    for j in range(3):
        for k in range(3):
            resultado[i][j] = resultado[i][j] + matrizDePrueba[i][k]*identidad[k][j]


for i in range(3):
    print(resultado[i])

print()
print()
nombres = ["Sarceño", "Juan", "Alex", "Subadra", "Chen", "Chepi"]
 
for elemento in nombres:
    print(elemento)

print()
print()

for i in range(6):
    print(nombres[i])