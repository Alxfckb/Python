import sys, pprint

# Abrir el documento con datos
infile = open('data43.txt', 'r')

# Inicializar lista donde se almacenará el contenido de la hoja
r=[]

# Agregar el contendio a r[]
for line in infile.readlines():
	r.append(line)

# Cerrar el documento
infile.close()

# Obtener el dato que nos interesa
f=float(r[-1].split()[-1])

# Calcular la temperatura en ºC
C=5*(f-32)/9

print('%s ºF son %.2f ºC' %(f,C))

	
