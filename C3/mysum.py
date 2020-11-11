#Crear una función que funcione como la función sum()

#Definimos la función
def mysum(arg):  
    
    for i in range(len(arg)):  
             
        if type(arg[i])==list :                 #Condición para elementos de tipo list
            sm=[]                               #Inicializar variable para almacenar elementos concatenados
            for j in range(len(arg)):
                read=arg[j]                     #Leer argumentos
                sm=sm+read                      #Concatenar
        
        if type(arg[i])==str:                   #Condición para elementos de tipo string
            sm=''                               #Inicialiazar variable para almacenar elementos concatenados
    
            for j in range(len(arg)):
                read=arg[j]                     #Leer argumentos
                sm=sm+read   
                   #Concatenar
        else:                                   #Condición para otro tipo de elementos
            sm=0                                #Inicializar variable para almacenar elementos concatenados
            for j in range(len(arg)):
                read=arg[j]                     #Leer argumentos
                sm=sm+read                      #Concatenar
        
            
                
    print(sm)                                   #Imprimir el resultado
    
               
            
            