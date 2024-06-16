class Hianyzas:
    def __init__(self,sor):
        adatok=sor.strip().split(";")
        self.nev=adatok[0]
        self.osztaly=adatok[1]
        self.elsonap=int(adatok[2])
        self.utolsonap=int(adatok[3])
        self.mulasztott=int(adatok[4])

lista:list[Hianyzas]=[]
file=open("szeptember.csv","r")
elsosor=file.readline()
for sor in file:
    lista.append(Hianyzas(sor))
file.close()

###
osszesora=0
for i in lista:
    osszesora+=i.mulasztott  
print(f"2. feladat: Összes mulaszott órák száma: {osszesora}")

print("3. feladat")
nap=int(input("Kérlek adj meg egy napot (1-30): "))
nev=input("Kérlek adj meg egy nevet: ")
print("4. feladat")
van=False
for i in lista:
    if nev==i.nev:
        van=True
        break
if van==True:
    print("A tanuló hiányzott szeptemberben")
else:
    print("A tanuló nem hiányzott szeptemberben")
    
print("5. feladat: Hiányzók 2017.09.19-n")
for i in lista:
    if nap==i.elsonap or nap==i.utolsonap:
        print(f"\t{i.nev} ({i.osztaly})")
        
szotar={}
for i in lista:
    if i.osztaly not in szotar:
        szotar[i.osztaly]=1
    if i.osztaly in szotar:
        szotar[i.osztaly]+=1
for k,v in szotar.items():
    (f"{k};{v}")
letreh=open("osszesites.csv","w",encoding="utf-8")
letreh.write(f'\n{i};{szotar[i]}')
letreh.close