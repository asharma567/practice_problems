import sys

def number_to_sum_of_squares(number):
    return sum([int(num)**2 for num in number])

def check_if_happy(number_str):
    x = int(number_str)
    change = 0
    last_gradient_direction = None

    while x != 1:
        cur_x = number_to_sum_of_squares(str(x))

        #check for gradient
        if cur_x > x: current_gradient_direction = 'upward_slope'
        if cur_x < x: current_gradient_direction = 'downward_slope'

        #check for change in gradient
        if current_gradient_direction != last_gradient_direction:
            change += 1
        last_gradient_direction = current_gradient_direction

        if change > 120: return False
        x = cur_x

    return True

if __name__ == '__main__':
    with open(sys.argv[1], 'r') as f:
        for line in f:
            print int(check_if_happy(line))