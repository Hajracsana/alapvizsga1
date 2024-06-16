class Vizi:
    def __init__(self,sor):
        adatok=sor.strip().split(";")
        self.nev=adatok[0]
        self.azon=adatok[1]
        self.eora=int(adatok[2])
        self.eperc=int(adatok[3])
        self.eossz=self.eora*60+self.eperc
        self.vora=int(adatok[4])
        self.vperc=int(adatok[5])
        self.vossz=self.vora*60+self.vperc

vizi:list[Vizi]=[]
file=open("kolcsonzesek.txt","r",encoding="utf-8")
elso_sor=file.readline().strip()
for sor in file:
    vizi.append(Vizi(sor))
file.close()

print(f"5. feladat: Napi kölcsönzések száma: {len(vizi)}")
be_nev=input("6. feladat: Kérek egy nevet: ")
print(f"\t{be_nev} kölcsönzései:")
talalt=False
for i in vizi:
    if i.nev==be_nev:
        talalt=True
        print(f"\t{i.eora:02d}:{i.eperc:02d} - {i.vora:02d}:{i.vperc:02d}")
if not talalt:
    print("\tNem volt ilyen nevű kölcsönző!")

be_ido=input("7. feladat: Adjon meg egy időpontot óra:perc alakban: ").split(":")
be_ora=int(be_ido[0])
be_perc=int(be_ido[1])
be_osszp=be_ora*60+be_perc
for i in vizi:
    if i.eossz<=be_osszp and i.vossz>=be_osszp:
        print(f"\t{i.eora:02d}:{i.eperc:02d} - {i.vora:02d}:{i.vperc:02d} {i.nev}")

