'''
https://www.codeeval.com/open_challenges/93/

Write a program which capitalizes the first letter of each word in a sentence.
'''
import sys 

def func(line):
    return ' '.join([word[0].upper() + word[1:] for word in line.split()])

if __name__ == '__main__':
    with open(sys.argv[1], 'r') as f:
        for line in f:
            print func(line.strip())