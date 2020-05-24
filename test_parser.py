import unittest
from collections import namedtuple


Line = namedtuple('Line', ['file', 'line'])

class Parser():
    
    def parse(self, s):
        if not s:
            return []
        
        lines = []
        for line in s.split('\n'):
            parts = [x for x in line.split('  ') if x]
            if len(parts) == 5 and parts[4] != ' Missing':
                for line_no in self.parse_lines_part(parts[4]):
                    lines.append(Line(parts[0], line_no))


        return lines

    def parse_lines_part(self, s):
        res = []
        for p in s.split(', '):
            if '-' in p:
                [fromRange, toRange] = p.split('-')
                for i in range(int(fromRange), int(toRange)+1):
                    res.append(i)
            else: 
                res.append(int(p))
        return res



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

        