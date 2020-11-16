import unittest

import sys
sys.path.insert(0, '../../src/Zadanie1')
from Hamming import Hamming

h = Hamming()
dist = h.distance("", "")
print(dist)

if __name__ == '__main__':
    unittest.main()
