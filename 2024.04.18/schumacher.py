class Versenyzo:
    def __init__(self, sor):
        adatok = sor.strip().split(";")
        self.date = adatok[0]
        self.grandprix = adatok[1]
        self.position = adatok[2]
        self.laps = adatok[3]
        self.points = adatok[4]
        self.team = adatok[5]
        self.status = adatok[6]
        
lista:list[Versenyzo] = []
file = open("schumacher.py", "r", encoding="utf-8")
elsosor = file.readline()
for sor in file:
    lista.append(Versenyzo(sor))
file.close()

print(f"3. feladat: {len(lista)}")

print(f"4. feladat: Magyar nagydíj helyezései:")
for i in lista:
    if i.grandprix == "Hungarian Grand Prix" and i.status == "Finished":
        print(f"\t{i.date} : {i.position}. hely")
        
print(f"5. feladat: Hibasstatisztika")
hibas = {}
for j in lista:
    if j.status not in hibas and j.status != "Finished":
        hibas[j.status] = 1
    else:
        hibas[j.status] += 1

for k, v in hibas.items():
    if v > 2:
        print(f"{k}:{v}")
