wielkoscNajwiekszej = 0
miastoZNajwieksza = ""

wielkoscNajmniejszej = 99999
miastoZNajmniejsza = ""
with open("../Dane_2103/galerie.txt", "r") as sorce:
    for linia in sorce.readlines():
        wymiary = linia.split()[2:]

        iterator = 70*2
        objetosc = 0
        lokali = 0
        miasto = linia.split()[1]

        while iterator >= 0:

            iterator -= 2
            if wymiary[iterator] == "0":
                pass
            else:
                lokali += 1
                objetosc += int(wymiary[iterator]) * int(wymiary[iterator + 1])

        print(miasto, objetosc, lokali)

        if objetosc > wielkoscNajwiekszej:
            wielkoscNajwiekszej = objetosc
            miastoZNajwieksza = miasto

        if objetosc < wielkoscNajmniejszej:
            wielkoscNajmniejszej = objetosc
            miastoZNajmniejsza = miasto

print("\n", miastoZNajwieksza, wielkoscNajwiekszej)
print(miastoZNajmniejsza, wielkoscNajmniejszej)