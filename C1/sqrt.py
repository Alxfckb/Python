a=2; b=1; c=2; 

from cmath import sqrt 
q= sqrt(b*b - 4*a*c)
x1= (-b + q)/2*a
x2= (-b - q)/2*a
print(a)
print(-b+q)
print (2*a)
#print (x1, x2)
#El error es que las raices son complejas y math es una librería para números reales, habría que importar desde cmath.
