import unittest
from calc import Calc

class TestCalc(unittest.TestCase):

    def setUp(self):
        self.calc = Calc()

    def test_add(self):
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(0,0), 0)
        self.assertEqual(self.calc.add(-1,-2), -3)

    def test_sub(self):
        self.assertEqual(self.calc.sub(2, 3), -1)
        self.assertEqual(self.calc.sub(0, 0), 0)
        self.assertEqual(self.calc.sub(-1, -1), 0)

    def test_mul(self):
        self.assertEqual(self.calc.mul(2, 3), 6)
        self.assertEqual(self.calc.mul(0, 3), 0)
        self.assertEqual(self.calc.mul(-1, 3), -3)
