#Encontrar la masa de varias sustancias
#definimos nuestras constantes(densidades en g/cm3)
air      =   0.0012
gas =   0.67
ice      =   0.9
cuerpo   =  1.03
iron     =   7.8
plata   =   10.5
platino =   21.4
#equivalencia entre litro y cm^3 
l=1000.00
# Cálculo de masas

mair=float(air*l)

mgas=float(gas*l)

mice=float(ice*l)

mcuerpo= float(cuerpo*l)

miron=float(iron*l)

mplata=float(plata*l) 

mplatino=float(platino * l)

#Imprimiendo 
print('la masa en un litro de aire es  %3.2f' %mair, 'g')
print('la masa en un litro de gasolina es  %3.2f' %mgas, 'g')
print('la masa en un litro de cuerpo humano es  %3.2f' %mcuerpo, 'g')
print('la masa en un litro de hierro es  %3.2f'  %miron, 'g')
print('la masa en un litro de plata es  %3.2f' %mplata, 'g')
print('la masa en un litro de platino es  %3.2f' % mplatino, 'g')

