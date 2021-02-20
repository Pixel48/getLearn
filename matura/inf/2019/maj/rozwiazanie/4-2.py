def factor(num):
  if num < 2: return 1
  return factor(num - 1) * num

outputFile = open('wynik4-2.txt', 'w')

with open('liczby.txt') as inFile:
  numbers = [int(line) for line in inFile.readlines()]
  outputLines = []
  for num in numbers:
    sum = 0
    for char in str(num):
      sum += factor(int(char))
    if sum == num: outputLines.append(str(num) + '\n')
  outputFile.writelines(outputLines)

outputFile.close()
