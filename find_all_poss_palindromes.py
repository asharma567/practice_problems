'''
finding all possible palindromes problem: 
*still looking for a better write up of the problem
'''
from itertoools import permutations


def permute_string(string):
    #starting with the first character move it once to the right
    
    for char in string:
        for i in xrange(len(string)):
            before = string[:i + 1]
            after = string[i:]
            perm = before + char + after
            possibilities.append(perm)
    return possibilities


def permute_string(string):
    return list(set([''.join(possibility) for possibility in permutations(string, len(string))))


def palindrome(string):
    if string = string[::-1]: return True
    return False

def main(): 
    list_of_possibilities = permute_string(string)
    return [(poss, palindrome(poss)) for poss in list_of_possibilities]
