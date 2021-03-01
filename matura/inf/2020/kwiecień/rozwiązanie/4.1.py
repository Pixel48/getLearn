file = open("../DANE_PR/dane4.txt", "r")

poprzedni = int(file.readline())

najmniejsza = ""
najwieksza = 0

for line in file.readlines():
    luka = abs(poprzedni - int(line))
    poprzedni = int(line)

    if luka > najwieksza:
        najwieksza = luka

    if type(najmniejsza) == str or luka < najmniejsza:
        najmniejsza = luka

file.close()

print("Najmniejsza luka: ", najmniejsza)
print("Największa luka: ", najwieksza)
