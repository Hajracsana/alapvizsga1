class Keszthely:
    def __init__(self,sor):
        adatok = sor.strip().split(";")
        self.vnev = adatok[0]
        self.szulnev = int(adatok[1])
        self.rajtsz = int(adatok[2])
        self.nem = adatok[3]
        self.kat = adatok[4]
        self.uszido = adatok[5]
        self.uszms = int(self.uszido[0:2]) * 3600 + int(self.uszido[3:5]) * 60 + int(self.uszido[6:])
        self.eldepo = adatok[6]
        self.eldems = int(self.eldepo[0:2]) * 3600 + int(self.eldepo[3:5]) * 60 + int(self.eldepo[6:])
        self.kerekido = adatok[7]
        self.kerekms = int(self.kerekido[0:2]) * 3600 + int(self.kerekido[3:5]) * 60 + int(self.kerekido[6:])
        self.masdepo = adatok[8]
        self.masdepoms = int(self.masdepo[0:2]) * 3600 + int(self.masdepo[3:5]) * 60 + int(self.masdepo[6:])
        self.futasido = adatok[9]
        self.futasms = int(self.futasido[0:2]) * 3600 + int(self.futasido[3:5]) * 60 + int(self.futasido[6:])
        self.osszido = self.uszms + self.eldems + self.kerekms + self.masdepoms + self.futasms

kesz:list[Keszthely] = []
file = open("Eredmenyek.txt" , "r", encoding="utf-8")
for sor in file:
    kesz.append(Keszthely(sor))
file.close()

print(f"\n2.feladat: A versenyt {len(kesz)} versenyző fejezte be.")

print("\n3.feladat:", end="")
elitjun = 0
for i in kesz:
    if i.kat == "elit junior":
        elitjun += 1
print(f'Versenyzők száma az "elit junior" kategóriában: {elitjun} fő.')

print("\n4.feladat:", end="")
osszev = 0
for i in kesz:
    osszev += (2014 - i.szulnev)
print(f"A versenyzők átlagos életkora: {osszev/(len(kesz)):.1f}")

kategoria = input("\nKérek egy kategórianevet: ")
van = False
print(f"Rajtszám(ok):", end="")
for i in kesz:
    if kategoria == i.kat:
        print(f"{i.rajtsz} ", end="")
        van = True
if van == False:
    print("Nincs ilyen kategória.")


print("\n6.feladat:", end="")
minido = 555555555555
minindex = ""
for i in kesz:
    if i.nem == "n" and i.osszido < minido:
        minindex = i.vnev
        minido = i.osszido
print(f"A legjobb időt {minindex} érte el.")