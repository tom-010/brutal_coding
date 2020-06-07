import unittest
from parser import Parser, Line


class TestParser(unittest.TestCase):

    def setUp(self):
        self.uut = Parser()

    def test_empty_string_no_lines(self):
        self.assertEqual(self.uut.parse(''), [])

    def report(self, lines):
        res = ''
        for line in lines:
            res += line + '\n'
        return res

    def test_no_line(self):
        report = self.report([
        'Name     Stmts   Miss  Cover   Missing',
        '--------------------------------------'])
        self.assertEqual(self.uut.parse(report), [])

    def test_one_line(self):
        report = self.report([
        'Name     Stmts   Miss  Cover   Missing',
        '--------------------------------------',
        'fib.py       4      1    75%   5      '])
        self.assertEqual(self.uut.parse(report), [Line('fib.py', 5)])

    def test_two_lines(self):
        report = self.report([
        'Name     Stmts   Miss  Cover   Missing',
        '--------------------------------------',
        'fib.py       4      1    75%   5      ',
        'sum.py       4      1    75%   7      '])
        self.assertEqual(self.uut.parse(report), [Line('fib.py', 5), Line('sum.py', 7)])
    
    def test_line_range(self):
        report = self.report([
        'Name     Stmts   Miss  Cover   Missing',
        '--------------------------------------',
        'fib.py       4      1    75%   5-8    '])
        self.assertEqual(self.uut.parse(report), [
            Line('fib.py', 5), 
            Line('fib.py', 6), 
            Line('fib.py', 7), 
            Line('fib.py', 8)])

    def test_range_and_line(self):
        report = self.report([
        'Name     Stmts   Miss  Cover   Missing',
        '--------------------------------------',
        'fib.py       4      1    75%   4, 8-11, 14-16, 19'])
        self.assertEqual(self.uut.parse(report), [
            Line('fib.py', 4),
            Line('fib.py', 8), 
            Line('fib.py', 9), 
            Line('fib.py', 10), 
            Line('fib.py', 11),
            Line('fib.py', 14),
            Line('fib.py', 15), 
            Line('fib.py', 16), 
            Line('fib.py', 19)])

        