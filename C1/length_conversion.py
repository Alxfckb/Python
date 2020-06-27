#1. Importar sys para leer datos en terminal
import sys 

#Pedir una medida de longitud en el SI
longm= float(sys.argv[1])

#Hacer conversión a pulgadas
linch=1.00/0.0254 * longm

#hacer conversión a pies
lfeet=1/12 * linch

#Hacer converisón a yardas
lyard=1/3 * lfeet

#hacer conversión a millas británicas
bmile=1/1760 * lyard 

#imprimir los resultados

print("en pulgadas = %3.2f " %linch, 'in')
print("en pies = %3.2f " %lfeet, 'ft')
print("en yardas = %3.2f" %lyard, 'yd')
print ("en millas británicas = %3.4f" %bmile, 'millas británicas')
