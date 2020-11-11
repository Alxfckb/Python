#Debuguear una función de prueba dada

def triple(x):
    return x+x*2

def test_tripple():   
    assert triple(3)==9
    assert round(triple(0.1),2) == 0.3
    assert triple([1,2])==[1,2,1,2,1,2]
    assert triple('hello')=='hellohellohello'


'''
def test_triple(x):  #No debe tener argumento
    assert triple(3)==9 
    assert triple(0.1)==0.3,     Error por aproximación
    assert triple([1,2])==[1,2,1,2,1,2]
    assert triple('hello')=='hello hello 2' Error, 'hello'*2 devuelve hellohello y si le sumamos 'hello' , tenemos 'hellohellohello'
'''