import sys
from string import maketrans
'''
knap-sack
optimize for cost given weight constraints --
1st number is a thing's index number, 
the 2nd is its weight
the 3rd is its cost
'''


def parse_line(s):
    weight_str, tuples = s.split(':')
    weight = int(weight_str)
    parsed_tuples = [map(float, a.translate(maketrans("", ""), '()$').split(',')) for a in tuples.split()]
    parsed_tuples_sorted = sorted(parsed_tuples, key=lambda x: x[2] / x[1], reverse=True)
    return parsed_tuples_sorted, weight

def func(parsed_tuples_sorted, weight):
    item_nums = []
    current_box_weight = 0
    
    for item in parsed_tuples_sorted:
        item_weight = item[1]
        item_index = item[0]
        if item_weight + current_box_weight <= weight:
            current_box_weight += item_weight
            item_nums.append(item_index)
    if item_nums: return ','.join(map(str,map(int,sorted(item_nums))))
    return '-'

if __name__ == '__main__':
    with open(sys.argv[1], 'r') as f:
      for line in f:
        print func(*parse_line(line))
