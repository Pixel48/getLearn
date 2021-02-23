def nww(a, b):
  if a < b:
    return nww(b, a)
  k = a
  while k % b > 0:
    k += a
  return k
