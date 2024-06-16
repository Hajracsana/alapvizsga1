class F1:
    def __init__(self,sor):
        adatok=sor.strip().split(";")
        self.nev=adatok[0]
        self.szuletesi_datum=adatok[1]
        self.nemzetiseg=adatok[2]
        self.rajtszam=int(adatok[3])
fore:list[F1]=[]
file=open("pilotak.csv","r", encoding="utf-8")
fejlec=file.readline()
for sor in file:
    fore.append(F1(sor))
file.close
#Feladatok#
print(f"3. feladat: {len(fore)}")
print(f"4. feladat: {fore[-1].nev}")
print("5. feladat")
for i in fore:
    if i.szuletesi_datum[:2]=="18" or i.szuletesi_datum[:4]=="1900":
        print(f"\t{i.nev} ({i.szuletesi_datum})")
#minumumkereses
min=0
mindex=0
for i in fore:
    if i.rajtszam<i:
        min=i.rajtszam
        mindex=i
print(f"6. feladat: ", end="" ) 
fore[mindex].nemzetiseg