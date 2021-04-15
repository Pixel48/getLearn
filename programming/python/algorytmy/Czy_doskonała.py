from math import sqrt

def doskonala(n):
    suma = 1
    pier = int(sqrt(n))
    for x in range(2, pier + 1):
        if n % x == 0:
            suma += x + n // x

    if n == pow(pier, 2):
        suma -= pier

    if suma == n:
        return True
    else:
        return False


def doskonala_mniej_wydajny(n):
    suma = 1
    for x in range(2, n):
        if suma > n:
            return False

        if n % x == 0:
            suma += x
    if suma == n:
        return True
    else:
        return False


# print(doskonala_mniej_wydajny(int(input("Podaj liczbe do sprawdzenia:"))))
print(doskonala(int(input("Podaj liczbe do sprawdzenia:"))))
