def fib_i(n):
  a = 1
  b = 1
  i = 1
  while i < n:
    a, b = b, a+b
    i += 1
  return a

def fib_r(n):
  if n < 2: return 1
  return fib_r(n-1) + fib_r(n-2)
