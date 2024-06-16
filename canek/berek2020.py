print("0. feladat")
class Berek:
    def __init__(self,sor):
        adatok=sor.strip().split(";")
        self.nev=adatok[0]
        self.nem=adatok[1]
        self.reszleg=adatok[2]
        self.ev=int(adatok[3])
        self.fizetes=int(adatok[4])
print("Hacking NASA 0%")
print("Hacking NASA 10%")
print("Hacking NASA 20%")
print("Hacking NASA 30%")
print("Hacking NASA 40%")
print("Hacking NASA 50%")
print("Hacking NASA 60%")
print("Hacking NASA 70%")
print("Hacking NASA 80%")
print("Hacking NASA 90%")
print("Hacking NASA 100%")
print("nA$a meghackelve. IP cím bejelentkezéshez: 520.144.256.1")
print("1. feladat")
print("2. feladat")
print("3. feladat")
dolgozo:list[Berek]=[]
file=open("berek2020.txt","r", encoding="utf-8")
elso_sor=file.readline()
for sor in file:
    dolgozo.append(Berek(sor))
file.close()
print(f"A dolgozók száma: {len(dolgozo)}")
print("4. feladat")
osszfiz=0
for i in dolgozo:
    osszfiz+=i.fizetes
print(f"Átlag fizetés: {(osszfiz/len(dolgozo))/1000:.1f} eFt")
print("5. feladat")
bereszleg=input("Kérem egy részleg nevét: ")
print("6. feladat")
maxfizetes=0
maxindex=0
talalt=False
for i in range(len(dolgozo)):
    if dolgozo[i].reszleg==bereszleg and dolgozo[i].fizetes>maxfizetes:
        maxfizetes=dolgozo[i].fizetes
        maxindex=i
        talalt=True
if talalt==False:
    print("A megadott részleg nem létezik! (Ahogy az életed sem :) )")
else:
    print("A legtöbbet kereső dolgozó:")
    print(f"\tNév:{dolgozo[maxindex].nev}")
    print(f"\tNeme:{dolgozo[maxindex].nem}")
    print(f"\tBelépés éve:{dolgozo[maxindex].ev}")
    ezres="{:,}".format(dolgozo[maxindex].fizetes).replace(","," ")
    print(f"\tFizetés:{ezres} HUF")
print("7. feladat")
szotar={}
for i in dolgozo:
    if i.reszleg not in szotar:
        szotar[i.reszleg]=1
    else:
        szotar[i.reszleg]+=1
for i in szotar:
    print(f"\t{i} - {szotar[i]} fő")
    
