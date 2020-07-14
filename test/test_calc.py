import unittest

from footest.calc import Calc

class TestCalc(unittest.TestCase):

    def setUp(self):
        self.calc = Calc()

    def test_add_one(self):
        self.assertEqual(self.calc.add_one(1), 2)

if __name__ == '__main__':
    unittest.main()
