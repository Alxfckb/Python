#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  4 15:18:14 2020

@author: alexanderalvarado
"""


#Tipe in programs and debug them
# a) Does sin^2(x))+cos^2(x)=1? código incorrecto
    #from math import sin, cos 
    #x=pi/4
    #1_val= sin^2(x) + cos^2(x)
    #print(1_VAL)
    
#Errores:    
#Error 1: ^ no es un operador para exponenciar
#Error 2: la suma de cuadrados se definió como 1_val y se quiso imprimir 1_VAL
#rror 3: no podemos definir variables empezando con números


#código corregido 
from math import sin, cos , pi

x=pi/4

val = sin(x)**2 + cos(x)**2 
print(val)

#b) Work with the expressions for movement with constant acceleration:
#código incorrecto
    #v0 = 3 m/s
    #t=1s
    #a = 2 m/s**2
    #s = v0*t + 1/2 a*t**2 print s

#Errores
#Error 1: las unidades de medida no tienen sentido en el código
#Error 2: en la penúltima línea falta un * al multiplicar 1/2 por a*t***2
#código corregido

v0 = 3
t = 1
a = 2

s = v0*t + 1/2*a*t**2

print(s)