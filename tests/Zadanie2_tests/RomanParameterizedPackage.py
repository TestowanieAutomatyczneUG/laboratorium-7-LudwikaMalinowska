import unittest
from parameterized import parameterized, parameterized_class

from Zadanie2.Roman import RomanNumerals

from nose.tools import assert_equal, assert_raises


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
        (141, "CXLI"),
        (575, "DLXXV"),
        (1024, "MXXIV"),
        (3000, "MMM")
    ])
    def test_one_parameterized(self,n, rom):
        self.assertEqual(self.tmp.roman(n), rom)

    def tearDown(self):
        self.temp = None


@parameterized([
        (1, "I"),
        (2, "II"),
        (3, "III"),
        (4, "IV"),
        (6, "VI"),
        (9, "IX"),
        (27, "XXVII"),
        (49, "XLIX"),
        (59, "LIX"),
        (141, "CXLI"),
        (575, "DLXXV"),
        (1024, "MXXIV"),
        (3000, "MMM"),
])
def test_roman_outside_class(n, rom):
    r = RomanNumerals()
    assert_equal(r.roman(n), rom)


@parameterized_class(('n', 'rom'), [
        (1, "I"),
        (2, "II"),
        (3, "III"),
        (4, "IV"),
        (6, "VI"),
        (9, "IX"),
        (27, "XXVII"),
        (49, "XLIX"),
        (59, "LIX"),
        (141, "CXLI"),
        (575, "DLXXV"),
        (1024, "MXXIV"),
        (3000, "MMM"),
])
class RomanParameterizedPackage2(unittest.TestCase):
    def setUp(self):
        self.tmp = RomanNumerals()

    def test_second_parameterized(self):
        self.assertEqual(self.tmp.roman(self.n), self.rom)



if __name__ == '__main__':
    unittest.main()