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
