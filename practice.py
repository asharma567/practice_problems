#interview cake Qs

'''
You're working with an intern that keeps coming to you with JavaScript code that won't run because the braces, brackets, and parentheses are off. To save you both some time, you decide to write a braces/brackets/parentheses validator.
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

'''
finding all possible palindromes problem: 
*still looking for a better write up of the problem
'''

from itertoools import permutations

def palindrome(string):
    if string = string[::-1]: return True
    return False

def permute_string(string):
    return list(set([''.join(possibility) for possibility in permutations(string, len(string))))

def main(): 
    list_of_possibilities = permute_string(string)
    return [(poss, palindrome(poss)) for poss in list_of_possibilities]


def permute_string(string):
    #starting with the first character move it once to the right
    
    for char in string:
        for i in xrange(len(string)):
            before = string[:i + 1]
            after = string[i:]
            perm = before + char + after
            possibilities.append(perm)
    return possibilities


'''
Write a function that, given:
an amount of money
a list of coin denominations
computes the number of ways to make amount of money with coins of the available denominations.
Example: for amount=4 (4¢) and denominations=[1,2,3] (1¢, 2¢ and 3¢), your program would output 4—the number of ways to make 4¢ with those denominations:
1¢, 1¢, 1¢, 1¢
1¢, 1¢, 2¢
1¢, 3¢
2¢, 2¢
'''

def change_possibilities_top_down(amount_left, denominations_left):
    # base cases:
    # we hit the amount spot on. yes!
    if amount_left == 0: return 1
    # we overshot the amount left (used too many coins)
    if amount_left < 0: return 0
    # we're out of coins
    if len(denominations_left) == 0: return 0

    print "checking ways to make %i with %s" % (amount_left, denominations_left)

    # choose a current_coin
    current_coin, rest_of_coins = denominations_left[0], denominations_left[1:]

    # see how many possibilities we can get
    # for each number of times to use current_coin
    num_possibilities = 0
    while (amount_left >= 0):
      num_possibilities += change_possibilities_top_down(amount_left, rest_of_coins)
      amount_left -= current_coin

    return num_possibilities


def func(amount, denomination_list, dicts = {}):
    '''
    Alternative
    Figure out the optimal dict for change machine problem
    '''
    denomination_list = sorted(denomination_list, reverse = True)
    
    for i in denomination_list:
        mult = amount / i
        remaining_amt = amount - mult * i
        dicts[i] =  mult
        if remaining_amt > 0: func(remaining_amt, denomination_list[1:], dicts)
        return dicts


'''
simple fib
'''

def fib(num):
    if num == 1: 
        return 1
    return fib(num - 1) + fib(num - 2)






    




