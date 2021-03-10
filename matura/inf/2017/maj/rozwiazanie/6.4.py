with open("../arkusz/Dane_PR/dane.txt") as sorce:
    pixele3D = []
    najdluzszy = 0
    for line in sorce.readlines():
        pixele3D.append(list(map(lambda x: int(x),line.split())))

    licznik = 0
    szerokosc = 0
    while szerokosc < len(pixele3D[0]):
        znacznik = 0
        dlugosc = 0
        ram = pixele3D[0][szerokosc]
        while znacznik < len(pixele3D):
            if pixele3D[znacznik][szerokosc] == ram:
                dlugosc += 1
            else:
                if najdluzszy < dlugosc:
                    najdluzszy = dlugosc
                dlugosc = 1
                ram = pixele3D[znacznik][szerokosc]
            znacznik += 1

        if najdluzszy < dlugosc:
            najdluzszy = dlugosc
        szerokosc += 1
    print("Dlugość najdłuższej linii pionowej:", najdluzszy)
