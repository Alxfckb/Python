from math import sqrt            # Importamos la función de raiz cuadrada
for n in range(1,60):
    r=2.0                        # Se define r
    for i in range(n):
        r=sqrt(r)                # Se saca la raiz de r 60 veces y se almacena   
    for i in range(n):           ##Esta línea contiene el error
        r=r**2                   # Se eleva r al cuadrado 60 veces y se amacena
    print('%d times sqrt and **2: %.16f'  %(n,r)) #Se imprime el resultado cada vez que se saca la raíz y se eleva al cuadrado
    
#Se cambia de 2.0 1 1.99