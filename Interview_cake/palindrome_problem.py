def reverse_inplace(string):
    string = list(string)
    back_step = len(string) - 1
    fwd_step = 0
    while back_step > fwd_step:
        
        #swap
        place_holder = string[fwd_step]
        string[fwd_step] = string[back_step]
        string[back_step] = place_holder
        fwd_step =fwd_step+ 1
        back_step =back_step- 1
    
    return ''.join(string)
        

def palin_checker2(string1): return string1 == reverse_inplace(string1)

def palin_checker1(string1): return string1 == string1[::-1]