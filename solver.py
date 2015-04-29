import math
import sys

from helpers import generatePrimeTable

def run(n):
  table = generatePrimeTable(n)
  print(table)

if (__name__ == '__main__'):
  bound = int(sys.argv[1])
  run(bound)