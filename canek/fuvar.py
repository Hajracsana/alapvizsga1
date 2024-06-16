class Fuvar:
    def __init__(self,sor):
        adatok=sor.strip().split(";")
        self.taxiid=int(adatok[0])
        self.indulas=str(adatok[1])
        self.idotartam=int(adatok[2])
        self.tavolsag=float(adatok[3].replace(",","."))
        self.viteldij=float(adatok[4].replace(",","."))
        self.borravalo=float(adatok[5].replace(",","."))
        self.fizetesModja=str(adatok[6])
taxi:list[Fuvar]=[]
file=open("fuvar.csv","r")
egysor=file.readline()
for sor in file:
    taxi.append(Fuvar(sor))
file.close()

print(f'3. feladat: {len(taxi)} fuvar')
print('4. feladat: ')
fuvarok=0
bevetel=0
for i in range(len(taxi)):
    if taxi[i].taxiid==6185:
        fuvarok+=1
        bevetel+=taxi[i].viteldij
        bevetel+=taxi[i].borravalo
print(f'\t {fuvarok} fuvar alatt: {bevetel}$')
print('5. feladat')
szotar={}
for i in taxi:
    if i.fizetesModja not in szotar:
        szotar[i.fizetesModja]=1
    else:
        szotar[i.fizetesModja]+=1
for k,v in szotar.items():
    print(f"\t{k} - {v} fuvar")

#6
osszeg=0
for i in taxi:
    osszeg+=(i.tavolsag*1.6)  
print(f'6. feladat: {osszeg:.2f}km')

print('7. feladat - Leghosszabb fuvar')
maxindex=0
maxtav=0
for i in range(len(taxi)):
    if taxi[i].idotartam>maxtav:
        maxtav=taxi[i].idotartam
        maxindex=i
print(f'\tFuvar hossza: {taxi[maxindex].idotartam} másodperc')
print(f'\tTaxi azonositó: {taxi[maxindex].taxiid}')
print(f'\tMegtett távolság: {taxi[maxindex].tavolsag} miles')
print(f'\tViteldíj: {taxi[maxindex].viteldij} $')
print('8. feladat - HIBA.TXT')
fuvarrend=sorted(taxi,key=lambda x:x.indulas)
# for i in range(10):
#     print(fuvarrend[i].taxiid,fuvarrend[i].indulas,fuvarrend[i].idotartam,fuvarrend[i].tavolsag)
file=open("hibak.txt","w",encoding="utf-8")
file.write(f"{egysor}\n")
for i in fuvarrend:
    if i.idotartam>0 and i.viteldij>0 and i.tavolsag==0:
        file.write(f'{i.taxiid};{i.indulas};{i.idotartam};{i.tavolsag};{i.viteldij},{i.borravalo};{i.fizetesModja}\n')