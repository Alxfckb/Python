#Calcular la velocidad y aceleración de datos en 1D

#Definir la función
def kinematics(i,x,t):
    v=[]                                        #Inicializar lista que almacena velocidades
    a=[]                                        #Inicializar lista que almacena aceleraciones
    for n in range(1,i+1):
        dx=x[n+1]-x[n-1]                        #Calcular diferenciales de x para la velocidad
        dt=t[n+1]-t[n-1]                        #Calcular diferenciales de t para la velocidad
        
        ai1=(x[n+1]-x[n])/(t[n+1]-t[n])         #Términos de para calcular la aceleración
        ai2=(x[n]-x[n-1])/(t[n]-t[n-1])
        
        V=dx/dt                                 #Calcular velocidad
        A=2*((dt)**(-1))*(ai1-ai2)              #Calcular aceleración
        v.append(V)                             #Almacenar velocidades en la lista v
        a.append(A)                             #Almacenar aceleraciones en lista a
    
    return v , a


#Definir función test
def test_kinematics():
    t=[0,0.5,1.5,2.2]                           #Definimos lista de prueba
    V=10                                        #Definimos velocidad
    x=[V*tt for tt in t]                        #Generamos valores de x
    tol = 1E-14                                 #Definimos la tolerancia de la prueba
    expected = 10                               #Valor teórico de las velocidades
    
    for i in range(2):        
        computed = kinematics(2,x,t)[0][i]      #Extraer valores de la función kinematics
        success  = expected-computed < tol      #Caso exitoso
        
    msg      = '(computed) %g != %g (expected)' %\
        (computed,expected)                     #Mensaje para caso exitoso
    assert success, msg                         #Mensaje al detectar caso no exitoso
    
    
    
#El programa no funciona para valores mayores al valor maximo de i porque no existen elementos con ese índice en nuestras listas
#Para valores menores, simplemente imprime los primeros i valores

