#Kronecker intento 2

m1=[[1,2],[3,4]]
m2=[[0,5],[6,7]]
v=[1,2,3]
l= [5 * m2[i][j] for i in range(2) for j in range(2)]


kron=[[[],[]],[[],[]]]
for i in range(2):
    for j in range(2):
                kron[i][j] = [ m1[i][j] * m2[l][k] for l in range(2) for k in range(2)]

for i in range(2):
        print(kron[i])
        