#Írj egy függvényt, amely paraméterül 2 értéket kap
#egy sávszélesség értéket Megabit-ben
#és egy fájlméretet Megabájtban
#A függvény számolja ki, hogy az adott fájl
#mennyi idő alatt tölthető le (óra, perc, mp)
#kérj be felhasználói adatokat, amíg azt nem írja, hogy "vége"
#kérj be egy sávszélességet, majd egy fájlméretet
#hívd meg a függvényt a bekért adatokkal

def LetoltesSzamitoKetyere(sav, meret):
    mp=meret*8/sav
    h=mp//3600
    m=(mp%3600)/60
    masod=mp%60
    print(f"Elvtárs, ennyi idő alatt töltheted le: {int(h)}h {int(m)}m {int(masod)}s")
    
print("-------------v1.0.0------------")      
print("Letöltés idő számító szerkezet. v1.0.0")
inditasjelzes=""
inditasjelzes=input("Mehet?(Ok/vége)")
while inditasjelzes=="vége":
    if inditasjelzes=="Ok":
        savszel=int(input("Welcome Comrade! Adja meg sávszélességét (Mbps): "))
        filesize=int(input("Most következzen a letöltendő file mérete (MB): "))
        LetoltesSzamitoKetyere(savszel, filesize)
        print("Nagyon szívesen! Buksisimogatásra igényt itt: czanek.balint@students.jedlik.eu")
        print("-------------v1.0.0------------")    
    elif inditasjelzes=="vége":
        print("Feladat vége! A soviet unio bannolt.")