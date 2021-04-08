
with open("../Dane_PR2/pary.txt") as file:
    najmniejsza_para = file.readline().split() #początkowa wartość

    for linia in file.readlines():
        linia = linia.split()

        if len(linia[1]) == int(linia[0]):

            if int(linia[0]) < int(najmniejsza_para[0]):
                najmniejsza_para[0] = linia[0]
                najmniejsza_para[1] = linia[1]

            elif int(linia[0]) == int(najmniejsza_para[0]):
                index = 0
                while index < len(linia[1]) and index < len(najmniejsza_para[1]):
                    if ord(linia[1][index]) < ord(najmniejsza_para[1][index]):
                        najmniejsza_para[0] = linia[0]
                        najmniejsza_para[1] = linia[1]
                        break
                    index += 1
    print(najmniejsza_para)