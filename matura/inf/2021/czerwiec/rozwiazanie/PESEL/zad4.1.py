zestawienie = dict()
with open("../Dane_2103/galerie.txt", "r") as sorce:
    for linia in sorce.readlines():
        kod = linia.split()[0]

        if kod in zestawienie:
            zestawienie[kod] += 1
        else:
            zestawienie[kod] = 1

for x in zestawienie:
    print(x, zestawienie[x])