import math
import random
#1
a = int(input('Kérem a másodfokú egyenlet főegyütthatóját:'))
a = float(a)
while a== 0:
    print('Ez nem lesz másodfokú egyenlet')
    a= input('Kérem a konsans tagot')
    a= float(a)
b= int(input('Kérem a másodfokú:'))
c= int(input('Kérem a konstans tagot'))
d= math.sqrt((b*b)-4*a*c))
print(d)
if d<0:
    print("Van valós megoldás")
else:
    print("Nem létezik valós megoldása")