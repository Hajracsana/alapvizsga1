import random
szamok=[]
for i in range(15):
    szamok.append(random.randint(10,99))
    print(*szamok)
    
for i in range(len(szamok)-1):
    for j in range(i+1,len(szamok)):
        if szamok[i]>szamok[j]:
            csere=szamok[i]
            szamok[i]=szamok[j]
            szamok[j]=csere
    print(*szamok)