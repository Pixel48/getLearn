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


tab = [2, 6, 1, 8, 3, 6, 3, 7, 8, 3]

babelkowe(tab)
print(tab)
