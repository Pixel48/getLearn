odpowiedz = open("2020 czerwiec rozszerzenie/PESEL/wyniki4.txt", "a+")
plik = open("2020 czerwiec rozszerzenie/Dane_PR2/pary.txt")
odpowiedz.write("\n\n 4.2")
for linia in plik.readlines():
    slowo = linia.split()[1]

    dlugosc = 0
    najdluzszy = 1
    ldluga = slowo[0]
    ostatnia = ""
    for litera in slowo:
        if litera != ostatnia:

            if dlugosc > najdluzszy:
                najdluzszy = dlugosc
                ldluga = ostatnia
            ostatnia = litera
            dlugosc = 1
        else:
            dlugosc += 1
    if dlugosc > najdluzszy:
        najdluzszy = dlugosc
        ldluga = ostatnia

    odpowiedz.write("\n\t")
    for ile in range(1, najdluzszy+1):
        print(ldluga)
        odpowiedz.write(ldluga)
    odpowiedz.write(" " + str(najdluzszy))
plik.close()
odpowiedz.close()
