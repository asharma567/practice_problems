import sys

def non_repeated_char(input_arr):
    if len(input_arr) == len(set(input_arr)): return input_arr[0]
    
    for i, char in enumerate(input_arr):
        for j, other_char in enumerate(input_arr):
            if i == j: 
                continue
            if char == other_char:
                break
            if j == len(input_arr) - 1:
                return char
    return False
from collections import Counter

def non_repeated_char_Fastest(input_arr):
    dic = Counter('yellow')
    for char in string_arr:
        if dic[char] == 1: 
            return char
    return False

if __name__ == '__main__':
    with open(sys.argv[1], 'r') as f:
        for line in f:
            print non_repeated_char(line)
