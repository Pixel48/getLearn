with open("../arkusz/Dane_PR/dane.txt") as sorce:
    doUsuniecia = 0
    for line in sorce.readlines():
        pixele = line.split()
        i = 0
        j = len(pixele)-1
        while i < j:
            if pixele[i] != pixele[j]:
                doUsuniecia += 1
                break
            i += 1
            j -= 1
    print(f"Należy usunąć: {doUsuniecia} pixeli")
