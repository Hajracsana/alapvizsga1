def szamol_neveket():
    nevek = set()
    while True:
        beirtNev = input("Adjon meg egy nevet: ").upper()
        if beirtNev == "":
            break
        nevek.add(beirtNev)
    print(f"Ennyi különböző név van: {len(nevek)}")

szamol_neveket()
