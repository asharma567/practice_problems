'''
https://www.codeeval.com/open_challenges/87/submit/?lid=758502

I want to do redo this one using: 
    i)Numpy
    ii)OOP
'''
import sys
import numpy as np

#initialize matrix
Matrix = [[0 for x in xrange(256)] for x in xrange(256)] 

def set_row(row_index, value):
    Matrix[row_index] = map(lambda x: value, Matrix[row_index])
    pass

def set_col(col_index, value):
    for row in Matrix:
        row[col_index] = value
    pass

def print_query_row(row_index):
    print sum(Matrix[row_index])
    pass

def print_query_col(col_index):
    print sum([row[col_index] for row in Matrix])
    pass


def setting_command_to_matrix(set_command_input, index, value = None):
    
    # proper form is a dictionary instead of an elif structure, try this later
    if set_command_input == 'SetCol': set_col(index, value)
    elif set_command_input == 'SetRow': set_row(index, value)
    elif set_command_input == 'QueryRow': print_query_row(index)
    elif set_command_input == 'QueryCol': print_query_col(index)
    
    pass
    

def main(line):
    
    input_str = line.strip().split()
    
    if len(input_str) == 3:
        # for setting assignments to the Matrix
        set_command_input, index_str, value_str = input_str
        index = int(index_str)
        value = int(value_str)
        setting_command_to_matrix(set_command_input, index, value)

    elif len(input_str) == 2:
        # for querying the Matrix
        set_command_input, index_str = input_str
        index = int(index_str)
        setting_command_to_matrix(set_command_input, index)
    else:
        raise ValueError('User input is incorrect')

    
    

if __name__ == '__main__':
    with open(sys.argv[1], 'r') as f:
        for line in f:
            main(line)
