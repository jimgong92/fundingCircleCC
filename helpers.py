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

# Params: bound, Integer
# Return: result, List - returns list up to the Nth prime
def getNPrimes(bound):
  result = []
  n = 2
  while (len(result) < bound):
    if (isPrime(n)):
      result.append(n)
    n += 1
  return result