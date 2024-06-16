import random
def milliomos_jatek():
    kerdesek = [
        {"kerdes": "Melyik egy nemzetközi hírnevű magyar étel neve?", "valaszok": ["kanász", "kondás", "gulyás", "pörkölt"], "helyes": 2},
        {"kerdes": "Milyen pitypangnak hívják a gyermekláncfüvet?", "valaszok": ["pongyola", "patyolat", "pipogya", "pamacs"], "helyes": 0},
        {"kerdes": 'Egészítsd ki a híres novella címét! "Mario és a ........."', "valaszok": ["boszorkány", "varázsló", "kiválasztott", "herceg"], "helyes": 1},
        {"kerdes": "Mit neveztek régen indóháznak?", "valaszok": ["festőműhelyt", "telefonközpontot", "vasútállomást", "postaállomást"], "helyes": 2},
        {"kerdes": "Ki rendezte az Titanic című 1997-ben készült filmet?", "valaszok": ["Steven Spielberg", "Ridley Scott", "James Cameron", "Quentin Tarantino"], "helyes": 2},
        {"kerdes": "Melyik Erkel operában hangzik el a Palotás?", "valaszok": ["Hunyadi László", "Bánk Bán", "Dózsa György", "István király"], "helyes": 1},
        {"kerdes": 'Milyen mára elavult jelentése volt évszázadokkal ezelőtt a "marha" szónak?', "valaszok": ["vagyon", "család", "ügyetlen", "szamár"], "helyes": 0},
        {"kerdes": "Mennyi a fény terjedési sebessége levegőben, légüres térben?", "valaszok": ["300 000 km/h", "300 000 km/s", "30 000 m/s", "3 000 000 m/s"], "helyes": 1},
        {"kerdes": "Milyen állat a kazuár?", "valaszok": ["hüllő", "macskaféle", "madár", "emlős"], "helyes": 2},
        {"kerdes": "Hányszor kell körbejárnia egy iszlám hívőnek Mekkában a Kába-követ?", "valaszok": ["hétszer", "ötször", "háromszor", "kétszer"], "helyes": 0},
        {"kerdes": "Melyik sportág kiválósága volt Varjú Vilmos?", "valaszok": ["birkózás", "ökölvívás", "súlylökés", "úszás"], "helyes": 1},
        {"kerdes": "Milyen nemzetiségű volt Jean Sibelius zeneszerző?", "valaszok": ["német", "belga", "finn", "svéd"], "helyes": 2}
    ]

    segitsegek = ["felező", "közönség", "telefon"]

    for i, kerdes in enumerate(kerdesek):
        print(f"\n{i+1}. kérdés: {kerdes['kerdes']}")
        for j, valasz in enumerate(kerdes['valaszok']):
            print(f"{j+1}. {valasz}")
        segitseg = input("Szeretnél segítséget kérni? (I/N): ")
        if segitseg.lower() == "i" and segitsegek:
            print("Elérhető segítségek: ", segitsegek)
            melyik_segitseg = input("Melyik segítséget szeretnéd kérni? ")
            if melyik_segitseg in segitsegek:
                segitsegek.remove(melyik_segitseg)
                if melyik_segitseg == "felező":
                    helytelen_valasz = random.choice([v for v in range(4) if v != kerdes['helyes']])
                    print("A felező segítség után maradt válaszok: ")
                    for v in [kerdes['helyes'], helytelen_valasz]:
                        print(f"{v+1}. {kerdes['valaszok'][v]}")
                elif melyik_segitseg == "közönség":
                    print("A közönség szavazatai alapján a legtöbben a következő választ ajánlják: ", kerdes['valaszok'][kerdes['helyes']])
                elif melyik_segitseg == "telefon":
                    print("A telefonos segítség szerint a helyes válasz: ", kerdes['valaszok'][kerdes['helyes']])
        valasztas = int(input("Válaszod (1-4): ")) - 1
        if valasztas == kerdes['helyes']:
            print("Helyes válasz!")
        else:
            print("Sajnos nem találtad el.")
            break

milliomos_jatek()
