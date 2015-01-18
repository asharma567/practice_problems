'''
https://www.codeeval.com/open_challenges/91/submit/
'''
import sys

#O(n) | O(n^2)
def bubble_sort(input_list):
    
    sorted = True

    while sorted:
        sorted = True
        for i in range(len(input_list) - 1):
            if input_list[i]  > input_list[i + 1]:
                sorted = False
                input_list[i], input_list[i + 1] = input_list[i + 1], input_list[i]
        
        return input_list
    

# Best | Worst
# O(nlogn) | O(n^2)
def quick_sort(input_list):
    
    less = []
    greater = []
    equivalent = []

    if len(input_list) > 1:

        #first element of the input_list is a pivot
        pivot = input_list[0]

        for number in input_list:
            if number > pivot:
                greater.append(number)
            elif number < pivot:
                less.append(number)
            elif number == pivot:
                equivalent.append(number)

        return quick_sort(less) + equivalent + quick_sort(greater)

    else:

        return input_list

# insert_sort
# O(n) | O(n^2)
def insert_sort(input_list):
    
    for index in range(1, len(input_list)):
        trailing_index = index - 1
        value_before_target = input_list[trailing_index]
        target_value = input_list[index]

        while trailing_index > 0 and value_before_target > target_value:
            input_list[trailing_index + 1] = value_before_target
            trailing_index -= 1

        input_list[trailing_index + 1] = target_value

    return input_list

if __name__ == '__main__':
    with open(sys.argv[1], 'r') as f:
        
        for line in f:
            unsort_list_of_floats = map(float, line.strip().split())
            sorted_list = quick_sort(unsort_list_of_floats)
            print ' '.join(map(lambda x: "{0:.3f}".format(x), sorted_list))

