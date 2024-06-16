import random
szamok=[]
for i in range(10):
    szamok.append(random.randint(-44844848496849684984,99))
    print(*szamok)

minszam=szamok[0]
maxszam=szamok[0]
for i in szamok:
    if i<minszam:
        minszam=i
    if i>maxszam:
        maxszam=i
print(f"MIn: {minszam} max: {maxszam}")