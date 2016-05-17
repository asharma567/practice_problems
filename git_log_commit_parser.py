import sys
import subprocess
import re

'''
how would you grab all the commit hashes

git log | grep 'commit' | cut -d' ' -f > commits.txt
ps axu | grep python | sed 's/\s\+/ /g' | cut -d' ' -f2,11-
'''

def stream_method():
    '''
    '''
    for line in sys.stdin:
        if 'commit' in line and len(line.split()) == 2 and 'initial' not in line:
            out = line.split('commit')[1].strip()
            if out:
                print out 


def full_call_method():
    hashes = subprocess.Popen(['git', 'log'], stdout=subprocess.PIPE)
    
    stdout_value = hashes.communicate()[0]
    for line in stdout_value.split('\n'):

        if 'commit' in line and len(line.split()) == 2 and 'initial' not in line:
            out = line.split('commit')[1].strip()
            if out:
                
                with open('commits_python.txt','ab') as f:
                    f.write(out + '\n')


def full_call_method_regex():
    hashes = subprocess.Popen(['git', 'log'], stdout=subprocess.PIPE)
    
    stdout_value = hashes.communicate()[0]
    for line in stdout_value.split('\n'):
        outcome = re.findall(r'^commit [a-z\d]+', line)
        if outcome: 
            with open('commits_python.txt','ab') as f:
                f.write(outcome[0].split()[1])

    


if __name__ == '__main__':
    # input comes from STDIN (standard input)
    # stream_method()   
    full_call_method_regex()

