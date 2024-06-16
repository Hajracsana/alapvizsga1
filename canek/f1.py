class F1:
    def __init__(self,sor):
        adatok=sor.strip().split(";")
        self.date=adatok[0]
        self.grandprix=adatok[1]
        self.position=adatok[2]
        self.laps=adatok[3]
        self.points=adatok[4]
        self.team=adatok[5]
        self.status=adatok[6]

lista:list[F1]=[]
file=open("schumacher.csv","r")
elsosor=file.readline()
for sor in file:
    lista.append(F1(sor))
file.close()

print(f"3. feladat: {len(lista)}")
print(f"4. feladat: Magyar nagydíj helyezései: ")
for i in lista:
    if i.grandprix=="Hungarian Grand Prix" and i.status=="Finished":
        print(f'\t{i.date} : {i.position}')
print("5. feladat - HIBASTATISZTIKA")
szotar={}
for i in lista:
    if i.status not in szotar and i.status!="Finished":
        szotar[i.status]=1
    if i.status in szotar and i.status!="Finished":
        szotar[i.status]+=1
for k,v in szotar.items():
    if v>2:
        print(f"{k}: {v}")