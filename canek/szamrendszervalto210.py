def Valtas210(szam):
    kettes = ""
    szam=int(szam)
    while szam > 0:
        kettes = str(szam % 2) + kettes
        szam = szam // 2
    return kettes

def Valtas102(szam):
    szam=""
    tizes = 0
    hossz = len(szam)
    for i in range(hossz):
        tizes += int(szam[i]) * 2 ** (hossz - 1 - i)
    return tizes

valasztas=""
dontes=""
kertszam=0


while valasztas!="STOP":
        valasztas=input("Kérem adja meg mit szeretne tenni (2-10;10-2;STOP): ")
        if valasztas=="2-10":
            kertszam=input("Adjon meg egy számot amivel dolgozni szeretne: ")
            kertszam=int(kertszam)
            print(Valtas210(kertszam))
        elif valasztas=="10-2":
            kertszam=input("Adjon meg egy számot amivel dolgozni szeretne: ")
            kertszam=str(kertszam)
            print(Valtas102(kertszam))
        elif valasztas=="STOP":
            print("Köszönöm, hogy a programot használta! Kérem értékelje csillagok megadásával (1-3 csillag)")
            csillagok=input("")
            if csillagok=="*":
                print(":(")
            elif csillagok=="**":
                print(":/")
            elif csillagok=="***":
                print(":)")
            elif csillagok=="STOP":
                print("Kérdőív vége")
            else:
                print("Kérem csillagokat adjon meg, ammenyiben nem szeretne értékelni írjon 'STOP'ot")
        else:
            print("Hibás érték!")
