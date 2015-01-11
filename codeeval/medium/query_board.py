'''
https://www.codeeval.com/open_challenges/87/submit/?lid=758502

I want to do redo this one using: 
	i)Numpy
	ii)OOP
'''
import sys

def set_row(row_index, value):
    Matrix[row_index] = map(lambda x: value, Matrix[row_index])
    return None

def set_col(col_index, value):
    for row in Matrix:
        row[col_index] = value
    return None

def query_row(row_index):
    return sum(Matrix[row_index])

def query_col(col_index):
    return sum([row[col_index] for row in Matrix])

#initialize matrix
Matrix = [[0 for x in xrange(256)] for x in xrange(256)] 


def main(line):
	
	input_str = line.strip().split()
	
	if len(input_str) == 3:
	    set_command, index_str, value_str = input_str
	    index = int(index_str)
	    value = int(value_str)
	
	elif len(input_str) == 2:
	    set_command, index_str = input_str
	    index = int(index_str)
	else:
	    raise ValueError('User input is incorrect')

	if set_command == 'SetCol': set_col(index, value)
	if set_command == 'SetRow': set_row(index, value)
	if set_command == 'QueryRow': print query_row(index)
	if set_command == 'QueryCol': print query_col(index)


if __name__ == '__main__':
	with open(sys.argv[1], 'r') as f:
		for line in f:
			main(line)
			