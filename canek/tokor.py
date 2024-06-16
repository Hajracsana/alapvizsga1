def KozeptukrozesParos(szoveg):
    hossz=len(szoveg)
    tomb=[]
    for betu in range(len(szoveg)):
        tomb.append(betu)
        print(tomb)
    
bekertSzoveg=""
print("Adjon meg egy értéket vagy tegyen '!' jelet!")
while bekertSzoveg!="!":
    bekertSzoveg=input("Kérek egy szöveget: ")
    if bekertSzoveg!="!":
        KozeptukrozesParos(bekertSzoveg)
        
        
