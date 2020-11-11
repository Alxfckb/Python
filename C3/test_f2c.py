#Vamos a crear una función de prueba que chequea F(C(f))=f y C(F(c))=c
import f2c as fc
#Definir la función 

def test_F_C(f,c): 
    
    a=round(fc.F(fc.C(f)),2)  
    b=round(fc.C(fc.F(c)),2)
    print(a,b)
    if a==f and b==c:
        print('cifunciona')
    else:
        print('no funciona')

test_F_C(f=2, c=3)

