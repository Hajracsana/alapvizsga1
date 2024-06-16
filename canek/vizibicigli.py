class BINYIGLI:
    def __init__(self, sor):
        adatok = sor.strip().split(";")
        self.nev = adatok[0]
        self.jaz = adatok[1]
        self.eora = (adatok[2])
        self.eperc = (adatok[3])
        self.vora = (adatok[4])
        self.vperc = (adatok[5])
        self.eossz=self.eora*60+self.eperc
        self.vossz=self.vora*60+self.vperc

bicigli = []

with open("kolcsonzesek.txt", "r", encoding="utf-8") as file:
    file.readline()
    for sor in file:
        bicigli.append(BINYIGLI(sor))

print(f"5. feladat: {len(bicigli)}")
print('6. feladat')
van=False
nev=input("Adjon meg egy nevet: ")
for i in bicigli:
    if nev in i.nev:
        van=True
        print(f'{i.eora}:{i.eperc} - {i.vora}:{i.vperc}')
if van==False:
    print("ERRORAdri")
print('7.feladat')
beido=input('Kérem az időt: ').split(":")
ora=int(beido[0])
perc=int(beido[1])
beossz=ora*60+perc
for sor in bicigli:
    if sor.eossz<=beossz and sor.vossz>=beossz:
        print(f'{sor.eora}:{sor.eperc} - {sor.vora}:{sor.vperc} : {sor.nev}')