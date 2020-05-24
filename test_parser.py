import unittest
from collections import namedtuple


Line = namedtuple('Line', ['file', 'line'])

class Parser():
    
    def parse(self, s):
        if not s:
            return []
        
        lines = []
        for line in s.split('\n'):
            parts = [x for x in line.split(' ') if x]
            if len(parts) == 5 and parts[4] != 'Missing':
                lines.append(Line(parts[0], int(parts[4])))


        return lines



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
    
  

        