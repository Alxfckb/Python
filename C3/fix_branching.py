#Resolver un problema con una función
def f(x):
    if 0<= x <= 2:
        return x**2
    elif 2 < x <= 4:
        return 4
    elif x < 0:
        return 0
# No obtenemos valores devueltos para x=5 0 x=10 porque el dominio de la función es [0,4] 
# y no le dijimos al programa qué hacer en caso de que x>5