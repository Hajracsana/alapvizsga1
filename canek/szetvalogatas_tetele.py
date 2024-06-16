lista=[]
pista=[]
miska=[]
import random
for i in range(10):
    lista.append(random.randint(10,99))
lista.sort()
print(*lista)

for i in lista:
    if i<=45:
        pista.append(i)
    else:
        miska.append(i)
    
print(pista)
print(miska)