from math import log

outputFile = open('wynik4-1.txt', 'w')

def isPow(what, ofWhat):
  if log(what, ofWhat) % 1 == 0: return True
  return False

with open(r'liczby.txt') as inFile:
  lines = [int(line.strip()) for line in inFile.readlines()]
  count = 0
  for num in lines:
    if isPow(num, 3):
      count += 1
      # print(num)
  outputFile.write(str(count))

outputFile.close()
