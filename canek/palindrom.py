def NoSpace(szoveg):
    eredmeny=""
    for betu in szoveg:
        if betu != " ":
            eredmeny=eredmeny+betu
    return eredmeny

def Palindrom(szoveg):
    szoveg=NoSpace(szoveg)
    hossz=len(szoveg)
    for i in range(hossz//2):
        if szoveg[i]!=szoveg[hossz-(i+1)]:
            return False
    return True
            

bekertSzoveg=""
print("Adjon meg szövegeket, vagy 'q' betűt, ha végzett!")
while bekertSzoveg!="q":
    bekertSzoveg=input("Kérek egy szöveget: ")
    if bekertSzoveg!="q":
        if Palindrom(bekertSzoveg):
            print("A megadott szöveg palindrom típusú")
        else:
            print("A megadott szöveg nem palindrom típusú")        