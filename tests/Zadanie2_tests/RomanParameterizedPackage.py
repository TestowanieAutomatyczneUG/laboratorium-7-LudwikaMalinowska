import unittest
from parameterized import parameterized, parameterized_class

from Zadanie2.Roman import RomanNumerals

class RomanParameterizedPackage(unittest.TestCase):

    def setUp(self):
        self.tmp = RomanNumerals()

    @parameterized.expand([
        (1, "I"),
        (2, "II"),
        (3, "III"),
        (4, "IV"),
        (6, "VI"),
        (9, "IX"),
        (27, "XXVII"),
        (49, "XLIX"),
        (59, "LIX"),
    ])

    def test_one_parameterized(self,n, rom):
        self.assertEqual(self.tmp.roman(n), rom)

    def tearDown(self):
        self.temp = None


if __name__ == '__main__':
    unittest.main()