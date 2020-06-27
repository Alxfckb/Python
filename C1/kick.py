#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#Importar pi de math
from math import pi
 
#Definir las constantes de la fuerza gravitacional
m=0.43 #kg
g=9.81 #m/s^2
#Calculo de la fuerza gravitacional
fg=m*g

#Definir las constantes de la fuerza de arrastre 
CD=0.2
p= 1.2 #kg/m
r=0.11 #m
A=pi*r**2 #m^2
Vhard=float(1200/36) #m/s
Vsoft= float(100/36) #m/s

#Calcular la fuerza de arrastre
fd=1/2*CD*p*A*Vsoft**2 
fd2=1/2*CD*p*A*Vhard**2

#Calcular las proporciones entre Fg y Fd
R1= fg/fd
R2 = fg/fd2

#imprimir los resultados
print('La fuerza gravitacional es %3.3f' %fg, 'N')
print('La fuerza de arrastre con V=120km/h es %3.3f' %fd2 ,'N')
print('La fuerza de arrastre con V=10km/h es %3.3f' %fd ,'N')
print('Para una patada suave Fg/Fd = %2.2f' %R1)
print('Para una patada fuerte Fg/Fd = %4.2f' %R2)


