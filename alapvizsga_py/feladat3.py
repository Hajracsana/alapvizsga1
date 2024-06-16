class Pelda:

    def __init__(self,row: str) -> None:
            splitted = row.strip().split(';')
            self.nev = splitted[0]
            self.pelda = splitted[1]
            self.matek = splitted[2]
            self.magyar = splitted[3]
            self.tori = splitted[4]
            self.info = splitted[5]
            self.angol = splitted[6]

#########

pelda_lista : list[Pelda] = []


def load_from_file(filename: str) -> None:
    file = open(filename, 'r', encoding='utf8')
    file.readline()
    for row in file:
        pelda_lista.append(Pelda(row))
    file.close()

load_from_file('pelda.csv')


stat = {}
for t in pelda_lista:
    if t.pelda not in stat.keys():
        stat[t.pelda] = 1
    else:
        stat[t.pelda] += 1

    for key,value in stat.items():
        if key[0] == '8':
            print(f'\t{key} osztály: {value} fő')

def dict() -> dict:
    stat = {}
    for t in vb_lista:
        if t.valtozas not in stat:
            stat[t.valtozas] = 1
        else:
            stat[t.valtozas] += 1

    for key,value in stat.items():
        if value > 1:
            print(f'\t{key} helyet változott: {value} csapat')
