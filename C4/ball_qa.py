#Programa de caida libre que pide v0 y t al usuario 

v0=float(input('v0=? '))

t=float(input('t=? '))

g=9.81

y=v0*t - 0.5*g*t**2

print(y)

