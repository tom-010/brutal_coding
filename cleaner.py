class Cleaner():
    
    def clean(self, lines, to_do):
        print(to_do)
        res = []
        line_no = 0
        for line in lines:
            if line_no not in to_do:
                res.append(line)
            line_no += 1
        return res
