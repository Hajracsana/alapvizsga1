class Hianyzasok:
    def __init__(self, sor):
        adatok = sor.strip().split(";")
        self.nev = adatok[0]
        self.osztaly = adatok[1]
        self.elsonap = int(adatok[2])
        self.utolsonap = int(adatok[3])
        self.mulasztottorak = int(adatok[4])
        
lista: list[Hianyzasok] = []
file = open("szeptember.csv", "r")
fejlec = file.readline()

for i in file:
    lista.append(Hianyzasok(i))
file.close()

hiany = 0
for i in lista:
    hiany += i.mulasztottorak

print(f"2. feladat: Összes mulasztott órák száma: {hiany} óra")

print("3. feladat")
nap = int(input("Adjon meg egy napot 1 és 30 között: "))
tanulonev = input("Adja meg egy tanuló nevét: ")

volt = False
print("4. feladat")
for i in lista:
    if tanulonev == i.nev:
        volt = True                            
        break
if volt:
    print("hianyzott")
else:
    print("Nem hianyzott")
    
print(f"5. feladat: Hiányzik 2017.09.{nap}. -n")
hianyzas = False
for i in lista:
    if nap == i.elsonap or nap == i.utolsonap:
        hianyzas = True
        print(f"{i.nev} ({i.osztaly})")
if hianyzas == False:
    print("Nem volt hianyzo")
    
szotar = {}
for i in lista:
    if i.osztaly not in szotar:
        szotar[i.osztaly] = 1
    else:
        szotar[i.osztaly] += 1
        
file = open("osszesites.csv", "w", encoding="utf-8")
for i in szotar:
    file.write(f"{i};{szotar[i]}\n")