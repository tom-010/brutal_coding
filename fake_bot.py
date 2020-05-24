from cleaner import Cleaner
from parser import Parser
import subprocess

project = 'pet-project'

class Cmd():

    def __init__(self):
        self.cwd = '.'

    def cd(self, to):
        self.cwd = to

    def run(self, command):  
        cammand_splitted = [x for x in command.split(' ') if x]
        result = subprocess.run(cammand_splitted, stdout=subprocess.PIPE, cwd=self.cwd)
        return  result.stdout.decode('utf-8')

# run coverage
cmd = Cmd()
cmd.cd(project)
cmd.run('coverage run -m unittest discover')
report_str = cmd.run('coverage report --show-missing --omit=test_*,*site-packages*')

# create report
parser = Parser()
report = parser.parse(report_str)

# collect files to manipulate
files = {}
for line in report:
    path = project+'/'+line.file

    if path not in files:
        files[path] = []
    
    files[path].append(line.line-1)

def read(filename):
    with open(filename) as f:
        return f.readlines()

def write(filename, content):
    with open(filename, 'w') as f:
        for item in content:
            f.write("%s" % item)

# perform coverage delete
cleaner = Cleaner('pass # pragma: no cover\n')
for filename in files.keys():
    content = read(filename)
    content = cleaner.clean(content, files[filename])
    write(filename, content)


