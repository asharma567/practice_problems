'''
https://www.codeeval.com/open_challenges/96/

Write a program which swaps letters' case in a sentence. 
All non-letter characters should remain the same.
'''
import sys

def func(s):
    array = len(s) * [None]
    for index, char in enumerate(s):
        if char.isupper(): 
            array[index] = char.lower()
        else:
            array[index] = char.upper()

    return ''.join(array)

if __name__ == '__main__':
    with open(sys.argv[1], 'r') as f:
        for line in f:
            print func(line.strip())