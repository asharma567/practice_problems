import sys
from collections import Counter
import string


def func(s):
    '''
    INPUT: string
    OUTPUT: optimal sum of string
    '''
    #setting the max value per letter at 26 ie the length of a alphabet
    decr = len(string.ascii_lowercase)
    
    #creating a hash just to avoid characters that aren't in the alphabet eg '!'
    alphabet = set(string.ascii_lowercase)
    
    #should assign variables 1-26 value inclusive starting with 26 to the most frequently occuring
    #find frequency of the letters of the alphabet then put it into list 
    keyval_tups = [(key, val) for key, val in Counter(s.lower()).iteritems() if key in alphabet]
    
    #order it s.t. the most frequent letter is first
    keyval_tups_sorted = sorted(keyval_tups, key=lambda x: x[1], reverse=True)

    #key = letter: value = number * count of occurence
    optimal_value_letter_dict = {keyval[0]: keyval[1] * (decr - i) for i, keyval in enumerate(keyval_tups_sorted)}
    
    return sum(optimal_value_letter_dict.values())


if __name__ == '__main__':
	with open(sys.argv[1], 'r') as f:
		for line in f:
			print func(line.strip())