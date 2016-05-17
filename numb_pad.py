'''
I would like to have a program that takes in a phone number, and returns the 'mnemonics' that might be associated with it. Mnemonics are letters that people can use to remember numbers, such as 555-4 PIZZA

The following numeric-to-character correspondances exist:

1 - '1'
2 - abc
3 - def
4 - ghi
5 - jkl
6 - mno
7 - pqrs
8 - tuv
9 - wxyz
0 - '0'

Numbers can also stand for themselves.  How would you build this?
'''
from itertools import product

mappings_dict = {
	'1' : ['1'],
	'2' : ['a','b','c','2'],
	'3' : ['d','e','f','3'],
	'4' : ['g','h','i','4'],
	'5' : ['j','k','l','5'],
	'6' : ['m','n','o','6'],
	'7' : ['p','q','r','s','7'],
	'8' : ['t','u','v','8'],
	'9' : ['w','x','y','z','9'],
	'0' : ['0'],
}

def fund(input_str):
    return list(product(*map(lambda x: mappings_dict[x], list(input_str))))
