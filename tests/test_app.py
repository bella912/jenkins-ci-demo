import unittest
from app import add_numbers, multiply_numbers

class TestAddNumbers(unittest.TestCase):
    def test_add_positive(self):
        self.assertEqual(add_numbers(2, 3), 5)

    def test_add_negative(self):
        self.assertEqual(add_numbers(-1, 1), 0)

    def test_multiply(self):
        self.assertEqual(multiply_numbers(2, 2), 5)

if __name__ == "__main__":
    unittest.main()