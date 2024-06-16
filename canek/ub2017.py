class Ultra:
    def __init__(self,sor):
        adatok=sor.strip().split(";")
        self.versenyzo=adatok[0]
        self.rajtszam=int(adatok[1])
        self.kategoria=adatok[2]
        self.idoeredmeny=adatok[3]
        self.tavszazalek=int(adatok[4])
        ido=adatok[3].split(":")
        self.ora=int(ido[0])
        self.perc=int(ido[1])
        self.mp=int(ido[2])
        self.osszora=self.ora+self.perc/60+self.mp/3600
ub:list[Ultra]=[]
file=open("ub2017egyeni.txt","r")
fejlec=file.readline()
for sor in file:
    ub.append(Ultra(sor))
file.close()
print(f'3.2 feladat: Futók száma {len(ub)}')
db=0
for i in ub:
    if i.tavszazalek==100 and i.kategoria=="Noi":
        db+=1
print(f'3.3 feladat Célba ért női vesenyzők száma: {db} fő')

maxhossz=0
maxindex=0
for i in range(len(ub)):
    if len(ub[i].versenyzo)>maxhossz:
        maxhossz=len(ub[i].versenyzo)
        maxindex=i
print('3.4  feladat: Leghosszabb nevű versenyző: ')
print(f'\t Név: {ub[maxindex].versenyzo}')
print(f'\t Rajtszám: {ub[maxindex].rajtszam}')
print(f'\t Kategória: {ub[maxindex].kategoria}')
print(f'\t Eredmény: {ub[maxindex].idoeredmeny}')
print(f'\t Távszázalék: {ub[maxindex].tavszazalek}')

osszido=0
db1=0
for i in ub:
    if i.kategoria=="Ferfi" and i.tavszazalek==100:
        osszido+=i.osszora
        db1+=1
print(f'3.5 feladat: Ferfi sportolók ideje: {osszido/db1}')