def wstawieanie(n):
    for i in range(1, len(n)):
        ram = n[i]
        j = i - 1

        while j >= 0 and n[j] > ram:
            n[j + 1] = n[j]
            j -= 1
        n[j + 1] = ram


tab = [6, 8, 2, 1, 9, 5, 3]

wstawieanie(tab)
print(tab)