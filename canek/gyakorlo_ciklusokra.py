import random
# #Faktoriális
# def faktorialis(szam):
#     if szam == 0:
#         return 1
#     else:
#         return szam * faktorialis(szam-1)

# szam = int(input("Adjon meg egy pozitív egész számot: "))
# print(f"{szam}!=" + str(faktorialis(szam)))

# #Előtte páratlan összead
# def paratlan_osszeg(szam):
#     osszeg = 0
#     for i in range(1, szam+1, 2):
#         osszeg = osszeg+i
#     return osszeg
# szam=int(szam)
# szam = int(input("Adjon meg egy pozitív egész számot: "))
# print(f"A {str(szam)}-nál/nél nem nagyobb páratlan számok összege: "+str(paratlan_osszeg(szam)))

# #Beolvasás     
# BeolvasottSzamok = []
# beolvasottSzam = None
# while beolvasottSzam != 0:
#     beolvasottSzam = int(input("Kérem adjon meg számokat, és ha végzett írjon 0-t!: "))
#     if beolvasottSzam != 0:
#         BeolvasottSzamok.append(beolvasottSzam)
        
# for szam in BeolvasottSzamok:
#     szam+=szam
#     osszeg=szam
# legnagyobb=max(BeolvasottSzamok)
# legkisebb=min(BeolvasottSzamok)
# darab=len(BeolvasottSzamok)
# atlag=(osszeg/darab)*100
# print(f"A számok összege: {osszeg}")
# print(f"A számok átlaga: {atlag}")
# print(f"A számok közül a legksiebb: {legkisebb}")
# print(f"A számokok közül a legnagyobb: {legnagyobb}")
# print(f"Ennyi szám van: {darab}")

# #Karakter bekérő
# szamlalo = 0
# while True:
#     karakter = input("Kérem adjon meg EGY karaktert: ")
#     if len(karakter) != 1:
#         print("Csak egy karaktert adjon meg!")
#     elif karakter == "@":
#         break
#     else:
#         szamlalo += 1

# print(f"Összesen {szamlalo} karaktert adott meg.")

#Tipp 
userguess=random.randint(1,1000)
print(f"A teszt érdekében a random szám: {userguess}")
tipp = int(input("Tippeljen egy számot 1 és 1000 között: "))
lepesek_szama = 1

while tipp != userguess:
    if tipp < userguess:
        print("A kitalált szám nagyobb.")
    else:
        print("A kitalált szám kisebb.")
    tipp = int(input("Tippelj újra: "))
    lepesek_szama += 1

print(f"Talált! {lepesek_szama} lépésből találtad ki a számot.")
