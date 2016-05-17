import sys

def change_machine(total, denominations=[1,3,5]):
    denom_dict = {str(denom):0 for denom in denominations}
    sorted_denominations = sorted(denominations)[::-1]    
    for denom in sorted_denominations:
        number_of_times = total / denom
        total -= (number_of_times * denom)
        denom_dict[denom] = number_of_times
    return sum(denom_dict.values())

if __name__ == '__main__':
    with open(sys.argv[1], 'r') as f:
        for line in f:
            print change_machine(total=int(line))


