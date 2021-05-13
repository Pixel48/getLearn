def pierwsza(n):
    if n < 2:
        return False
    else:
        for x in range(2, (n // 2) + 1):
            if not (n % x):
                print(x)
                return False

        return True


n = 83

if pierwsza(n):
    print("podana liczba jest pierwszą")
else:
    print("podana liczba NIE jest pierwszą")