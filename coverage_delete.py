from cleaner import Cleaner
from parser import Parser
import subprocess
import sys

class Cmd():

    def __init__(self):
        self.cwd = '.'

    def cd(self, to):
        self.cwd = to

    def run(self, command):  
        cammand_splitted = [x for x in command.split(' ') if x]
        result = subprocess.run(cammand_splitted, stdout=subprocess.PIPE, cwd=self.cwd)
        return  result.stdout.decode('utf-8')

class CoverageDelete():

    def run(self, project):
        report_str = self.run_coverage(project)
        report = self.create_report(report_str)
        files = self.collect_files_to_manipulate(project, report)
        self.perform_coverage_delete(files)

    def run_coverage(self, path):
        cmd = Cmd()
        cmd.cd(path)
        cmd.run('coverage run -m unittest discover')
        return cmd.run('coverage report --show-missing --omit=test_*,*site-packages*')

    def create_report(self, report_str):
        parser = Parser()
        report = parser.parse(report_str)
        return report

    def collect_files_to_manipulate(self, project, report):
        files = {}
        for line in report:
            path = project+'/'+line.file

            if path not in files:
                files[path] = []
            
            files[path].append(line.line-1)
        return files

    def perform_coverage_delete(self, files):
        # perform coverage delete
        cleaner = Cleaner('pass # pragma: no cover\n')
        for filename in files.keys():
            content = self.read(filename)
            content = cleaner.clean(content, files[filename])
            self.write(filename, content)

    def read(self, filename):
        with open(filename) as f:
            return f.readlines()

    def write(self, filename, content):
        with open(filename, 'w') as f:
            for item in content:
                f.write("%s" % item)

if __name__ == "__main__":
    CoverageDelete().run(sys.argv[1])
