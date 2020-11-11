#Implementar la función factorial

#Definir la función
def fact(n):
    f=1                  #Inicializar la variable que almacena n!
    for i in range(n):
        if f>0:
            f*=n-i       #Calcular n!
        if n==0 or n==1: #Caso para n=0 y n=1
            f=1      
    return f

def test_fact():
# Check an arbitrary case 
    n=4
    expected = 4*3*2*1
    computed = fact(n)
    assert computed == expected # Check the special cases 
    assert fact(0) == 1
    assert fact(1) == 1            