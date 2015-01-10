'''
https://www.codeeval.com/open_challenges/32/
'''
import sys

def check_this_line(line_str):
    subj_line, end = line_str.strip().split(',')
    return int(subj_line[-len(end):] == end)


if __name__ == '__main__':
    with open(sys.argv[1], 'r') as f:
        for line in f:
            print check_this_line(line), line