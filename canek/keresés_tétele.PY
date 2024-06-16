import random
szamok=[]
for i in range(10):
    vsz=random.randint(-10,10)
    while vsz==0:
        vsz=random.randint(-10,10)
    szamok.append(vsz)
    print(*szamok)

#maga a tétel
van=False
totalindex=i
for i in szamok:
    if i%3==0:
        van=True
        totalindex=i
        break
    else:
        break

if van==True:
    print("VAN")
    print(szamok[totalindex])
else: 
    print("NINCS.")