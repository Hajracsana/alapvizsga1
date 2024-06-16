import random
szamok=[]
for i in range(10):
    vsz=random.randint(-10,10)
    while vsz==0:
        vsz=random.randint(-10,10)
    szamok.append(vsz)
    print(*szamok)
    
#maga a tétel
pozitiv=0
for i in szamok:
    if i>0:
        pozitiv+=1
print(f" POZ: @{pozitiv} NIGATÍV: {len(szamok)-pozitiv}")