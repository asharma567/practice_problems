import sys

if __name__ == '__main__':
    with open(sys.argv[1], 'r') as f:

        #leaving the last element off because of blank at the end
        input_lis_int_str = f.read().split('\n')[:-1]
    print sum(map(int, input_lis_int_str))