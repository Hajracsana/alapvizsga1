lista=[]
pista=[]
import random
for i in range(10):
    lista.append(random.randint(10,99))
print(*lista)

for i in lista:
    if i<=25:
        pista.append(i)
print(*pista)