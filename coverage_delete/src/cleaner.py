class Cleaner():
    
    def __init__(self, replace=None):
        self.replace = replace

    def leading_whitespaces(self, s):
        res = ''
        for c in s:
            if c == ' ':
                res += ' '
            else:
                return res
        return res

    def _clean_it(self, lines, to_do, replacement):
        res = []
        line_no = 0
        last_deleted = False
        for line in lines:
            should_delete = line_no in to_do

            if should_delete:
                if replacement and not last_deleted:
                    res.append(self.leading_whitespaces(line) + replacement)
                last_deleted = True
            else:
                res.append(line)
                last_deleted = False

            line_no += 1
        return res

    def clean(self, lines, to_do):
        return self._clean_it(lines, to_do, self.replace)
