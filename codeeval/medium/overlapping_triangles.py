'''
https://www.codeeval.com/open_challenges/70/


'''


#check for penetration
def check_horizontal(rect_one_horizontal_range, rect_two_horizontal_range):

    for node in rect_one_horizontal_range:
        
        #check if it's in the range
        left = rect_two_horizontal_range[0]
        right = rect_two_horizontal_range[1]
        if node >= left or node <= right:
            return True
    return False

#check for penetration
def check_vertical(rect_one_vertical_range, rect_two_vertical_range):

    for node in rect_one_vertical_range:
        
        #check if it's in the range
        upper = rect_two_vertical_range[0]
        lower = rect_two_vertical_range[1]
        if node >= lower or node <= upper:
            return True
    return False

rect_one_horizontal_range = (one_upper_left_x, one_lower_right_x)
rect_one_vertical_range = (one_upper_left_y, one_lower_right_y)

rect_two_horizontal_range = (two_upper_left_x, two_lower_right_x)
rect_two_vertical_range = (two_upper_left_y, two_lower_right_y)

result_horizontal = check_horizontal(rect_one_horizontal_range, rect_two_horizontal_range)  
result_vertical = check_vertical(rect_one_vertical_range, rect_two_vertical_range)

print result_horizontal and result_vertical