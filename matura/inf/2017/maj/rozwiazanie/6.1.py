with open("../arkusz/Dane_PR/dane.txt") as sorce:
    najjasniejszy = 0
    najciemniejszy = 255
    for line in sorce.readlines():
        for pixel in line.split():
            if najjasniejszy < int(pixel):
                najjasniejszy = int(pixel)
            if najciemniejszy > int(pixel):
                najciemniejszy = int(pixel)
print("Najciemniejszy pixel:",najciemniejszy)
print("Najjaśniejszy pixel:",najjasniejszy)
