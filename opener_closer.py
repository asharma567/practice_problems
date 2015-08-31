#interview cake Qs

'''
You're working with an intern that keeps coming to you with JavaScript code 
that won't run because the braces, brackets, and parentheses are off. To save 
you both some time, you decide to write a braces/brackets/parentheses validator.

Let's say:
'(', '{', '[' are called "openers."
')', '}', ']' are called "closers."

Write an efficient function that tells us whether or not an input string's openers and closers are properly nested.
'''

def fac(line):
    openners = {
        '(' : ')',
        '{' : '}',
        '['  : ']',
    }
    closers = openners.values()

    for word in line:
        for char in word:
            print char
            if char in closers:
                if char != lastopenners_closer: 
                    return False
                else:
                    pass

            if char in openners:
                lastopenners_closer = openners[char]











    




