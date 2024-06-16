class Fifa:
    def __init__(self,sor):
        adatok=sor.strip().split(";")
        self.csapat=adatok[0]
        self.helyezes=int(adatok[1])
        self.valtozas=int(adatok[2])
        self.pontszam=int(adatok[3])

fifa:list[Fifa]=[]
file=open("fifa.txt","r")
elso_sor=file.readline().strip()
for sor in file:
    fifa.append(Fifa(sor))
file.close()

print(f"3. feladat: A világranglistán {len(fifa)} csapat szerepel.")

ossz_pont=0
for i in fifa:
    ossz_pont+=i.pontszam
print(f"4. feladat: A csapatok átlagos pontszáma: {ossz_pont/len(fifa):.2f} pont")

print("5. feladat: A legtöbbet javító csapat:")
max_valt=0
max_index=0
for i in range(len(fifa)):
    if fifa[i].valtozas>max_valt:
        max_valt=fifa[i].valtozas
        max_index=i
print(f"\tHelyezés: {fifa[max_index].helyezes}")
print(f"\tCsapat: {fifa[max_index].csapat}")
print(f"\tPontszám: {fifa[max_index].pontszam}")

van="nincs"
for i in fifa:
    if i.csapat=="Magyarország":
        van="van"
        break
print(f"6. feladat: A csapatok között {van} Magyarország.")

szotar = {}
for i in fifa:
    if i.valtozas not in szotar:
        szotar[i.valtozas] = 1
    else:
        szotar[i.valtozas] += 1
for k,v in szotar.items():
    if v > 1:
        print(f"\t{k} helyet változott - {v} csapat")