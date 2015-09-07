
'''
PALINDROMIC RANGES
CHALLENGE DESCRIPTION:

A positive integer is a palindrome if its decimal representation 
(without leading zeros) is a palindromic string (a string that reads 
the same forwards and backwards). 

For example, the numbers 5, 77, 363, 4884, 11111, 12121 and 349943 are palindromes. 

A range of integers is interesting if it contains an even number of palindromes. 
The range [L, R], with L <= R, is defined as the sequence of integers from L to R 
(inclusive): (L, L+1, L+2, ..., R-1, R). 
L and R are the range's first and last numbers. 

The range [L1,R1] is a subrange of [L,R] if L <= L1 <= R1 <= R. 
Your job is to determine how many interesting subranges of [L,R] there are.
'''
import sys

def is_palindrome(number):
    return int(str(number) == str(number)[::-1])

def find_n_grams(list_, n): 
    return zip(*[list_[i:] for i in xrange(n)])

def find_num_of_palindromes(range_):
    return sum([is_palindrome(x) for x in range_])

def find_all_palies(L, R):
    range_of_ints = range(L, R + 1)
    lis_of_pali = [find_n_grams(range_of_ints, i) for i in range(len(range_of_ints))]
    count_of_even_palies = len([find_num_of_palindromes(tup) for sub_list in lis_of_pali for tup in sub_list if find_num_of_palindromes(tup) % 2 == 0]) 
    if count_of_even_palies in (0,1): 
        x = len([find_num_of_palindromes(tup) for sub_list in lis_of_pali for tup in sub_list])
        return 1 if x > 0 else 0
    return len([find_num_of_palindromes(tup) for sub_list in lis_of_pali for tup in sub_list])


if __name__ == '__main__':
    with open(sys.argv[1], 'r') as f:
        for line in f:
            a, b = line.split()
            print find_all_palies(int(a), int(b))