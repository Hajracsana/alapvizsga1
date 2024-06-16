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
for i in szamok:
    if i%3==0:
        van=True
        print("ANYÁDAT VAN BENNE HAGYD MÁR ABBA")
    else:
        print("NINCS BENNE BAROM!!!!!!!!")

if van==True:
    print("SUKA BLATY")
else: 
    print("KOMMUNISTA VAGY?")