class Adatszerk:
    def __init__(self,sor):
        adat=sor.strip().split(";")
        self.hazai=adat[0]
        self.idegen=adat[1]
        self.hazai_pont=int(adat[2])
        self.idegen_pont=int(adat[3])
        self.helyszin=adat[4]
        self.idopont=adat[5]
        
kosar:list[Adatszerk]=[]
file=open("eredmenyek.csv","r")
elso_sor=file.readline().strip()
for sor in file:
    kosar.append(Adatszerk(sor))
file.close()

hazaid_db=0
idegen_db=0
for i in kosar:
    if i.hazai=="Real Madrid":
        hazaid_db+=1
    if i.idegen=="Real Madrid":
        idegen_db+=1
print(f"3. feladat: Real Madrid Hazai {hazaid_db}, Idegen: {idegen_db}")

volt=False
for i in kosar:
    if i.hazai_pont==i.idegen_pont:
        volt=True
        break
print("4. feladat. Volt döntetlen? ", end="")
if volt==True:
    print("igen")
else:
    print("nem")
    
for i in kosar:
    if "Barcelona" in i.hazai:
        print(f"5. feladat. bercelioniai csapat neve: {i.hazai}")
        break
print("6. feladat")
for i in kosar:
    if i.idopont=="2004-11-21":
        print(f"\t{i.hazai}-{i.idegen} ({i.hazai_pont}:{i.idegen_pont})")
print("7. feladat")
stadionok=[]
for i in kosar:
    if i.helyszin not in stadionok:
        stadionok.append(i.helyszin)
for i in stadionok:
    db=0
    for j in kosar:
        if j.helyszin==i:
            db+=1
    if db>20:
        print(f"\t {i}: {db}")
        
stadion={}
for i in kosar:
    if i.helyszin not in stadion:
        stadion[i.helyszin]=1
    else:
        stadion[i.helyszin]+=1
print("7. feladat v2")
for i in stadion:
    if stadion[i]>20:
        print(f"\t {i,stadion[i]}")