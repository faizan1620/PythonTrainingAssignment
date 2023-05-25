import unittest
import sys
from main import Calci

# Test cases for testing main.py functions
# To run te unittest , go to the tests folder and run the command python -m unittest

sys.path.insert(0, "../")


class TestCalculations(unittest.TestCase):
    def setUp(self):
        self.calculation = Calci(8, 2)

    def test_sum(self):
        self.assertEqual(self.calculation.sum(), 10, "The sum is wrong.")
        self.assertNotEqual(self.calculation.sum(), 5, "The sum is wrong.")

    def test_diff(self):
        self.assertEqual(self.calculation.difference(), 6, "The difference is wrong.")
        self.assertNotEqual(
            self.calculation.difference(), 2, "The difference is wrong."
        )

    def test_product(self):
        self.assertEqual(self.calculation.product(), 16, "The product is wrong.")
        self.assertNotEqual(self.calculation.product(), 10, "The product is wrong.")

    def test_quotient(self):
        self.assertEqual(self.calculation.division(), 4, "The division is wrong.")
        self.assertNotEqual(self.calculation.division(), 3, "The division is wrong.")
        self.calculation = Calci(7, 0)
        self.assertEqual(
            self.calculation.division(),
            "Can't divide with zero",
            "The division is wrong.",
        )


if __name__ == "__main__":
    unittest.main()
