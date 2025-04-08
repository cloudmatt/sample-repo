import unittest
from src.cool_func import cool_func

# FILE: src/test_cool_func.py


class TestCoolFunc(unittest.TestCase):
    def test_cool_func(self):
        message = "This is a test"
        expected_output = "Cool: This is a test"
        self.assertEqual(cool_func(message), expected_output)


if __name__ == "__main__":
    unittest.main()
