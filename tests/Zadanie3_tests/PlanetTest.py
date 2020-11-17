import unittest
# from Zadanie3.Planet import Planet
import sys
sys.path.insert(0, '../../src/Zadanie3')
from Planet import Planet

class PlanetTests(unittest.TestCase):

    def setUp(self):
        self.temp = Planet()

    def test_mercury_age_correctly_counted(self):
        self.assertEqual(self.temp.count_age_on_planet(2134835688, "Merkury"), 280.88)

    def test_venus_age_correctly_counted(self):
        self.assertEqual(self.temp.count_age_on_planet(1000000000, "Wenus"), 51.51)

    def test_earth_age_correctly_counted(self):
        self.assertEqual(self.temp.count_age_on_planet(1000000000.0, "Ziemia"), 31.69)

    def test_mars_age_correctly_counted(self):
        self.assertEqual(self.temp.count_age_on_planet(1000000000, "Mars"), 16.85)

    def test_jupiter_age_correctly_counted(self):
        self.assertEqual(self.temp.count_age_on_planet(1000000000, "Jowisz"), 2.67)

    def test_saturn_age_correctly_counted(self):
        self.assertEqual(self.temp.count_age_on_planet(1000000000, "Saturn"), 1.08)

    def test_uranus_age_correctly_counted(self):
        self.assertEqual(self.temp.count_age_on_planet(1000000000, "Uran"), 0.38)

    def test_neptune_age_correctly_counted(self):
        self.assertEqual(self.temp.count_age_on_planet(1000000000, "Neptun"), 0.19)


    def test_mercury_exception1(self):
        self.assertRaises(ValueError, self.temp.count_age_on_planet, 2134835688, "Merkur")

    def test_mercury_exception2(self):
        self.assertRaises(ValueError, self.temp.count_age_on_planet, "", "Merkury")

    def test_mercury_exception3(self):
        self.assertRaises(ValueError, self.temp.count_age_on_planet, "2134835688", "Merkury")


if __name__ == '__main__':
    unittest.main()

