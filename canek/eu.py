class EU:
    def __init__(self,sor):
        adatok=sor.strip().split(";")
        self.orszag=adatok[0]
        self.datum=adatok[1]
        
eulista:list[EU]=[]
file=open("EUcsatlakozas.txt","r")
for sor in file:
    eulista.append(EU(sor))
file.close()
print(f'1. feladat: Tagállamok száma: {len(eulista)} db')
db=0
for i in eulista:
    if "2007" in i.datum:
        db+=1
print(f"2007-ben {db} ország csatlakozott.")
for i in eulista:
    if i.orszag=="Magyarország":
        print(f'Magyarország csatlakozásának dátuma: {i.datum}')
    break

volte=False
for i in eulista:
    if ".05." in i.datum:
        volte=True
    break
if volte==True:
    print("Májusban volt csatlakozás!")
else:
    print("Májusban nem volt csatlakozás!")
    
maxdatum=""
maxorsz=""
for i in eulista:
    if i.datum>maxdatum:
        maxdatum=i.datum
        maxorsz=i.orszag
print(f'Legutoljára csatlakozott ország: {maxorsz}')
szotar={}
for i in eulista:
    if i.datum[0:4] not in szotar:
        szotar[i.datum[0:4]]=1
    else:
        szotar[i.datum[0:4]]+=1
        