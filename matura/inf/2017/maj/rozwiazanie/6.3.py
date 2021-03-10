with open("../arkusz/Dane_PR/dane.txt") as sorce:
    pixele3D = []
    kontrastujacych = 0

    for line in sorce.readlines():
        pixele3D.append(list(map(lambda x: int(x),line.split())))

    for idLinii, line in enumerate(pixele3D):
        for id, pixel in enumerate(line):
            if id > 0:
                if pixele3D[idLinii][id - 1] > pixel + 128 or pixele3D[idLinii][id - 1] < pixel - 128:
                        kontrastujacych += 1
                        continue

            if id + 1 < len(line):
                if pixele3D[idLinii][id + 1] > pixel + 128 or pixele3D[idLinii][id + 1] < pixel - 128:
                    kontrastujacych += 1
                    continue
            if idLinii > 0:
                if pixele3D[idLinii-1][id] > pixel + 128 or pixele3D[idLinii-1][id] < pixel - 128:
                    kontrastujacych += 1
                    continue
            if idLinii + 1 < len(pixele3D):
                if pixele3D[idLinii + 1][id] > pixel + 128 or pixele3D[idLinii + 1][id] < pixel - 128:
                    kontrastujacych += 1
                    continue

    print(kontrastujacych)
