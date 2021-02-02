def w(n):
  out = 0
  n = str(n)
  for char in n:
    out += int(char)

  if len(str(out)) != 1: return w(out)
  return out

inputFile = open('./pierwsze.txt')
outputFile = open('./wyniki4_3.txt', 'w')

count = 0
for line in inputFile.readlines():
  line = int(line.strip())
  if w(line) == 1: count += 1
  
outputFile.write(str(count))

inputFile.close()
outputFile.close()