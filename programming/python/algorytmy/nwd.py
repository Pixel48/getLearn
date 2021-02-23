def nwd(a, b):
  if b > 0:
    print(a, '%',  b)
    return nwd(b, a%b)
  print(a)
  return a
