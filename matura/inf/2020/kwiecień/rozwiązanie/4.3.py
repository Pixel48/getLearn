file = open("../DANE_PR/dane4.txt", "r")

poprzedni = int(file.readline())

krotnosci = dict() # #luka : krotność

for line in file.readlines():
    luka = abs(poprzedni - int(line))
    poprzedni = int(line)

    try:
        krotnosci[luka] += 1
    except KeyError:
        krotnosci[luka] = 1

file.close()

najwieksza_luka = max(krotnosci.values())
raz = True
for klucz in krotnosci:
    if krotnosci[klucz] == najwieksza_luka:
        if raz:
            print("Największa krotność: ", krotnosci[klucz])
            raz = False
        print("Największe luki:", klucz)
