#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  4 17:33:48 2020

@author: alexanderalvarado
"""


#(c)Verify these equations: (a+b)^2 , (a-b)^2

#a=3,3 a2 = a**2 b2 = b**2
#eq1_sum = eq2_sum =
#eq1_pow = eq2_pow =
#b=5,3
#a2 + 2ab + b2 a2 - 2ab + b2
#(a + b)**2 (a - b)**2
#print ’First equation: %g = %g’, % (eq1_sum, eq1_pow)
#print ’Second equation: %h = %h’, % (eq2_pow, eq2_pow)

#--------------Errores------------------
#Error 1: hay que definir las variables en diferentes líneas
#Error 2: al definir a y b, se usa coma para definir un float pero debe usarse un punto 
#Error 3: falta dos veces el operador * en el segundo término de los trinomios
#Error 4: en los print, no debe haber coma entre ... %g/h' , % ...
#Error 5: En la última línea se  valuó en (eq2_pow, eqw_pow) cuando debió ser en (eq2_sum, eq2_pow)
a=3.3
b=5.3
a2=a**2
b2=b**2

eq1_sum = a2 + 2*a*b + b2
eq2_sum = a2 - 2*a*b + b2

eq1_pow = (a + b)**2
eq2_pow = (a - b)**2

print ('First equation : %g = %g' % (eq1_sum, eq1_pow))
print ('Second equation : %g = %g' % (eq2_sum, eq2_pow))


