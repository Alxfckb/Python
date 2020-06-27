initial_amount = 100
p = 5.5 #interest rate
amount = initial_amount
years = 0
while(amount<=1.5*initial_amount):
     amount = amount + p/100 * amount
     years = years + 1
     
print(years)
print(amount)


#105.5
#111.30
#117.42
#123.88
#130.69
#137.88
#145.46
#153.46

     
#No pasa nada al cambiar p=5

initial_amount = 100
p = 5.5 #interest rate
amount = initial_amount
years = 0
while(amount<=1.5*initial_amount):
     amount +=  p/100 * amount
     years += 1
     
print(years)
print(amount)

#Este programa resuelve problemas matemáticos financieros

