import math
from unittest import result

def add_frac(frac1, frac2):        # frac1 + frac2
    if (frac1[1] == 0 and frac2[1] == 0):
        raise ZeroDivisionError()
    
    out = [0, 0]
    out[0] = frac1[0] * frac2[1] + frac2[0] * frac1[1]
    out[1] = frac1[1] * frac2[1]

    nww = math.gcd(out[0], out[1])
    return[x//nww for x in out]

def sub_frac(frac1, frac2):        # frac1 - frac2
    if (frac1[1] == 0 and frac2[1] == 0):
        raise ZeroDivisionError()
    
    out = [0, 0]
    out[0] = frac1[0] * frac2[1] - frac2[0] * frac1[1]
    out[1] = frac1[1] * frac2[1]

    nww = math.gcd(out[0], out[1])
    return[x//nww for x in out]

def mul_frac(frac1, frac2):        # frac1 * frac2
    if (frac1[1] == 0 and frac2[1] == 0):
        raise ZeroDivisionError()
    
    out = [0, 0]
    out[0] = frac1[0] * frac2[0]
    out[1] = frac1[1] * frac2[1]

    nww = math.gcd(out[0], out[1])
    return[x//nww for x in out]

def div_frac(frac1, frac2):        # frac1 / frac2
    if (frac1[1] == 0 and frac2[1] == 0):
        raise ZeroDivisionError()
    
    out = [0, 0]
    out[0] = frac1[0] * frac2[1]
    out[1] = frac1[1] * frac2[0]

    nww = math.gcd(out[0], out[1])
    return[x//nww for x in out]

def is_positive(frac):             # bool, czy dodatni
    if frac[1] == 0:
        raise ZeroDivisionError()
    return True if frac[0] * frac[1] > 0 else False

def is_zero(frac):                 # bool, typu [0, x]
    if frac[1] == 0:
        raise ZeroDivisionError()
    return True if frac[0] == 0 else False

def cmp_frac(frac1, frac2):        # -1 | 0 | +1
    if (frac1[1] == 0 and frac2[1] == 0):
        raise ZeroDivisionError()
    cmp1 = frac1[0] * frac2[1]
    cmp2 = frac2[0] * frac1[1]
    if cmp1 == cmp2:
        return 0
    else:
        return 1 if cmp1 > cmp2 else -1

def frac2float(frac):              # konwersja do float
    return float(frac[0] / frac[1])

import unittest

class TestFractions(unittest.TestCase):

    def setUp(self):
        self.zero = [0, 1]

    def test_add_frac(self):
        self.assertEqual(add_frac([1, 2], [1, 3]), [5, 6])

    def test_sub_frac(self):
        self.assertEqual(sub_frac([1, 2], [1, 3]), [1, 6])

    def test_mul_frac(self):
        self.assertEqual(mul_frac([3, 4], [5, 7]), [15, 28])

    def test_div_frac(self):
        self.assertEqual(div_frac([5, 6], [3, 2]), [5, 9])

    def test_is_positive(self):
        self.assertEqual(is_positive([3, -4]), False)
        self.assertEqual(is_positive([-3, -4]), True)
        self.assertEqual(is_positive([3, 4]), True)

    def test_is_zero(self):
        self.assertEqual(is_zero([0, 2]), True)
        self.assertEqual(is_zero([2, 3]), False)

    def test_cmp_frac(self):
        self.assertEqual(cmp_frac([1, 2], [1, 3]), 1)
        self.assertEqual(cmp_frac([1, 2], [2, 4]), 0)
        self.assertEqual(cmp_frac([-1, 2], [1, 3]), -1)

    def test_frac2float(self):
        self.assertEqual(frac2float([1, 2]), 0.5)
        self.assertEqual(frac2float([0, 1]), 0.0)

    def tearDown(self): pass

if __name__ == '__main__':
    unittest.main()     # uruchamia wszystkie testy