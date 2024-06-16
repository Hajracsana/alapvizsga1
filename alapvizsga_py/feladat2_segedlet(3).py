aktido = current[0] * 60 + current[1]

if aktido > ido:
    print('A vizsga már véget ért!')

else:
    print(f'Vizsga hátralevő ideje: {ido-aktido} perc')