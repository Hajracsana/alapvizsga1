class Snokker:
    def __init__(self,sor):
        adatok=sor.strip().split(";")
        self.helyezes=adatok[0]
        self.nev=adatok[1]
        self.orszag=adatok[2]
        self.nyeremeny=int(adatok[3])
        
slist:list[Snokker]=[]
file=open("snooker.txt","r")
fejlec=file.readline()
for sor in file:
    slist.append(Snokker(sor))
file.close
#feladatok
print(f'3. feladat: A világlistán {len(slist)} versenyző szerepel')
#Átlagkeresés
maxossz=0
for i in slist:
    maxossz+=i.nyeremeny
print(f'4. feladat: A versenyzők átlagosan {maxossz/len(slist):.2f} fontot kerestek')
#

maxossz2=0
maxindex=0
for i in range(len(slist)):
    if slist[i].nyeremeny>maxossz2:
        maxossz2=slist[i].nyeremeny
        maxindex=i
print("5. feladat: A legjobban kereső kínai versenyző:")
print(f"\tHelyezes: {slist[maxindex].helyezes}")
print(f"\tNév: {slist[maxindex].nev}")
print(f"\tOrszág: {slist[maxindex].orszag}")
print(f"\tNyeremény összege: {slist[maxindex].nyeremeny*380} Ft")

#keresés
van=False
for i in slist:
    if i.orszag=="Norvégia" and len(i.nev)<=4:
        van=True
        break
print("6. feladat: ",end=" ")
if van==True:
    print("A versenyzők között van norvég versenyző.")
else:
    print("A versenyzők között nincs norvég versenyző.")
    
print("7. feladat: Statisztika")
szotar={}
for i in slist:
    if i.orszag not in szotar:
        szotar[i.orszag]=1
    else:
        szotar[i.orszag]+=1
for k,v in szotar.items():
    if v>4:
        print(f"\t{k} - {v} fő")