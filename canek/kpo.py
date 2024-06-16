import random
opciok=["kő","papír","olló"]
def Jatekos1(lista):
    lepes=random.choice(lista)
    return lepes
    
def Jatekos2(lista2):
    lepes2=random.choice(lista2)
    return lepes2

egyes=Jatekos1(opciok)
kettes=Jatekos2(opciok)
if egyes=="kő" and kettes=="olló":
    print("Egyes játékos nyert")
elif egyes=="olló" and kettes=="kő":
    print("Kettes játékos nyert")

if egyes=="papír" and kettes=="kő":
    print("Egyes játékos nyert")
elif egyes=="kő" and kettes=="papír":
    print("Kettes játékos nyert")

if egyes=="olló" and kettes=="papír":
    print("Egyes játékos nyert")
elif egyes=="papír" and kettes=="olló":
    print("Kettes játékos nyert")

if egyes==kettes:
    print("Döntetlen")