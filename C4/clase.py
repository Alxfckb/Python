#Función 1

def read_file(file):      #Definimos la función que lee archvios

    T=[]
    L=[]
    
    #Abrir el archivo en modo leer
    infile=open(file,'r')                    

    #Almacenamos el valor de v0 
    v0=float(infile.readline().split()[1] )           

    #Leer el resto de líneas y almacenar los valores
    for line in infile.readlines():
        L.append(line)
        
    #Cerrar el archivo
    infile.close()     
    
    #Almacenar los valores t en una lista
    for element in L[1:]:
        for t in element.split():
            T.append(float(t))
            
    #Retornar v0 y la lista con valores T
    return v0, T

#Función 2
def write_file():
    g=9.8
    
    #Almacenar los datos de la función 1
    v0=read_file('balldat.txt')[0]
    t=read_file('balldat.txt')[1]
    
    #Ordenar los elementos t de forma ascendente
    T=sorted(t,key=float)
    
    #Calcular y almacenar los valores de y
    Y=[]                                            #Inicializar lista de valores y
    for i in range(len(T)):
        y = v0*T[i]-0.5*g*T[i]**2
        Y.append(y)
        
    #Crear el archivo de texto    
    outfile=open('new_file.txt','w')
     
    outfile.write('   t   ' + '    y    ' + '\n')       #Encabezado
    
    #Imprimir columnas
    for i in range(len(T)):
        outfile.write('%.5f  %.5f' %(T[i] ,Y[i])+'\n')
        
    #Cerrar el archivo de texto 
    outfile.close()
   
 
    
    
    
    
    
    











    