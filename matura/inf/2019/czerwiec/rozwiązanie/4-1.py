outputFile = open('./wyniki4_1.txt', 'w')
# otwórz plik wynikowy

def isPrime(arg):
  for i in range(2, arg):
    if arg % i == 0:
      return False
  return True

inputFile = open('./liczby.txt')
inputLines = inputFile.readlines()

start = 100
stop = 5000

import sys
if len(sys.argv[1:]) == 2:
  start = int(sys.argv[1])
  stop = int(sys.argv[2])

for line in inputLines:
  line = int(line.strip())
  if isPrime(line):
    if line in range(start, stop):
      outputFile.write(str(line) + '\n')

outputFile.close()
inputFile.close()
