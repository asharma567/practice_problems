
'''
I have an array where every number in the range 1...n 
appears once except for one number which appears twice. 
Write a function for finding the number that appears twice.
'''


def func(array):
    #time/space complexity O(n) / O(n)
    
    sorted_array = sorted(array)
    
    for i in xrange(1, len(sorted_array)):
        if sorted_array[i - 1] == sorted_array[i]: 
            print sorted_array[i - 1]

def func2(array):
    #time/space complexity O(n) / O(1)
    #given that it's a triangle series: sum of sequence is (n^2 + n)/2
    #we can just take the difference vs actual sum, as shown:
    
    n = len(array)
    proper_sum_of_array = (n**2 + n) / 2
    actual_sum = 0
    
    for i in xrange(array):
        actual_sum += i
    
    repeated_number = actual_sum - proper_sum_of_array
    
    return repeated_number
