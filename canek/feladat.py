class Bicikli:
    def __init__(self,sor):
        adatok=sor.strip().split(";")
        self.rajtszam=adatok[0]
        self.kategoria=adatok[1]
        self.nev=adatok[2]
        self.egyesulet=adatok[3]
        self.ido=adatok[4]
        self.ora=int(self.ido[0])
        self.perc=int(self.ido[2:3])
        self.mp=int(self.ido[5:])
        self.ossz=int((self.ora)*360+self.perc*60+self.mp)
    
maraton:list[Bicikli]=[]
file=open("bukkm2019.txt","r", encoding="utf-8")
esor=file.readline().strip()
for sor in file:
    maraton.append(Bicikli(sor))
file.close()

#***#
print("2. feladat")
print(f"Versenytávot nem teljesítők: {100-((len(maraton)/691)*100)}%")
print("3. feladat")
darab=0
for i in maraton:
    if i.rajtszam[0]=="R" and i.kategoria[-1]=="n":
        darab+=1
print(f"Női versenyzők száma rövid távú versenyen: {darab}fő")
print("6. versenyző")
van=False
for i in maraton:
    if i.ossz>=6:
        van=True
        break
if van==True:
    print("Volt ilyen versenyző")
else:
    print("Nem volt ilyen versenyző")
print("7. feladat")
maxindex=0
maxido=1
for i in range(len(maraton)):
    if "R" in maraton[i].rajtszam:
        if maraton[i].ossz<maxido:
            maxido=maraton[i].ossz
            maxindex=i    
print(f"\tRajtszám: {maraton[maxindex].rajtszam}")
print(f"\tNév: {maraton[maxindex].nev}")
print(f"\tEgyesület: {maraton[maxindex].egyesulet}")
print(f"\tIdő:{maraton[maxindex].ido}")

szotar={}
for i in maraton:
    if i.kategoria[-1]=="f":
        if i.kategoria not in szotar:
            szotar[i.kategoria]=1
        else:
            szotar[i.kategoria]+=1
for i in szotar:
    print(f"{i} - {szotar[i]}fő")