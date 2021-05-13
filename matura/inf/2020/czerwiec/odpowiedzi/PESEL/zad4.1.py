def czy_pierwsza(x):
    if x == 2:
        return True
    for i in range(3, x // 2 + 1):
        if x % i == 0:
            return False
    return True


def podaj_liczby_pierwsze(szukana):
    for pierwsza in range(3,szukana):
        if czy_pierwsza(pierwsza):
            druga = szukana - pierwsza
            if czy_pierwsza(druga):
                return [pierwsza, druga]

        else:
            continue



plik = open("2020 czerwiec rozszerzenie/Dane_PR2/pary.txt")
odpowiedz = open("2020 czerwiec rozszerzenie/PESEL/wyniki4.txt", "a+")

odpowiedz.write("Zadanie 4.1")

for linia in plik.readlines():

    liczba = int(linia.split()[0])
    if liczba % 2 or liczba < 4:
        continue
    else:
        a, b = podaj_liczby_pierwsze(liczba)
        odpowiedz.write("\n\t"+ str(liczba) + " " + str(a) + " " + str(b))

plik.close()
odpowiedz.close()
