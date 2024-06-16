class Bal:
    def __init__(self,sor):
        adat=sor.strip().split(";")
        self.nev=adat[0]
        self.elsop=adat[1]
        self.utolsop=adat[2]
        self.suly=int(adat[3])
        self.magas=int(adat[4])
        
balkezesek:list[Bal]=[]
file=open("balkezesek.csv","r")
elsosor=file.readline().strip()
for sor in file:
    balkezesek.append(Bal(sor))
file.close()
print(f"3. feladat: {len(balkezesek)}")
print("4. feladat")
for i in balkezesek:
    if "1990-10" in i.utolsop:
        print(f"\t{i.nev}, {i.magas*2.54:.1f} cm")
print("5. feladat")
beevsz=int(input("Kérek egy 1990 és 1999 közötti évszámot: "))
while beevsz<1990 or beevsz>1999:
    beevsz=int(input("HIBA! Kérek egy 1990 és 1999 közötti évszámot: "))
print("6. feladat", end=" ") 
osszs=0
osszdb=0
for i in balkezesek:
    if int(i.elsop[0:4])<beevsz and int(i.utolsop[0:4])>beevsz:
        osszs+=i.suly
        osszdb+=1
print(f"{osszs/osszdb:.2f} font")