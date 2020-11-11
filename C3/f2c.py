#Este programa convierte de ºF a ºC y de ºC a ºF

#Función de ºF a ºC
def C(f):
    c=(f-32)*(5/9)         #Convertir a ºC
    return c               #Imprimir la conversión

#Función de ºC a ºF-
def F(c):                       #Definir la función
    f= (9/5)*c + 32             #Convertir a ºF
    return f

'''
#Imprimir 
print('F(C(23)=',F(C(23)))
print('C(F(5)=',C(F(5)))
'''