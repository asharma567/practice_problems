'''
DELTA TIME

https://www.codeeval.com/open_challenges/166/
'''
import sys
import datetime as dt

def take_delta(tstring):
    t1_str, t2_str = tstring.split()
    t2 = dt.datetime.strptime(t1_str, '%H:%M:%S')
    t1 = dt.datetime.strptime(t2_str, '%H:%M:%S')
    t_delta = t1 - t2
    s = t_delta.seconds

    return '{:02}:{:02}:{:02}'.format(s // 3600, s % 3600 // 60, s % 60)

if __name__ == '__main__':
    with open(sys.argv[1], 'r') as f:
        for line in f:
            print take_delta(line.strip())