#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  4 18:26:39 2020

@author: alexanderalvarado
"""


#Valuar la campana de Gauss en m=0, s=2, x=1
#Importar la función exponencial, constante pi y raiz cuadrada de math
from math import exp , sqrt, pi

#Definimos las constantes
m=0
s=2
x=1

#Definimos la función G (la campana)

G = 1/(sqrt(2*pi)*s)*exp(-1/2* ((x-m)/s)**2 )
print (G)
