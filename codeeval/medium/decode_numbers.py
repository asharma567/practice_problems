import sys

def decoder(input_arr):
    if not input_arr or len(input_arr) == 1: return 1
    
    ct = 0
    char_length = 1
    while True:
        current_char = input_arr[:char_length]
        if len(current_char) != char_length: break
        if int(current_char) > 26 or int(current_char) < 0: break
        ct += decoder(input_arr[char_length:])
        char_length += 1
        
    return ct

def solve(s):
    if not s or len(s) == 1:
        return 1

    count = 0
    char_length = 1

    while True:
        target = s[:char_length]

        if len(target) != char_length:
            break
        if int(target) > 26:
            break

        count += solve(s[char_length:])
        char_length += 1

    return count 

if __name__ == '__main__':
    with open(sys.argv[1], 'r') as f:
        for line in f:
            print solve(line)


