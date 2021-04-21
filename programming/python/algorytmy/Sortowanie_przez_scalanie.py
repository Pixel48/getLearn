def podziel(tablica):

    if len(tablica) > 1:

        mid = len(tablica) // 2
        lewa = podziel(tablica[:mid])
        prawa = podziel(tablica[mid:])
        return scal(lewa, prawa)

    else:
        return tablica


def scal(lewa, prawa):
    iLewa = 0
    iPrawa = 0
    chwilowaTab = []

    while iLewa < len(lewa) and iPrawa < len(prawa):
        if lewa[iLewa] < prawa[iPrawa]:
            chwilowaTab.append(lewa[iLewa])
            iLewa += 1
        else:
            chwilowaTab.append(prawa[iPrawa])
            iPrawa += 1

    while iLewa < len(lewa):
        chwilowaTab.append(lewa[iLewa])
        iLewa += 1

    while iPrawa < len(prawa):
        chwilowaTab.append(prawa[iPrawa])
        iPrawa += 1

    return chwilowaTab
