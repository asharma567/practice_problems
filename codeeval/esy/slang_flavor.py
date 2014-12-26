'''
https://www.codeeval.com/open_challenges/174/submit/?lid=731009
'''



"""Sample code to read in test cases:

import sys
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    # ignore test if it is an empty line
    # 'test' represents the test case, do something with it
    # ...
    # ...

test_cases.close()
"""
import sys

ending_punc = {'.', '!', '?'}
ending_punc_ctr = 0
position_ctr = 0

lis = [
', yeah!', 
', this is crazy, I tell ya.',
', can U believe this?',
', eh?',
', aw yea.',
', yo.',
'? No way!',
'. Awesome!'
]
output = []


def print_outcome(s):
    '''
    INPUT
    OUTPUT
    
    '''
    
    output = []
    for char in s:
        if char in ending_punc: 
            ending_punc_ctr += 1
            #check if it's even i.e. every other
            if ending_punc_ctr % 2 == 0:
                output.append(lis [position_ctr % len(lis)])
                position_ctr += 1
            else:
                output.append(char)
        else:
            output.append(char)
    return ''.join(output)


if __name__ == '__main__':
	with open(sys.argv[1], 'r') as f:
	    print print_outcome(f.read())
