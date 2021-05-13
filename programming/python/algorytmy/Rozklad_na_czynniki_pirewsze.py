from math import sqrt


def rozklad(n):
    k = 2

    while n > 1 and k <= sqrt(n):
        while n % k == 0:
            print(f"{n} | {k}")
            n /= k
        k += 1

    if n > 1:
        print("reszta", n)
    else:
        print(1)

rozklad(1245)
