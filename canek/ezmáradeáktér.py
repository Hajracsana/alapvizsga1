class Nobel:
    def __init__(self,sor):
        adatok=sor.strip().split(";")
        self.ev=int(adatok[0])
        self.nev=adatok[1]
        self.szulethalal=adatok[2]
        self.orszag=adatok[3]
lista:list[Nobel]=[]
file=open("orvosi_nobeldijak.txt","r",encoding="utf-8")
elsosor=file.readline
for i in file:
    lista.append(Nobel(i))
file.close()

print(f"{len(lista)}")