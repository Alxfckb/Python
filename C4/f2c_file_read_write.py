import sys, pprint

# Abrir el documento con datos
infile = open('data44.txt', 'r')

# Inicializar lista donde se almacenará el contenido de la hoja
r=[]
f=[]
c=[]

# Agregar el contenido a r[]
for line in infile.readlines():
        r.append(line)
infile.close()
print(r)

n=r[3:]

# Agregar cada número a la lista f
for i in range(len(n)):
	numbers = n[i].split()[-1] 		
	f.append(float(numbers))
print(f)

for i in range(len(f)):
	C=5*(f[i]-32)/9
	c.append(C)

outfile = open('newdata44.txt',"w")
for i in range(len(f)):
	F=(f[i])
	ans=c[i]
	outfile.write('Fahrenheit degrees: %s   Celcius degrees: %.1f' %(F,ans))
	outfile.write('\n')
outfile.close()





