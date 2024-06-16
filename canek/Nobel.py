class Nobel:
    def __init__(self,sor):
        adatok=sor.strip().split(";")
        self.evszam=int(adatok[0])
        self.tipus=adatok[1]
        self.keresztnev=adatok[2]
        self.vezeteknev=adatok[3]
nobellist:list[Nobel]=[]
file=open("nobel.csv","r", encoding="utf-8")
fejlec=file.readline()
for sor in file:
    nobellist.append(Nobel(sor))
file.close

print("3. feladat: ", end="")
totalindex=0
script_kereszt="Arthur B."
script_vezetek="McDonald"
for i in range(len(nobellist)):
    if nobellist[i].keresztnev==script_kereszt and nobellist[i].vezeteknev==script_vezetek:
        totalindex=i
        break
print(nobellist[totalindex].tipus)
#4. feladat
uj_totalindex=0
for i in range(len(nobellist)):
    if nobellist[i].tipus=="irodalmi" and nobellist[i].evszam=="2017":
        uj_totalindex=i
        break
print(f"4. feladat: {nobellist[i].keresztnev} {nobellist[i].vezeteknev}")
#5.
print("5. feladat")
for i in range(len(nobellist)):
    if nobellist[i].vezeteknev=="" and "béke" in nobellist[i].tipus and nobellist[i].evszam>1990:
        print(f"\t{nobellist[i].evszam}: {nobellist[i].keresztnev}")
print("6. feladat")
for i in range(len(nobellist)):
    if "Curie" in nobellist[i].vezeteknev:
        print(f"\t{nobellist[i].evszam}: {nobellist[i].keresztnev} {nobellist[i].vezeteknev}({nobellist[i].tipus})")
print("7. feladat")
nobeldijak={}
for i in nobellist:
    if i.tipus not in nobeldijak:
        nobeldijak[i.tipus]=1
    else:
        nobeldijak[i.tipus]+=1
for k,v in nobeldijak.items():
    print(f"\t{k} - {v} db")
print("8. feladat: orvosi.txt")
Lista=[]
for i in range(len(nobeldijak)):
    if nobellist[i].tipus=="orvosi":
        with open("orvosi.txt","w") as file:
            file.write(f"{nobellist[i].evszam}: {nobellist[i].vezeteknev} {nobellist[i].keresztnev}")