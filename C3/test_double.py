#Escribimos la función que nos piden
def double(l):
    return l*2

def test_double(l):
    assert double(2) == 4
    assert abs(double(0.1) - 0.2) < 1E-15 
    assert double([1, 2]) == [1, 2, 1, 2] 
    assert double((1, 2)) == (1, 2, 1, 2) 
    assert double(3+4j) == 6+8j
    assert double('hello') == 'hellohello'
