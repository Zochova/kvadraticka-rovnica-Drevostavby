#D=ax2+bx+c=0

import math

x=int(input('Zadajte číslo a: '))

y =int(input('Zadajte číslo b: '))

z=int(input('Zadajte číslo c: '))

w=(y**2) - (4*x*z)

mož1 = (-y-math.sqrt(w))/(2*x)

mož2 = (-y+math.sqrt(w))/(2*x)

print('Riešenia sú {0} a {1}'.format(mož1,mož2))