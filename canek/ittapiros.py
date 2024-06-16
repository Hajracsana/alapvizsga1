import random
penz=0
feltettOsszeg=0
reszOsszesen=0
nyeres=0
opt0=["1","2"]
opt1=["1","2","3"]
opt2=["1","2","3","4","5"]
opt3=["1","2","3","4","5","6","7","8","9","10"]


print("Üdvözöllek a játékban!")
penz=input("Mennyi pénzzel szeretne nekiállni a játéknak?: ")
penz=int(penz)
while True:
    menuselect=input("Kérlek add meg mit szeretnél csinálni! 'e':egyenleg, 'j': játék 'k':Kilépés: ")
    if menuselect=="e":
        print(f"{penz} forint")
    elif menuselect=="k":
        print(f"Köszönöm a játkot, ennyiszer nyertél {nyeres}. Viszlát!")
        break
    elif menuselect=="/add-money":
        penz+=100000000
        print("Fejlesztői beállítás sikeresen aktiválva")
    elif menuselect=="wineeg":
        nyeres+=100000
        print("Fejlesztői beállítás sikeresen aktiválva")
    elif menuselect=="j":
        if penz==0:
            print(f"Sajnálom, elfogyott a rendelkezésre álló kereted. Ennyiszer sikerült nyerned: {nyeres}")
        else:
            hard=input("Kérlek add meg a játék nehézségi szintjét (0,1,2,3): ")
#1. szint
            if hard=="1":
                print("Ebben a nehézségi szintben a poharak száma 3")
                feltettOsszeg=input("Mennyi összeget szeretne feltenni tétnek?: ")
                feltettOsszeg=int(feltettOsszeg)
                if feltettOsszeg<=penz:
                    print(f"Az általad feltett összeg {feltettOsszeg} forint")
                else:
                    while int(feltettOsszeg) > int(penz):
                        print(f"A feltett összeg nagyobb mint a rendelkezésre álló összeg: Ennyit tettél fel: {feltettOsszeg} forint, és ennyid van: {penz} forint")
                        feltettOsszeg=input("Mennyi összeget szeretne feltenni tétnek?: ")
                answer=random.choice(opt1)
                print(answer)
                guess=input("Kérlek add meg melyik pohárra gondoltál: ")
                if guess==answer:
                    print("Gratulálok, nyertél! Az összeged megdupláztuk")
                    nyeres+=1
                    reszOsszesen=feltettOsszeg*2
                    penz+=reszOsszesen
                    print(f"Aktuális egyenleged: {penz}")
                    kerdes=input("Szeretnéd folytatni? (y/n): ")
                    if kerdes=="y": 
                        None
                    else:
                        print("Köszönöm a játékot!")
                        break
                else:
                    print("Sajnálom, vesztettél! A feltett téted levonjuk.")
                    penz-=feltettOsszeg
                    print(f"Aktuális egyenleged: {penz}")
                    if penz>0:
                        kerdes=input("Szeretnéd folytatni? (y/n): ")
                        if kerdes=="y": 
                            None
                        else:
                            print("Köszönöm a játékot!")
                            break
                    elif penz==0:
                        print("Sajnos eljátszottad a pénzed! Köszönöm a játékot!")
                        break
#2. szint
            elif hard=="2":
                print("Ebben a nehézségi szintben a poharak száma 5")
                feltettOsszeg=input("Mekkora összeget szeretne feltenni tétnek?: ")
                feltettOsszeg=int(feltettOsszeg)
                if feltettOsszeg<=penz:
                    print(f"Az általad feltett összeg {feltettOsszeg} forint")
                else:
                    while int(feltettOsszeg) > int(penz):
                        print(f"A feltett összeg nagyobb mint a rendelkezésre álló összeg: Ennyit tettél fel: {feltettOsszeg} forint, és ennyid van: {penz} forint")
                        feltettOsszeg=input("Mekkora összeget szeretne feltenni tétnek?: ")
                answer=random.choice(opt2)
                print(answer)
                guess=input("Kérlek add meg melyik pohárra gondoltál: ")
                if guess==answer:
                    print(f"Gratulálok, nyertél! Az összeged megdupláztuk, nehézségi szint bónusza: {feltettOsszeg*0,25} forint")
                    nyeres+=1
                    reszOsszesen=(feltettOsszeg*2)+(feltettOsszeg*0.25)
                    penz+=reszOsszesen
                    print(f"Aktuális egyenleged: {penz}")
                    kerdes=input("Szeretnéd folytatni? (y/n): ")
                    if kerdes=="y": 
                        None
                    else:
                        print("Köszönöm a játékot!")
                        break
                else:
                    print(f"Sajnálom, vesztettél! A feltett téted levonjuk. Nehézségi szintedre való tekintettel ennyit megtarthatsz: {feltettOsszeg*0,25} forint")
                    penz-=feltettOsszeg-(feltettOsszeg*0.25)
                    print(f"Aktuális egyenleged: {penz}")
                    if penz>0:
                        kerdes=input("Szeretnéd folytatni? (y/n): ")
                        if kerdes=="y": 
                            None
                        else:
                            print("Köszönöm a játékot!")
                            break
                    elif penz==0:
                        print("Sajnos eljátszottad az összes pénzed! Köszönöm a játékot!")
                        break
#3. szint
            elif hard=="3":
                print("Ebben a nehézségi szintben a poharak száma 10")
                feltettOsszeg=input("Mekkora összeget szeretne feltenni tétnek?: ")
                feltettOsszeg=int(feltettOsszeg)
                if feltettOsszeg<=penz:
                    print(f"Az általad feltett összeg {feltettOsszeg} forint")
                else:
                    while int(feltettOsszeg) > int(penz):
                        print(f"A feltett összeg nagyobb mint a rendelkezésre álló összeg: Ennyit tettél fel: {feltettOsszeg} forint, és ennyid van: {penz} forint")
                        feltettOsszeg=input("Mekkora összeget szeretne feltenni tétnek?: ")
                answer=random.choice(opt3)
                print(answer)
                guess=input("Kérlek add meg melyik pohárra gondoltál: ")
                if guess==answer:
                    print(f"Gratulálok, nyertél! Az összeged megdupláztuk, nehézségi szint bónusza: {feltettOsszeg*0,5} forint")
                    nyeres+=1
                    reszOsszesen=feltettOsszeg*2+(feltettOsszeg*0.5)
                    penz+=reszOsszesen
                    print(f"Aktuális egyenleged: {penz}")
                    kerdes=input("Szeretnéd folytatni? (y/n): ")
                    if kerdes=="y": 
                        None
                    else:
                        print("Köszönöm a játékot!")
                        break
                else:
                    print(f"Sajnálom, vesztettél! A feltett téted levonjuk. Nehézségi szintedre való tekintettel ennyit megtarthatsz: {feltettOsszeg*0,5} forint ")
                    penz-=feltettOsszeg-(feltettOsszeg*0.5)
                    print(f"Aktuális egyenleged: {penz}")
                    if penz>0:
                        kerdes=input("Szeretnéd folytatni? (y/n): ")
                        if kerdes=="y": 
                            None
                        else:
                            print("Köszönöm a játékot!")
                            break
                    elif penz==0:
                        print("Sajnos eljátszottad az összes pénzed! Köszönöm a játékot!")
                        break
#0. szint
            elif hard=="0":
                print("Ebben a nehézségi szintben a poharak száma 2")
                feltettOsszeg=input("Mennyi összeget szeretne feltenni tétnek?: ")
                feltettOsszeg=int(feltettOsszeg)
                if feltettOsszeg<=penz:
                    print(f"Az általad feltett összeg {feltettOsszeg} forint")
                else:
                    while int(feltettOsszeg) > int(penz):
                        print(f"A feltett összeg nagyobb mint a rendelkezésre álló összeg: Ennyit tettél fel: {feltettOsszeg} forint, és ennyid van: {penz} forint")
                        feltettOsszeg=input("Mekkora összeget szeretne feltenni tétnek?: ")
                answer=opt1[1]
                guess=input("Kérlek add meg melyik pohárra gondoltál (addig fog újratölteni a kérdés amíg nem találod el.): ")
                while guess!=answer:
                    print("Micsoda hihetetlen véletlen, nyertél! Az összeged megdupláztuk, és mivel ilyen jó vagy +50 forint üti a markod.")
                    nyeres+=1
                    reszOsszesen=feltettOsszeg*2+50
                    penz+=reszOsszesen
                    print(f"Aktuális egyenleged: {penz} forint")
                    kerdes=input("Szeretnéd folytatni? (y/n): ")
                    if penz>0:
                        kerdes=input("Szeretnéd folytatni? (y/n): ")
                        if kerdes=="y": 
                            None
                        else:
                            print("Köszönöm a játékot!")
                            break
                    elif penz==0:
                        print("Sajnos eljátszottad az összes pénzed! Szerencsejátékfüggő! Köszönöm a játékot!")
                        break