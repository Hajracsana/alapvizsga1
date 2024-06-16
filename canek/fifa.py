class FIFA:
    def __init__(self,sor):
        adatok=sor.strip().split(";")
        self.csapat=adatok[0]
        self.helyezes=int(adatok[1])
        self.valtozas=int(adatok[2])
        self.pontszam=int(adatok[3])
fifalist:list[FIFA]=[]
file=open("fifa.txt","r")
egysor=file.readline()
for sor in file:
    fifalist.append(FIFA(sor))
file.close()

print(f'3. feladat: A listában {len(fifalist)} csapat van')
print(f'4. feladat:', end="")
osszeg=0
darab=len(fifalist)
for i in fifalist:
    osszeg+=i.pontszam
print(f'A csapatok átlagos pontszáma: {osszeg/darab:.2f}')
print('5. feladat: a legtöbbet javító csapat:')
maxindex=0
maxvalt=0
for i in range(len(fifalist)):
    if fifalist[i].valtozas>maxvalt:
        maxvalt=fifalist[i].valtozas
        maxindex=i
print(f'\tHelyezés: {fifalist[maxindex].helyezes}')
print(f'\tCsapat: {fifalist[maxindex].csapat}')
print(f'\tPontszám: {fifalist[maxindex].pontszam}')

print('6. feladat: ', end="")
van=False
for i in fifalist:
    if i.csapat=="Magyarország":
        van=True
        break
if van==True:
    print('A csapatok között van Magyarország')
else:
    print('A csapatok között nincs Magyarország')
    
szotar={}
for i in fifalist:
    if i.valtozas not in szotar:
        szotar[i.valtozas]=1
    else:
        szotar[i.valtozas]+=1

for k,v in szotar.items():
    if v>1:
        print(f"\t{k} helyet változott - {v} csapat")