'''
https://www.codeeval.com/open_challenges/87/submit/?lid=758502

I want to do redo this one using: 
    i)Numpy
    ii)OOP
'''
import sys
import numpy as np



class Query_board(object):

    def __init__(self, rows = 256, columns = 256):
        self.Matrix = np.zeros((rows, columns))

    def set_row(self, row_index, value):
        self.Matrix[row_index] = value
        pass

    def set_col(self, col_index, value):
        self.Matrix[:, col_index] = value
        pass

    def print_query_row(self, row_index):
        print self.Matrix[row_index].sum()
        pass

    def print_query_col(self, col_index):
        print self.Matrix[:, col_index].sum()
        pass

    # working on this 
    # commands_dict = {
    # 'SetCol': self.set_col(index, value),
    # 'SetRow': self.set_row(index, value),
    # 'QueryRow': self.print_query_row(index),
    # 'QueryCol': self.print_query_col(index)
    # }

    def executing_user_command(self, set_command_input, index, value = None):
        # Query_board.commands_dict[set_command_input]

        if set_command_input == 'SetCol': self.set_col(index, value)
        elif set_command_input == 'SetRow': self.set_row(index, value)
        elif set_command_input == 'QueryRow': self.print_query_row(index)
        elif set_command_input == 'QueryCol': self.print_query_col(index)
        
        pass
        

def main(board, line):
    
    input_str = line.strip().split()
    
    if len(input_str) == 3:
        # for setting assignments to the Matrix
        set_command_input, index_str, value_str = input_str
        index = int(index_str)
        value = int(value_str)
        board.executing_user_command(set_command_input, index, value)

    elif len(input_str) == 2:
        # for querying the Matrix
        set_command_input, index_str = input_str
        index = int(index_str)
        board.executing_user_command(set_command_input, index)
    else:
        raise ValueError('User input is incorrect')


if __name__ == '__main__':
    with open(sys.argv[1], 'r') as f:
        board = Query_board(256, 256)
        for line in f:
            main(board, line)
