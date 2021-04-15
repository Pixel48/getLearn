def horner(wsp, st, x):
    if st == 0:
        return wsp[0]
    else:
        return x * horner(wsp, st - 1, x) + wsp[st]


stopien = int(input("Podaj stopień wielomianu: "))

wspolczynnik = []
for i in range(0, stopien):
    wspolczynnik.append(int(input(f"Podaj współczynnik stojący przy potędze: ")))

wspolczynnik.append(int(input("Podaj wyraz wolny: ")))
argument = int(input("Podaj argument: "))

print("W(", argument, ") = ", horner(wspolczynnik, stopien, argument))
