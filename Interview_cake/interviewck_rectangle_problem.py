'''
A crack team of love scientists from OkEros (a hot new dating site) have devised a way to represent dating profiles as rectangles on a two-dimensional plane.
They need help writing an algorithm to find the intersection of two users' love rectangles. They suspect finding that intersection is the key to a matching algorithm so powerful it will cause an immediate acquisition by Google or Facebook or Obama or something.

Write a function to find the rectangular intersection of two given love rectangles.
'''

#won't work if it shares an edge

def func(rect_dict1, rect_dict2):
    def find_top_left(rect_dict): 
        return (rect_dict['x'], rect_dict['y'] + rect_dict['height'])
    
    def find_diagonal(rect_dict): 
        return (rect_dict['x'] + rect_dict['width'] , rect_dict['y'] + rect_dict['height'])
    
    def bottom_right(rect_dict): 
        return (rect_dict['x'] + rect_dict['width'], rect_dict['y'])
    
    def get_points(rect_dict):
        all_points = [map(lambda x: (x, i), range(rect_dict['x'], rect_dict['x'] + rect_dict['width'] + 1)) for i in xrange(rect_dict['y'], rect_dict['y'] + rect_dict['height'] + 1)]
        return reduce(lambda x, y: x + y, all_points)

    rect_dict1['corners'] = [
    bottom_right(rect_dict1), 
    find_diagonal(rect_dict1),
    find_top_left(rect_dict1),
    (rect_dict1['x'], rect_dict1['y'])
    ]  

    rect1_points = set(get_points(rect_dict1))
    rect2_points = set(get_points(rect_dict2))
    

    intersection_points = rect1_points.intersection(rect2_points)
    print intersection_points

    if len(intersection_points) < 4:
        return None
    else:
        x_min, y_min = min(intersection_points)
        x_max, y_max = max(intersection_points)
        
        #max, max
        top_right_corner = [(x_max, y_max)]
        print top_right_corner
        #max, min
        top_left_corner = [(x_min, y_max)]
        print top_left_corner
        
        #min, max
        bottom_right_corner = [(x_max, y_min)]
        print bottom_right_corner
        
        #min, min
        bottom_left_corner = [(x_min, y_min)]
        print bottom_left_corner
        
        new_rect = {
        'x': bottom_left_corner[0][0],
        'y': bottom_left_corner[0][1],
        'width': abs(bottom_left_corner[0][0] - bottom_right_corner[0][0]),
        'height': abs(bottom_left_corner[0][1] - top_left_corner[0][1])
        }

    return new_rect
