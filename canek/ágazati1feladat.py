import math
import random
def Felszin(meret):
    felszin=(meret/2)*(meret/2)*math.pi
    return felszin

atmero=int(input("Kérem a medence átmérőjét: "))
szinek=["kék","zöld","lila","hupikék"]
print(f"A medence színe: {random.choice(szinek)}")
print(f"A takarófólia mérete: {Felszin(atmero)} m^2")
#feladat anyniban tér el hogy egy Luxusórára kell üvegfólia -- 8 pontot ér