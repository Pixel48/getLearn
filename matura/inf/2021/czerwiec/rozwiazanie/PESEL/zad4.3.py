najwiecej = 0
Mnajwiecej = ""

najmniej = 1000
Mnajmniej = ""

with open("../Dane_2103/galerie.txt", "r") as sorce:
    for linia in sorce.readlines():
        wymiary = linia.split()[2:]

        iterator = 70*2
        miasto = linia.split()[1]
        l_objentosci = list()
        ile_rodzaji = 0

        while iterator >= 0:

            iterator -= 2
            if wymiary[iterator] == "0":
                pass
            else:
                objetosc = int(wymiary[iterator]) * int(wymiary[iterator + 1])

                if objetosc in l_objentosci:
                    pass
                else:
                    l_objentosci.append(objetosc)
                    ile_rodzaji += 1

        if ile_rodzaji > najwiecej:
            najwiecej = ile_rodzaji
            Mnajwiecej = miasto

        if ile_rodzaji < najmniej:
            najmniej = ile_rodzaji
            Mnajmniej = miasto

print(Mnajwiecej, najwiecej)
print(Mnajmniej, najmniej)