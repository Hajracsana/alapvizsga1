def beker(uzenet,min,max):
    valasz = int(input(f"{uzenet}: "))
    while valasz < min or valasz > max:
        print(f'{min} és {max} közötti értéket adjon meg: ')
        valasz = int(input(f'{uzenet}: '))
    return valasz