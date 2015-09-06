'''
https://www.codeeval.com/open_challenges/131/

CHALLENGE DESCRIPTION:

You are given a number N and a pattern. The pattern consists of lowercase latin letters and one operation "+" or "-". The challenge is to split the number and evaluate it according to this pattern e.g. 
1232 ab+cd -> a:1, b:2, c:3, d:2 -> 12+32 -> 44

'''


addition = lambda x: int(x.split('+')[0]) + int(x.split('+')[1])
subtraction = lambda x: int(x.split('-')[0]) - int(x.split('-')[1])
division = lambda x: int(x.split('+')[0]) / int(x.split('+')[1])
mod = lambda x: int(x.split('+')[0]) % int(x.split('+')[1])
mult = lambda x: int(x.split('+')[0]) * int(x.split('+')[1])

operator_strings = {
'+' : addition,
'-' : subtraction,
'*' : mult,
'%' : mod,
'/' : division,
}

def find_position_of_operator(pattern_string):
    return [(ltr, i) for i, ltr in enumerate(pattern_string) if ltr in operator_strings.keys()]

def number_string_maker(numbers_string):
    numbers_string_lis = list(numbers_string)
    for tup in position:
        opr, pos = tup
        numbers_string_lis.insert(pos, opr)
    return numbers_string_lis

def execute_operation(numbers_string_lis): 
    for ltr in ''.join(numbers_string_lis):
        if operator_strings.get(ltr, None):
            return operator_strings[ltr](''.join(numbers_string_lis))
        
if __name__ == '__main__':
    with open(sys.argv[1], 'r') as f:
        for line in f:
            numbers_string, pattern_string = line.split()
            position = find_position_of_operator(pattern_string)
            pattern_with_numbers = number_string_maker(numbers_string, position)
            print execute_operation(pattern_with_numbers)


