numbers=list(range(10))                   #Se crea una lista con los números dígitos
print(numbers)                            #Se imprime la lista

for n in numbers:
    i =int(len(numbers)/2)        #Se generan índices que valen la mitad del número de elementos en la lista
    del numbers[i]                       #Se elimina el elemento que corresponde a la posición i que se acaba de calcular 
    print('n=%d, del %d' % (n,i), numbers) #se imprime cada n y se especifica qué casilla será eliminada
    