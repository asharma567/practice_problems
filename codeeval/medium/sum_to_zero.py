'''
You are given an array of integers. 
Count the numbers of ways in which the sum 
of 4 elements in this array results in zero.
'''
from itertools import combinations
import sys


def sum_k_combinations(string_array):
    array = map(int, string_array.split(','))
    return len([i for i in combinations(array, 4) if sum(i) == 0])


if __name__ == '__main__':
    with open(sys.argv[1], 'r') as f:
        for line in f:
            print sum_k_combinations(line.strip())