#Calcular el area de un triángulo arbitrario 

#Definir la función
def triangle_area(v1,v2,v3):
    l=[v1,v2,v3]                #Almacenar puntos en una lista
    x=[]                        #Inicializar lista que guarda coordenadas en x
    y=[]                        #Incializar lista que guarda coordenadas en y
    

    for i in range(3):
        x.append(l[i][0])       #Añadir valores de x a la lista x
        y.append(l[i][1])       #Añadir valores de y a la lista y
  
    for i in range(2):
        a=0                     
        a+=x[i]*(y[i+1]-y[2-i]) #Calcular los primeros  4 términos del área
    A=(1/2)*abs(a) + abs((1/2)*(x[2]*(y[0]-y[1]))) #Area completa
    return A
    
#Definir función test
def test_triangle_area():
    
    v1=[0,0]; v2=[1,0]; v3=[0,2]                #Seleccionamos vértices
    expected = 1                                #Valor esperado
    computed=triangle_area(v1,v2,v3)            #Valor calculado por la función
    tol =1E-14                                  #Tolerancia de diferencia entre el valor teórico y el calculado
    success = (expected-computed) < tol         #Caso exitoso
    msg= 'computed area=%g != %g (expected)' %\
        (computed,expected)                     #Caso no exitoso
    assert success, msg                         #Codición que evalúa success, en caso de ser falso, despliega el mensaje de caso no exitoso∫ 
    