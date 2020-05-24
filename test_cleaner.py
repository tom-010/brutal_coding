import unittest
from cleaner import Cleaner



class CleanerTest(unittest.TestCase):

    def setUp(self):
        self.uut = Cleaner()

    def test_delte_nothing(self):
        lines = ['a','b','c','d','e']
        self.assertEqual(self.uut.clean(lines, []), lines)

    def test_delete_one_line(self):
        lines = ['a','b','c','d','e']
        self.assertEqual(self.uut.clean(lines, [0]), ['b','c','d','e'])

    def test_delete_multiple_line(self):
        lines = ['a','b','c','d','e']
        self.assertEqual(self.uut.clean(lines, [0, 2, 3]), ['b','e'])

    def test_delete_line_that_does_not_exist(self):
        lines = ['a','b','c','d','e']
        self.assertEqual(self.uut.clean(lines, [10,20,30]), lines)
