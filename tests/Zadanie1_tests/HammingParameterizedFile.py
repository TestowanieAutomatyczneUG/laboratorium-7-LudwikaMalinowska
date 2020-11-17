import unittest
from Zadanie1.Hamming import Hamming


class HammingParameterizedFile(unittest.TestCase):

    def test_from_file(self):
            fileTest = open("../../data/hamming_data_test")
            tmpHamming = Hamming()
            for line in fileTest:
                if line.startswith("#") or line.startswith(" ") or line.startswith("\n"):
                    continue
                else:
                    data = line.split(",")
                    a, b, result = str(data[0]), str(data[1]), int(data[2].strip("\n"))
                    # print(a,b,result)
                    self.assertEqual(tmpHamming.distance(a,b), result)
            fileTest.close()


if __name__ == '__main__':
    unittest.main()