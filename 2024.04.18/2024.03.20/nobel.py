class Nobel:
    def __init__(self, sor):
        adatok = sor.strip().split(";")
        self.ev = int(adatok[0])
        self.tipus = adatok[1]
        self.keresztnev = adatok[2]
        self.vezeteknev = adatok[3]
        
nobel:list[Nobel] = []
file = open("nobel.csv", "r", encoding="utf-8")
fejlec = file.readline()
for sor in file:
    nobel.append(Nobel(sor))
file.close()

for i in nobel:
    if i.keresztnev == "Arthur B." and i.vezeteknev == "McDonald":
        print(f"3. feladat: {i.tipus}")

for i in range(len(nobel)):
    if nobel[i].ev == 2017 and nobel[i].tipus == "irodalmi":
        print(f"4. feladat: {nobel[i].keresztnev} {nobel[i].vezeteknev}")
        
print("5. feladat: ")
for i in nobel:
    if i.ev >1990 and i.tipus =="béke" and i.vezeteknev== "":
        print(f"{i.ev}: {i.keresztnev}")

print("6. feladat:")        
for i in nobel:
    if "Curie" in i.vezeteknev:
        print(f"\t{i.ev}: {i.keresztnev} {i.vezeteknev} {i.tipus}")

print("7. feladat")        
stat = {}
for i in nobel:
    if i.tipus not in stat:
        stat[i.tipus] = 1
    else:
        stat[i.tipus] += 1
for k,v in stat.items():
    print(f"\t{k} - {v}")
    
file = open("orvosi.txt", "w", encoding="utf-8") 
for n in nobel:
    if n.tipus == "orvosi":
        file.write(f"{n.ev} : {n.keresztnev} {n.vezeteknev}\n")   