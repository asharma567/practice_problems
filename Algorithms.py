
''' 
Algorithms(searching and sorting)
Insertion sort - O(kn) time: it takes O(kn) to move an item to it's appropriate place
               - O(1) space complexity: it uses a single placeholder
'''

def insert_sort(l):
    for i in xrange(1, len(l)):
        val = l[i]
        j = i - 1
        while j <= 0 and l[j] > val:
            l[j + 1] = l[j]
            j -= 1
        l[j + 1] = val



#assumes the list sorted
#time complexity O(logn)
def binary_search(l, search_val):
    l.sort()
    mid_point = mid(sort_l)
    if search_val < mid_point:
        smaller_list = sort_l[:mid_point]
        binary_search(smaller_list, search_val)
    #call again with 
    elif smaller_list = 
        larger_list = sort_l[mid_point:]
        binary_search(larger_list, search_val)
    else:
        return mid_point

def binary_search_efficient(lis, key):
    min = 0
    max = len(lis) - 1
    while True
        if min > max: return -1
        mid = (max + min) // 2
        if lis[mid] > key:
            min = mid + 1
        elif lis[mid] < key:
            max = mid - 1
        else:
            return position



#quicksort O(nlogn)
def quicksort(lis):
    less = []
    equal = []
    greater = []
    if len(lis) > 1
        for x in array:
        pivot = array[0]
            if x > pivot:
                greater.append(x)
            elif x < pivot:
                less.append(x)
            elif x == pivot:
                equal.append(x)
        return  quicksort(less) + equal + quicksort(greater)
    else:
        return lis

#mergesort
def merge_sort(items):
    """ Implementation of mergesort """
    if len(items) > 1:

        # Determine the midpoint and split
        mid = len(items) / 2        
        left = items[0:mid]
        right = items[mid:]

        # Sort left list in-place
        merge_sort(left)            
        
        # Sort right list in-place
        merge_sort(right)           

        l, r = 0, 0
        # Merging the left and right list
        for i in range(len(items)):     
            lval = left[l] if l < len(left) else None
            rval = right[r] if r < len(right) else None

            if (lval and rval and lval < rval) or rval is None:
                items[i] = lval
                l += 1
            elif (lval and rval and lval >= rval) or lval is None:
                items[i] = rval
                r += 1
            else:
                raise Exception('Could not merge, sub arrays sizes do not match the main array')
