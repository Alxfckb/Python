C = 41
C == 40                           #Falso porque se está consultando si C vale 40
C != 40 and C < 41 C!=40or C<41   #Falso porque aunque c es distinto de 40, c no es menor que 41
not C == 40                       #verdadero porque c==40 es falso
not C > 40                        #Falso porque C>40 es verdadero
C <= 41                           #verdadero porque c=41
not False                         #verdadero porque estamos negando un valor falso             
True and False                    #Falso por la tabla de verdad
False or True                     #Verdadero porque F^T---->T
False or False or False           #Falso porque F^F^F ---> F^F---->F
True and True and False           #Falso porque FvTvF ----> TvF
False == 0                        #Verdadero porque es el valor or defecto
True == 0                         #Falso porque False==0
True == 1                         #Verdadero porque es el valor or defecto