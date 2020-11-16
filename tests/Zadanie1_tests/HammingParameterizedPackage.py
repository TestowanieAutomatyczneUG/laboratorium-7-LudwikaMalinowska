import unittest
import sys
from parameterized import parameterized, parameterized_class
sys.path.insert(0, '../../src/Zadanie1')
from Hamming import Hamming
import math


class HammingParameterizedPackage(unittest.TestCase):

    def setUp(self):
        self.tmp = Hamming()

    @parameterized.expand([
        ("", "", 0),
        ("A", "A", 0),
    ])

    def test_one_parameterized(self,a,b, dist):
        self.assertEqual(self.tmp.distance(a,b), dist)



    def tearDown(self):
        self.temp = None




if __name__ == '__main__':
    unittest.main()

