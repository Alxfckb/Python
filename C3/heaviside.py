#Implementar la función Heaviside

#Definir la función
def H(x):
    
    if x<0:
        return 0
    if x>=0:
        return 1

#Definir función test y probarla en los casos que pide el libro
def test_H():
    assert H(-10)==0
    assert H(-10E-15)==0
    assert H(0)==1
    assert H(1E-15)==1
    assert H(10)==1
    