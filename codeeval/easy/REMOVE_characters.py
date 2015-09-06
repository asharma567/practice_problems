'''
https://www.codeeval.com/open_challenges/13/submit/?lid=717936
'''

import sys

def delete_char(s):
    new_s = ''
    set_del_chars = set(del_chars)
    for sent_char in sentence:
        if sent_char not in set_del_chars: new_s += sent_char
    return new_s

if __name__ == '__main__':
	with open(sys.argv[1], 'r') as f:
	    for line in f:
	        print delete_char(line.split(', '))