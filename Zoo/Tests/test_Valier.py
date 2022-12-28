from Valier import *
from AnimalsImport import *
import unittest
class valier_tests(unittest.TestCase):
    def test_add(self):
        boris = wolf('Boris', 5, 5)
        kira = llama('Kira Yoshikage', 10, 96)
        t = valier('Test', 100, 'desert')
        t.add(kira)
        t.add(boris)
        expected = [kira]
        actual = t.animals
        self.assertEqual(expected, actual)

    def test_delete(self):
        boris = wolf('Boris', 5, 5)
        t = valier('Test', 100, 'forest')
        t.add(boris)
        t.delete(boris)
        expected = []
        actual = t.animals
        self.assertEqual(expected, actual)

    def test_deleteAll(self):
        boris = wolf('Boris', 5, 5)
        t = valier('Test', 100, 'forest')
        t.add(boris)
        t.deleteAll()
        expected = []
        actual = t.animals
        self.assertEqual(expected, actual)

    def test_feed(self):
        boris = wolf('Boris', 5, 5)
        moris = wolf('Moris', 5, 5)
        t = valier('Test', 100, 'forest')
        t.add(boris)
        t.add(moris)
        t.feed(10, "meat")
        expected = True
        actual = t.feeded
        self.assertEqual(expected, actual)

    def test_notFeed(self):
        boris = wolf('Boris', 5, 5)
        moris = wolf('Moris', 5, 5)
        t = valier('Test', 100, 'forest')
        t.add(boris)
        t.add(moris)
        t.feed(9, "meat")
        t.feed(1, "grass")
        expected = False
        actual = t.feeded
        self.assertEqual(expected, actual)

if __name__ == '__main__':
    unittest.main()