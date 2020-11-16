import unittest

import sys
sys.path.insert(0, '../../src/Zadanie1')
from Hamming import Hamming

#h = Hamming()
#dist = h.distance("", "")
#print(dist)


class HammingTest(unittest.TestCase):

    # Utility functions
    def setUp(self):
        try:
            self.temp = Hamming()
            self.assertRaisesRegex

        except AttributeError:
            self.assertRaisesRegex = self.assertRaisesRegexp

    def test_empty_strands(self):
        self.assertEqual(self.temp.distance("", ""), 0)

    def test_single_letter_identical_strands(self):
        self.assertEqual(self.temp.distance("A", "A"), 0)

    def test_single_letter_different_strands(self):
        self.assertEqual(self.temp.distance("G", "T"), 1)

    def test_long_identical_strands(self):
        self.assertEqual(self.temp.distance("GGACTGAAATCTG", "GGACTGAAATCTG"), 0)

    def test_long_different_strands(self):
        self.assertEqual(self.temp.distance("GGACGGATTCTG", "AGGACGGATTCT"), 9)

    def test_disallow_first_strand_longer(self):
        with self.assertRaisesWithMessage(ValueError):
            self.temp.distance("AATG", "AAA")
        # self.assertRaises(ValueError, self.temp.distance, "AATG", "AAA")

    def test_disallow_second_strand_longer(self):
        with self.assertRaisesWithMessage(ValueError):
            self.temp.distance("ATA", "AGTG")
        # self.assertRaises(ValueError, self.temp.distance, "ATA", "AGTG")

    def test_disallow_left_empty_strand(self):
        with self.assertRaisesWithMessage(ValueError):
            self.temp.distance("", "G")
        # self.assertRaises(ValueError, self.temp.distance, "", "G")

    def test_disallow_right_empty_strand(self):
        with self.assertRaisesWithMessage(ValueError):
            self.temp.distance("G", "")
        # self.assertRaises(ValueError, self.temp.distance, "G", "")

    def assertRaisesWithMessage(self, exception):
        return self.assertRaisesRegex(exception, r".+")

    def tearDown(self):
        self.temp = None

if __name__ == '__main__':
    unittest.main()
