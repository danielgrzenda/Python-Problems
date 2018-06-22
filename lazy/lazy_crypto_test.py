import subprocess
import glob
class TestFailed(BaseException):
    def __new__(self, m):
        self.message = m
    def __str__(self):
        return self.message

def get_answer(file):
    f = open(file,'r')
    answ = f.read()
    f.close()
    return int(answ)

def test_input(input, answer):
    line = "python lazy_cryto.py < %s" %input
    try:
        p = subprocess.Popen(line, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        ans = int(p.stdout.read()) #if not int it breaks
    except Exception as e:
        raise TestFailed("Fail: Execution error")
    print("[" + input + "]: " + ("PASS" if answer == ans else "FAIL"))
#get all inoput files
for test in glob.glob("*.in"):
    test_input(test, get_answer(test.split('.')[0]+'.ans'))
