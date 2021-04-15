def babelkowe(tab):
    flaga = True

    while flaga:
        flaga = False
        for i in range(0, len(tab) - 1):
            if tab[i] > tab[i + 1]:
                flaga = True
                ram = tab[i]
                tab[i] = tab[i + 1]
                tab[i + 1] = ram


def kubelkowe(tab, maxLiczba):
    zakres = maxLiczba / len(tab)
    kubelki = {x * zakres + zakres: []
               for x in range(0, len(tab))}

    for liczba in tab:
        for klucz in kubelki:
            if liczba < klucz:
                kubelki[klucz].append(liczba)
                break

    tab.clear()

    for kluczKubelka in kubelki:
        if len(kubelki.get(kluczKubelka)) > 1:
            babelkowe(kubelki.get(kluczKubelka))
        for liczba in kubelki.get(kluczKubelka):
            tab.append(liczba)
    return tab


tablica = [6, 8, 2, 1, 4, 5, 3]

print(tablica)
kubelkowe(tablica, max(tablica) + 1)

print(tablica)
