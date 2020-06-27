#Código 1: este podría no funcionar como esperamos, sin embargo lo hace. El problema es que imprime demasiados decimales
C=21;  F= 9/5*C + 32; print ('c1', F) 

#Código 2<
C=21.0; F= (9/5)*C+32; print('c2',F)

#Código 3
C=21.0; F= 9*C/5+32; print('c3',F)

#Código 4
C = 21.0; F = 9.*(C/5.0) + 32; print('c4',F)

#Código 5
C = 21.0; F = 9.0*C/5.0 + 32; print('c5',F)

#Código 6
C=21; F= 9*C/5+32; print('c6',F)

#Código 7
C = 21.0; F = (1/5)*9*C + 32; print('c7',F)

#Codigo 8 
C=21; F= (1./5)*9*C+32; print(F)
