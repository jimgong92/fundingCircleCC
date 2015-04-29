import math
from helpers import isPrime, getNPrimes

def run():
  table = generatePrimeTable(10)
  print(table)

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

if (__name__ == '__main__'):
  run()