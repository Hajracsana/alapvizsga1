# def DejoVagyok():
#     print("De jó vagyok Pythonból!")
# def SokszorKiir(hanyszor, szoveg):
#     for i in range(hanyszor):
#         print(szoveg)

# for i in range(10):
#     DejoVagyok()
    
# SokszorKiir(3, "Egyre jobb vagyok!")
# SokszorKiir(6, "Megy ez nekünk!")

# print(" Adjon meg egy szöveget, és hogy hányszor írjam ki!")
# bekertszoveg=input("Mi legyen a szöveg?")
# bekerthanyszor=int(input("Hányszor írjam ki?"))
# SokszorKiir(bekerthanyszor, bekertszoveg)

# def Osszead(a, b):
#     print(f"A számok összege {a+b}")
#     return a+b
    
# bekertelso=int(input("Mi legyen?: "))
# bekertmasodik=int(input("Mi legyen?: "))
# Osszead(bekertelso, bekertmasodik)

# bekertSzam=45649849874968496846456456498798456456
# aktualisOsszeg=0
# while bekertSzam!=0:
#     bekertSzam=int(input("Adjon meg egy számot(0-t ha végzett): "))
#     aktualisOsszeg=Osszead(aktualisOsszeg, bekertSzam)
    
# def TombOsszeg(szamTomb):
#     osszeg=0
#     for szam in szamTomb:
#         osszeg=osszeg+szam
#     return osszeg

# bekeres=-1
# szamok=[]
# while bekeres !=0:
#     bekeres=int(input("Adjon meg egy számot/0-t ha végzett: "))
#     szamok.append(bekeres)
# szamok.remove(0)
# print(f"A számok összege: {TombOsszeg(szamok)}")

def Szovegfordit(szoveg):
    hossz=len(szoveg)-1
    forditott=" "
    for i in range(hossz, -1, -1):
        forditott=forditott+szoveg[i]
    return forditott
        
randomSzoveg="indul a görög aludni"
forditottSzoveg=Szovegfordit(randomSzoveg)
print(randomSzoveg)
print(forditottSzoveg)