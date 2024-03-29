#Test helper functions

import unittest
import helpers

class TestSolverMethods(unittest.TestCase):
  def test_test(self):
    self.assertTrue(True)

  def test_isPrime(self):
    self.assertTrue(helpers.isPrime(13))
    self.assertFalse(helpers.isPrime(1))
    self.assertFalse(helpers.isPrime(4))

  def test_getNPrimes(self):
    self.assertEqual(helpers.getNPrimes(4), [2, 3, 5, 7])

  def test_generatePrimeTable(self):
    self.assertEqual(helpers.generatePrimeTable(2), "   2  3\n2  4  6\n3  6  9")

if __name__ == '__main__':
  unittest.main()