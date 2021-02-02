inputFile = open('./pierwsze.txt')
outputFile = open('./wyniki4_2.txt', 'w')

def isPalindrom_i(string):
  if string == string[::-1]: return True
  else: return False

def isPalindrom_r(string):
  if len(string) < 2: return True
  if len(string) == 2: 
    if string[0] == string[-1]: return True
    else: return False

  if string[0] == string[-1]: return isPalindrom_r(string[2:-1])
  else: return False
  
def isPrime(arg):
  for i in range(2, arg):
    if arg % i == 0:
      return False
  return True

for line in inputFile.readlines():
  line = line.strip()
  # if isPalindrom_i(line):
  if isPrime(int(line[::-1])):
    outputFile.write(line + '\n')