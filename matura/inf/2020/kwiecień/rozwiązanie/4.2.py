file = open("../DANE_PR/dane4.txt", "r")

poprzednia = int(file.readline())  # #Poprzednia liczba
poprzednia_luka = 0  # #Luka w poprzedniej parze liczb
dlugosc = 1
poczatek = file.readline()


naj_poczatek = poczatek  # #Początek najdłuższego ciągu
koniec = ""  # #Koniec najdłuższego ciągu
naj_dlugosc = 0  # #Gługość najdłuższego ciągu

for line in file.readlines():
    luka = abs(poprzednia - int(line))

    if luka != poprzednia_luka:  # #Gdy przerwie ciąg

        if dlugosc > naj_dlugosc:  # #Gdy znajdzie nowy najdłuższy ciąg
            koniec = poprzednia
            naj_poczatek = poczatek
            naj_dlugosc = dlugosc

        # #Zerowanie dla nowego ciągu
        dlugosc = 1
        poprzednia_luka = luka
        poczatek = poprzednia
    dlugosc += 1
    poprzednia = int(line)

file.close()
print("Początek najdłuższego ciągu: ", naj_poczatek)
print("Koniec najdłuższego ciągu: ", koniec)
print("Długość: ", naj_dlugosc)
