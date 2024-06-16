class VB:
    def __init__(self,sor):
        adatok=sor.strip().split(";")
        self.varos=adatok[0]
        self.nev1=adatok[1]
        self.nev2=adatok[2]
        self.ferohely=int(adatok[3])
    
vilagbajnok:list[VB]=[]
file=open("vb2018.txt","r")
egysor=file.readline()
for sor in file:
    vilagbajnok.append(VB(sor))
file.close()
print("Feladatmegoldás")
print(f"3. feladat: stadionok száma: {len(vilagbajnok)} ")
#4. feladat
indextotal=0
feroh=vilagbajnok[0].ferohely
for i in range(len(vilagbajnok)):
    if vilagbajnok[i].ferohely<feroh:
        feroh=vilagbajnok[i].ferohely
        indextotal=i
print("4. feladat: A legkevesebb férőhely:")
print(f'\t Város: {vilagbajnok[indextotal].varos}')
print(f'\t Stadion neve: {vilagbajnok[indextotal].nev1}')
print(f'\t Férőhely: {vilagbajnok[indextotal].ferohely}')
#5.
atlag=0
for i in vilagbajnok:
    atlag+=i.ferohely
    
print(f"5. feladat: Átlagos férőhelyszám: {atlag/len(vilagbajnok):.1f}")

#6. feladat
darab=0
for i in vilagbajnok:
    if i.nev2!="n.a.":
        darab+=1
print(f"6. feladat: Két néven is ismert stadionok száma: {darab}")
#7. feladat
bevit=input("7. feladat: Kérem a város nevét: ")
while len(bevit)<3:
    bevit=input("7. feladat: Kérem a város nevét: ")
#8. feladat
van=False
for i in vilagbajnok:
    if bevit == i.varos:
        van=True
        break
if van==True:
    print("8. feladat: A megadott város VB helyszín.")
else:
    print("8. feladat: A megadott város nem VB helyszín.")
#9. feladat
varos=[]
for i in vilagbajnok:
    if i.varos not in varos:
        varos.append(i.varos)
print(f"9. feladat: {len(varos)} különböző városban voltak mérkőzések")