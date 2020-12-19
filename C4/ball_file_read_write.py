#Programa que evalua datos de una hoja 


#a)


def read_data(myfile):
    
    '''
    Esta función lee datos de una hoja 'archivo.txt'
    y extrae el primer valor de la primera línea, 
    luego devuelve una lista con tiempos extraidos del archivo .txt
    '''

#Inicializar listas de almacenamiento

    T=[]                                #Lista para alamacenar tiempos
    L=[]                                #Lista para almacenar líneas

    #abrir la hoja de datos
    infile=open(myfile,'r')
    
    #Leer primera línea
    linea = infile.readline()

    v0=float(linea.split()[1])          #Extraer v0

    #Leer el resto de lineas y almacenarlas en L
    for lines in infile.readlines():
        L.append(lines)
        
    #Cerrar el documento    
    infile.close()    

    #Añadir los tiempos a la lista T        
    for element in L[1:]:
        s=element.split()
        for t in s:
            T.append(float(t.split()[0]))
    #Devolver v0 y T            
    return v0, T

#Función test
def test_read_data():
    
    outfile=open('testdata.txt', 'w')
    outfile.write('v0: 69'+'\n')
    outfile.write('t:'+ '\n')
    outfile.write('0.23 123 372 0.22 818 808 234'+'\n')
    outfile.write('120 0.234 23.41 24.556 '+ '\n')
    outfile.write('1 -1 2 -2 3 -3 4 -4')
    outfile.close()
    
    print(read_data('testdata.txt'))   
                
#c)
def  write_n_sort():
    #
    data=read_data('balldat.txt')        #Datos a extraer
    g=9.8
    y=[]                                #Lista para almacenar valores de y
    t=[]                                #Lista que almacena valores de t en orden
    v0=data[0]                          #Extraer v0
    T=data[1]                           #Valores de T extraídos y en desorden
    
    #Ordenar los valores obtenidos
    for  i in range(len(T)):
        t.append(min(T))
        T.remove(min(T))
    
    
    #Generar los valores de y
    for i in range(len(t)):
        Y=v0*t[i]-0.5*g*t[i]**2
        y.append(Y)
        
    #Crear documento txt e imprimir   
    outfile=open('yvst.txt','w')
    
    outfile.write('   t         y'+'\n')
    
    for i in range(len(t)):
        outfile.write('%.5f   %.5f' %(t[i],y[i])+'\n')          #Escribir cada t y y
    outfile.close()    
        
