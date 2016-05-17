import sys
from itertools import product

def find_all_possib(n, lis):
    final_lis = set(list(product(lis, repeat=n)))
    alpha_lis = sorted(final_lis)

    return ','.join(map(lambda x: ''.join(x), alpha_lis))

if __name__ == '__main__':
    with open(sys.argv[1], 'r') as f:
        for line in f:
        	if line == '': continue
            number_of_repeats, b = line.split(',')
            print find_all_possib(int(number_of_repeats), list(b.strip()))