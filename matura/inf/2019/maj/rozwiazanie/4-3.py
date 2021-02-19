from math import gcd

outputFile = open('wynik.txt', 'w')

def agcd(arr):
  if len(arr) < 2: return arr[0]
  if len(arr) == 2: return gcd(arr[0], arr[1])
  return gcd(agcd(arr[:-1]), arr[-1])
  
# with open("przyklad.txt") as liczby:
with open("liczby.txt") as liczby:
  arr = [int(i) for i in liczby.readlines()]

i = 0; j = 1
currStart = i
currGCD = 1
currLen = 1
maxStart = i
maxLen = 1
maxGCD = 0

while j < len(arr):
  while not agcd(arr[i:j+1]) > 1:
    i += 1
    j += 1
  currStart = i
  currGCD = agcd(arr[i:j+1])
  currLen += 1
  j += 1
  while agcd(arr[i:j+1]) == currGCD:
    j += 1
    currLen += 1
  if currLen > maxLen:
    maxLen = currLen
    currLen = 1
    i = maxStart + 1
    maxStart = currStart
    currStart = i
    maxGCD = currGCD
    j = i + 1
  print(arr[maxStart], maxLen, maxGCD)



# with open('przyklad.txt') as inputFile:
# # with open('liczby.txt') as inputFile:
#   arr = [int(line) for line in inputFile.readlines()]
#   i = 0; j = 1
#   currGCD = 1
#   currStart = 0
#   gcdArrLen = 1
#   maxGcdArr = 1
#   maxGcdArrGcd = 1
#   maxGcdArrStart = 1
#   myGCD = 1
#   # until there's file
#   while j <= len(arr):
#     # find first arr part
#     while gcdArrLen == 1:
#       # print(agcd(arr[i:j]))
#       # myGCD = agcd(arr[i:j])
#       myGCD = gcd(arr[i], arr[j])
#       if myGCD > 1:
#         print('OK!')
#         j += 1
#         gcdArrLen = j-i+1
#         currStart = i
#         currGCD = myGCD
#       else:
#         i += 1
#         j += 1
#     # how long is arr
#     while currGCD == myGCD:
#       print("first: {} len: {}, NWD: {} ".format(arr[maxGcdArrStart], maxGcdArr, maxGcdArrGcd), flush=True, end='')
#       # myGCD = agcd(arr[i:j])
#       j += 1
#       myGCD = gcd(myGCD, arr[j])
#       if myGCD != currGCD:
#         j -= 1
#         if j-i+1 > maxGcdArr:
#           maxGcdArr = j-i+1
#           maxGcdArrStart = i
#           maxGcdArrGcd = currGCD
#         i = currGCD+1
#         j = i+1
#   print("\n\nPierwsza liczba:", arr[maxGcdArrStart], "\n", 
#         "Długość:", maxGcdArr, "\n",
#         "NWD:", maxGcdArrGcd)
