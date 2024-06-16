class ORszagNepessege:
    def __init__(self, sor):
        adatok = sor.strip().split(";")
        self.orszag = adatok[0]
        self.terulet = int(adatok[1])
        self.nepessegszam=0
        self.nepesseg = adatok[2]
        self.fovaros = adatok[3]
        self.fovarosnepessege = int(adatok[4])
        self.nepsuruseg=0

lista:list[ORszagNepessege] = []
file = open("adatok-utf8.txt", "r", encoding="utf-8")
file.readline()
for sor in file:
    lista.append(ORszagNepessege(sor))
file.close()

for i in lista:
    if i.nepesseg[-1]=="g":
        i.nepessegszam=int(i.nepesseg[:-1]+"0000")
    else:
        i.nepessegszam=int(i.nepesseg)
    i.nepsuruseg=round(i.nepessegszam/i.terulet)
print(len(lista))
maxindex=0

for i in lista:
    if i.orszag=="Kína":
        print(i.nepsuruseg)

indianep=0
kinanep=0
for i in lista:
    if i.orszag=="India":
        i.nepessegszam=indianep
for i in lista:
    if i.orszag=="Kína":
        i.nepessegszam=kinanep
print(indianep-kinanep)