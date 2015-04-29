import math
# Params: n, Integer
# Return: Boolean - whether true
def isPrime(n):
  if (n < 2):
    return False
  root = math.sqrt(n)
  bound = math.trunc(root) + 1
  for i in range(2, bound):
    if (n % i == 0):
      return False
  return True