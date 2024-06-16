class Hegyek:
    def __init__(self,sor):
        adatok=sor.strip().split(";")
        self.nev=adatok[0]
        self.hegyseg=adatok[1]
        self.magas=int(adatok[2])
        
hegyeklist:list[Hegyek]=[]
file=open("Magyarorszag_hegyek.txt","r", encoding="UTF-8")
fejlec=file.readline()
for sor in file:
    hegyeklist.append(Hegyek(sor))
file.close

#Feladatok
print(f'3. feladat: Hegycsúcsok száma: {len(hegyeklist)}')
magas=0
for i in hegyeklist:
    magas+=i.magas
print(f'4. feladat: A hegyek átlagmagassága: {magas/len(hegyeklist)}m')

maxmagas=0
maxindex=0
for i in range(len(hegyeklist)):
    if hegyeklist[i].magas>maxmagas:
        maxmagas=hegyeklist[i].magas
        maxindex=i
print('5. feladat: A legmagasabb hegycsúcs adatai:')
print(f'\tNév: {hegyeklist[maxindex].nev}')
print(f'\tHegység: {hegyeklist[maxindex].hegyseg}')
print(f'\tMagassága: {hegyeklist[maxindex].magas}m')
print('6. feladat')
beinput=int(input('Kérek egy magasságot: '))
van=False
for i in hegyeklist:
    if i.magas>beinput and i.hegyseg=="Börzsöny":
        van=True
        break
if van==True:
    print(f'\tVan ', end="")
else:
    print(f'Nincs ', end="")
print(f'{beinput}m-nél magasabb hegycsúcs a Börzsönyben.')

valto=3.280839895
db=0
for i in hegyeklist:
    if i.magas*valto>3000:
        db+=1
print(f'7. feladat: 3000 lábnál magasabb hegycsúcsok száma: {db}')
print('8. feladat STATISZTIKA')
szotar={}
for i in hegyeklist:
    if i.hegyseg not in szotar:
        szotar[i.hegyseg]=1
    else:
        szotar[i.hegyseg]+=1
for k,v in szotar.items():
    print(f'\t{k} - {v} db')

print('9. feladat: bukk-videk.txt')
file=open('bukk_videk.txt',"w",encoding="UTF-8")
file.write("Hegycsúcs neve;Magasság láb\n")
for i in hegyeklist:
    if i.hegyseg=="Bükk-vidék":
        file.write(f'{i.nev};{i.magas*valto:.1f}\n')
file.close