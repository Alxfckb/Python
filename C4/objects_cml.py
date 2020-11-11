#Importar sys
import sys 

#Leer valor en terminal
a=eval(sys.argv[1])

print(a,type(a))


#"this is a string" da error porque los argumentos de eval() van entre comillas
#Por tanto, estamos pidiendo que corramos el código this is a string, cuando esto no existe en python
#La forma de solucionarlo es escribir '"this is a string"'
