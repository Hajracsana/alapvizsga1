class Eredmeny:
    def __init__(self,sor):
        adatok=sor.strip().split(";")
        self.nev=adatok[0]
        self.orszag=adatok[1]
        self.technikai=float(adatok[2])
        self.komponens=float(adatok[3])
        self.levonas=int(adatok[4])
        
rovid:list[Eredmeny]=[]
donto:list[Eredmeny]=[]
file=open("rovidprogram.csv","r",encoding="utf-8")
esor=file.readline().strip()
for sor in file:
    rovid.append(Eredmeny(sor))
file.close()
file=open("donto.csv","r",encoding="utf-8")
file.readline()
for sor in file:
    donto.append(Eredmeny(sor))
file.close()

print("2. feladat")
print(f"\tA rövidprog.-ban {len(rovid)} fő indult")
print("3. feladat")
van=False
for i in donto:
    if i.orszag=="HUN":
        van=True
        break
if van==True:
    print("\tJutott ki")
else:
    print("\tNem jutott ki")