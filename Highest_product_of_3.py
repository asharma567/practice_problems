'''
Given an array_of_ints, 
find the highest_product you can get 
from three of the integers.
'''
#Highest Product of 3
array_of_ints = [1, 10, -5, 1, -100]

def func(array_of_ints):
	max_prod = 0
	for i in range(len(array_of_ints)):
	    for j in range(len(array_of_ints)):
	        for x in range(len(array_of_ints)):
	            if i == j or i == x or x == j: continue
	            prod = array_of_ints[i] * array_of_ints[j] * array_of_ints[x]
	            if  prod > max_prod: max_prod = prod
return max_prod


#alternative solution
from itertools import combinations

max([reduce(lambda x, y: x * y, i) for i in combinations(array_of_ints, 3)])


def another_solution(array_of_ints):
	sorted_array_of_ints = sorted(array_of_ints)
	lis = lambda lis: reduce(lambda x,y: x * y, lis)

	#scenario takes the two negatives and one positive largest
	negpos1, negpos2 = sorted_array_of_ints[:2]
	last_int = sorted_array_of_ints[-1]
	negatives_pot = negpos1 * negpos2 * last_int

	#scenario it takes the three top positive
	positive1, positive2, positive3  = sorted_array_of_ints[-3:]

	top_pos = positive1 * positive2 * positive3

	if top_pos < negatives_pot: 
	    print negatives_pot
	else:
	    print top_pos

def highest_product_of_3(array_of_ints):
    if len(array_of_ints) < 3:
        raise Exception("Less than 3 items!")

    # We're going to start at the 3rd item (at index 2)
    # so pre-populate highests and lowests based on the first 2 items.
    # The alternative is starting these as None and checking below if they're set
    # I think this is a little cleaner, but it's debatable.
    highest = max(array_of_ints[0], array_of_ints[1])
    lowest = min(array_of_ints[0], array_of_ints[1])

    highest_product_of_two = array_of_ints[0] * array_of_ints[1]
    lowest_product_of_two = array_of_ints[0] * array_of_ints[1]

    # Except this one--we pre-populate it for the first /3/ items.
    # This means in our first pass it'll check against itself, which is fine.
    highest_product_of_three = array_of_ints[0] * array_of_ints[1] * array_of_ints[2]

    # walk through items, starting at index 2
    for current in array_of_ints[2:]:

        # do we have a new highest product of 3?
        # it's either the current highest, 
        # or the current times the highest product of two
        # or the current times the lowest product of two
        highest_product_of_three = max(
            highest_product_of_three,
            current * highest_product_of_two,
            current * lowest_product_of_two)

        # do we have a new highest product of two?
        highest_product_of_two = max(
            highest_product_of_two,
            current * highest,
            current * lowest)

        # do we have a new lowest product of two?
        lowest_product_of_two = min(
            lowest_product_of_two,
            current * highest,
            current * lowest)

        # do we have a new highest?
        highest = max(highest, current)

        # do we have a new lowest?
        lowest = min(lowest, current)

    return highest_product_of_three
