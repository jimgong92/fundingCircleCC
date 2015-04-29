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

def generatePrimeTable(bound):
  table = 'TEST'
  # Get primes within bound
  primes = getNPrimes(bound)
  # Get width of columns (length of biggest number)
  columnWidth =  len(str(math.pow(primes[-1], 2)))
  # Get width of row labels (length of biggest prime)
  rowLabelOffset = len(str(primes[-1]))
  # Generate initial row of column labels - offset by row labels
  #   Offset initial row by width of the row labels
  columnLabels = rowLabelOffset * ' '
  for i in range(bound):
    columnLabels += 'TEST'
  # Generate table rows (row label | product of row * column labels)
  for i in range(bound):
    row = '\nTEST'
    for j in range(bound):
      row += 'TEST'
    table += row
  return table