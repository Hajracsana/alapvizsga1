import random

# A felhasználó által megadott arányok
szarazfold_arany = int(input("Adja meg a szárazföld arányát (0-100): "))
viz_arany = 100 - szarazfold_arany

# Piroska ugróképessége
ugro_kepesseg = int(input("Adja meg Piroska ugróképességét: "))

# Az ösvény hossza
osveny_hossz = 100

# Az ösvényt reprezentáló lista
osveny = [1] + [random.choices([1, 2], weights=[szarazfold_arany, viz_arany])[0] for _ in range(osveny_hossz-2)] + [1]

# Az ösvény megjelenítése
print(''.join(['#' if elem == 1 else '_' for elem in osveny]))

# Piroska átkelési képességének ellenőrzése
viz_szamlalo = 0
max_viz_szamlalo = 0

for elem in osveny:
    if elem == 2:
        viz_szamlalo += 1
        max_viz_szamlalo = max(max_viz_szamlalo, viz_szamlalo)
    else:
        viz_szamlalo = 0

if max_viz_szamlalo > ugro_kepesseg:
    print("Piroska nem tud átkelni az ösvényen száraz lábbal.")
else:
    print("Piroska át tud kelni az ösvényen száraz lábbal.")
