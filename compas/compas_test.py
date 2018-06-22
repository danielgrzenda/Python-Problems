import subprocess
import glob

class TestFailed(BaseException):
    def __init__(self, m):
        self.message = m
    def __str__(self):
        return self.message

def get_answer(file):
    f = open(file,'r')
    answ = f.read()
    f.close()
    return int(answ)

def test_input(input, answer):
    line = "python compas.py < %s" %input
    try:
        p = subprocess.Popen(line, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        out = p.stdout.read()
        ans = int(out) #if not int it breaks
    except Exception as e:
        raise TestFailed("FAILE: Execution error")
    print("[" + input + "]: " + ("PASS" if answer == ans else "FAIL"))

files = glob.glob("*.in")
files.sort()
for test in files:
    test_input(test, get_answer(test.split('.')[0]+'.ans'))
