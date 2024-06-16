def KozeptukrozesParos(szoveg):
    resz=""
    if szoveg=="!":
        print("Program vége!")
    else:
        for betu in range(fele):
            resz=resz+szoveg[betu]
        for betu in reversed(range(fele)):
            resz=resz+szoveg[betu]
        print(resz.upper())

#páratlan felfelé kerekített! - kisbetűs _)
def KozeptukrozesParatlan(szoveg):
    resz=""
    if szoveg=="!":
        print("Program vége!")
    else:
        for betu in range(fele+1):
            resz=resz+szoveg[betu]
        for betu in reversed(range(fele+1)):
            resz=resz+szoveg[betu]
        print(resz.lower())
    
bekertSzoveg=""
print("Adjon meg egy értéket vagy tegyen '!' jelet!")
while bekertSzoveg!="!":
    bekertSzoveg=input("Kérek egy szöveget: ")
    hossz=len(bekertSzoveg)
    fele=hossz//2
    if hossz==fele*2:
        KozeptukrozesParos(bekertSzoveg)
    else:
         KozeptukrozesParatlan(bekertSzoveg)