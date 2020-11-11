#Escribir una función dada la función test

#a)

def halve(x):
    if type(x)==float:
        return x/2.0
    elif type(x)==int:
        return int(x/2)
    
def test_halve():
    assert halve(5.0) == 2.5 # Real number division 
    assert halve(5) == 2 # Integer division
    
#b)
def add(a,b):
    return a+b

def test_add():
# Test integers
    assert add(1, 2) == 3
# Test floating-point numbers with rounding error
    tol = 1E-14
    a=0.1; b=0.2
    computed = add(a, b)
    expected = 0.3
    assert abs(expected - computed) < tol
# Test lists
    assert add([1,4], [4,7]) == [1,4,4,7]
    # Test strings
    assert add('Hello, ', 'World!') == 'Hello, World!'
    
def equal(a,b):
    if a==b:
        return  True, a
    elif len(a)==len(b) and a!=b:
        
        for i in range(1,len(a)):
            if a[:i]!=b[:i]:
                break
        return False, str(a[:i]+'|'+b[i-1:])
        
    elif len(a)!=len(b):
        for i in range(1,len(a)):
            if a[:i]!=b[:i]:
                break
        return False, str(a[:i]+'|'+b[i-1:-1]+'*|'+b[i+1:])
    elif len(a.split())==len(b.split()):
        

def test_equal():
    assert equal('abc', 'abc') == (True, 'abc')
    
    assert equal('abc', 'aBc') == (False, 'ab|Bc') 
                                   
    assert equal('abc', 'aBcd') == (False, 'ab|Bc*|d') 
    
    assert equal('Hello, World!', 'hello world') == \
        (False, 'H|hello,|  |wW|oo|rr|ll|dd|*!|*')
    
        
        
        