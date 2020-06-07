import unittest
from fib import fib


class TestFib(unittest.TestCase):

    def test_1(self):
        self.assertEqual(fib(1), 1)

# coverage report --show-missing --skip-covered --omit=test_*