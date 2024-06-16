import random

def megtett_mezok():
    return random.randint(1, 3)

def verseny():
    autok = [1, 2]
    nyertes = None
    vesztes = None
    while nyertes is None:
        for auto in autok:
            auto_mezo = megtett_mezok()
            print("*" * auto_mezo, end=" ")
            if auto_mezo >= 60:
                nyertes = auto
                vesztes = autok[autok.index(auto) - 1]
                break
        print()
    print(f"A(z) {nyertes}. autó nyert, a vesztes autó {megtett_mezok()} mezőn tartózkodott a nyertes célba jutásának időpontjában.")

def bajnoksag():
    eredmenyek = []
    nyertes=""
    while True:
        verseny()
        eredmenyek.append(nyertes)
        if eredmenyek.count(eredmenyek[-1]) == 3:
            break
    print("Az összes futam alakulása:", eredmenyek)
    print(f"A bajnok az {eredmenyek[-1]}. autó!")