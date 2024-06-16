# #1. feladat
# jegyek=[]
# tantargy=input("Kérlek add meg a tantárgy nevét: ")
# while True:
#     jegy=input("Kérlek add meg jegyeidet, ha végeztél, írj '*'-ot!: ")
#     if jegy=="*":
#         break
#     else:
#         jegyek.append(int(jegy))
# atlag=sum(jegyek)/len(jegyek)
# print(f"Az átlagod {tantargy} tantárgyból {atlag:.2f}")

#2. feladat
Nevek=[]
categy=0
catketto=0
catharom=0
while True:
    nev=input("Kérem adjon megy egy nevet: ")
    if nev=="*":
        break
    else:
        Nevek.append(str(nev))
for nev in Nevek:
    if len(nev)<16:
        categy+=1
    elif len(nev)<26:
        catketto+=1
    else:
        catharom+=1
print("Hossz\tDarab")
print(f"0-15\t{categy}")
print(f"16-25\t{catketto}")
print(f"25+\t{catharom}")