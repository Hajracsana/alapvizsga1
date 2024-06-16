def Osszead(a,b):
    print("Ön az 'Összeadás' programot válsztotta")
    osszeg=a+b
    return osszeg
def Kivon(a,b):
    print("Ön az 'Kivonás' programot válsztotta")
    osszeg=a-b
    return osszeg
def Szorzas(a,b):
    print("Ön az 'Szorzás' programot válsztotta")
    osszeg=a*b
    return osszeg
def Osztas(a,b):
    print("Ön az 'Osztás' programot válsztotta")
    if b<1:
        print("Ellenőrizze az értéket!")
    else:
        osszeg=a/b
        osszeg=float(osszeg)
        return osszeg



print("---------------------------------------")
print("Az első saját programom v1.0")
a=input("Kérem adja meg az első számot: ")
b=input("Kérem adja meg a második számot: ")
print(Osztas(int(a),int(b)))