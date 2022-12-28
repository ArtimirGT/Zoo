import unittest

from AnimalsImport import *


l = llama("L", 10, 5)
w = wolf("W", 10, 5)
e = elephant("E", 10, 5)
d = dog("D", 10, 5)

class baseAnimals_Tests(unittest.TestCase):

    def test_LEat(self):
        l.eat(1, "grass")
        l.eat(10, "meat")
        expected = False
        actual = l.IsFeeded
        self.assertEqual(expected, actual)

    def test_LEatFull(self):
        l.sum = 0
        l.eat(1, "grass")
        l.eat(9, "grass")
        expected = True
        actual = l.IsFeeded
        self.assertEqual(expected, actual)

    def test_LArea(self):
        l.area = 10
        expected = 10
        actual = l.area
        self.assertEqual(expected, actual)

    def test_WEat(self):
        w.eat(1, "meat")
        w.eat(10, "grass")
        expected = False
        actual = w.IsFeeded
        self.assertEqual(expected, actual)

    def test_WEatFull(self):
        w.sum = 0
        w.eat(1, "meat")
        w.eat(9, "meat")
        expected = True
        actual = w.IsFeeded
        self.assertEqual(expected, actual)

    def test_WArea(self):
        w.area = 10
        expected = 10
        actual = w.area
        self.assertEqual(expected, actual)

    def test_EEat(self):
        e.eat(1, "grass")
        e.eat(10, "meat")
        expected = False
        actual = e.IsFeeded
        self.assertEqual(expected, actual)

    def test_EEatFull(self):
        e.sum = 0
        e.eat(1, "grass")
        e.eat(9, "grass")
        expected = True
        actual = e.IsFeeded
        self.assertEqual(expected, actual)

    def test_EArea(self):
        e.area = 10
        expected = 10
        actual = e.area
        self.assertEqual(expected, actual)

    def test_DEat(self):
        d.eat(1, "meat")
        d.eat(10, "grass")
        expected = False
        actual = d.IsFeeded
        self.assertEqual(expected, actual)

    def test_DEatFull(self):
        d.sum = 0
        d.eat(1, "meat")
        d.eat(9, "meat")
        expected = True
        actual = d.IsFeeded
        self.assertEqual(expected, actual)

    def test_DArea(self):
        d.area = 10
        expected = 10
        actual = d.area
        self.assertEqual(expected, actual)

if __name__ == '__main__':
    unittest.main()