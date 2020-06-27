#Importar sys para leer los números desde terminal
import sys
#1. Pedir el primer número
primer_numero= float(sys.argv[1])
#2. Pedir el segundo número
segundo_numero= float(sys.argv[2])
#3. Efectuar
suma=(primer_numero+segundo_numero)

#4. Imprimir la suma
print("suma1 = "+str(suma))
print("suma2 = %2.0d" % suma)
print("suma3 = %3.1f" % suma)                                 