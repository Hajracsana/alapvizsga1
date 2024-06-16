class Fuvar:
    def __init__(self,sor):
        adatok=sor.strip().split(";")
        self.azon=int(adatok[0])
        self.indulas=adatok[1]
        self.hossz=int(adatok[2])
        self.tav=float(adatok[3].replace(",","."))
        self.viteldij=float(adatok[4].replace(",","."))
        self.borravalo=float(adatok[5].replace(",","."))
        self.mod=adatok[6]

fuvar:list[Fuvar]=[]
file=open("fuvar.csv","r", encoding="utf-8")
elso_sor=file.readline().strip()
for sor in file:
    fuvar.append(Fuvar(sor))
file.close()

print(f"3. feladat: {len(fuvar)} fuvar")

print("4. feladat")
fuvarok = 0
bevetel = 0
for i in range(len(fuvar)):
    if fuvar[i].azon == 6185:
        fuvarok += 1
        bevetel += fuvar[i].viteldij
        bevetel += fuvar[i].borravalo
print(f"\t{fuvarok} fuvar alatt: {bevetel} ")

print("5. feladat")
szotar = {}
for i in fuvar:
    if i.mod not in szotar:
        szotar[i.mod] = 1
    else:
        szotar[i.mod] += 1
for k,v in szotar.items():
    print(f"\t{k} : {v}")
    
print("6. feladat")
megtettut = 0
for i in fuvar:
    megtettut += i.tav
print(f"\t{megtettut * 1.6:.2f} km")

print("7. feladat")
mxindex = 0
maxut = 0
for i in fuvar:
    if i.tav > maxut:
        maxut = i.tav
        mxindex = i
print(f"\tFuvar hossza: {mxindex.hossz}")
print(f"\tTaxi azonosito: {mxindex.azon}")
print(f"\tMegtett tavolsag: {mxindex.tav}")
print(f"\tViteldij: {mxindex.viteldij + mxindex.borravalo }")

fuvarrend = sorted(fuvar, key = lambda x:x.indulas)

file=open("hibak.txt","w",encoding="utf-8")
file.write(f"{elso_sor}\n")
for i in fuvarrend:
    if i.hossz>0 and i.viteldij>0 and i.tav==0:
        file.write(f"{i.azon};{i.indulas};{i.hossz};{i.tav};{i.viteldij};{i.borravalo};{i.mod}\n")