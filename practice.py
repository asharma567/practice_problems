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
'''

1. **Most Frequent Words**

    Given a file that contains the text of a document and an integer n, return a list of the top n most frequent words.
'''

from collections import Counter

def get_n_most_frequent(file_name, n):
    # O(n)
    with open(file_name) as f:
        document = f.read()

    #tokenize the words in the document
    bag_of_words = [word for word in document]

    #get n most frequent
    ctr_dict = Counter(bag_of_words}

    return [ctr_dict.most_common(i + 1) for i in range(n)]



    '''
1. **Pig Latin Translator**

    Write a pig latin translator. Given a phrase in english, return the pig latin.

    If the word starts with a consonant, move consonant to the end and add ay.
    cat->atcay
    If the word starts with a vowel, add hay.
    orange->orangehay
    If the word starts with more than one consonant, move all of them to the end and add ay.
    string->ingstray
    Start by assuming the phrase is all lowercase with no punctuation.
    '''

from string import consonants

def pig_latin_translator(word):
    vowels = set('aeiou')
    if type(word) != str:
        return None
    
    cons_ctr = 0
    temp_word = word
    while temp_word:
        slice_ = temp_word[:1]
        if slice_ not in vowels:
            temp_word = temp_word[1:]
            cons_ctr += 1
        else:
            break

    if cons_ctr > 0:    
        return  word[cons_ctr:] + word[:cons_ctr] + 'ay'

    elif word[:1] in vowels:
        return word + 'hay'
    else:
        return word


if __name__ == '__main__':
    print pig_latin_translator('orange')
    print pig_latin_translator('string')
    print pig_latin_translator('cat')
'''
1. **Intersection of two lists**

    Given two lists of integers, return the intersection.

    example: `[2, 5, 3, 8, 1], [1, 9, 5, 6] => [1, 5]`
    
    Extension: get a linear time algorithm
    
    Extension 2: preserve duplicates (if both lists have two 6’s, the result should have two 6’s)
'''
    #loop method
    def find_intersection(A, B):
        #O(n^2)
        return [element for element in A if element in B]

    #set method 1
    def find_intersection(A, B):
        #O(n)
        set_B = set(B)
        return [element for element in A if element in set_B]

    #set method 2
    def find_intersection(A, B):
        #O(n)
        return list(set(B).intersection(A))

    #counter method
    def find_intersection(A, B):
        #O(n)
        ctr_dict = Counter(A + B)
        
        #O(n)
        return [item for item in ctr_dict.items() if item[1] != 1]

    def find_intersection(A, B):
        #O(n)
        return list(set(A) & set(B))

    #preserve dups
    [3,2,3], [3,3] -> [3,3]
    def find_intersection(A, B):
        
        #format to string
        A = map(str, A)
        B = map(str, B)
        
        #O(n)
        ctr_A = Counter(A)
        ctr_B = Counter(B)

        #[(1:'a'), (2:'6')]
        intersection_keys = [key for key in ctr_A.keys() if key in ctr_B.keys()]
        
        #pick the lesser of the two
        multiples = {key : min(ctr_A[key], ctr_B[key]) for key in intersection_keys}
        multiplied = [list(key * value) for key, value in multiples.items()]
        return [element for inner_list in multiplied for element in inner_list]

    # can we do better?

'''
1. **Triple Sum to 0**

    Given a list of integers, find three which sum to zero.

    example: `[3, 4, -10, 10, 1, -2, -7] => (3, 4, -7)`

    Extension: Don't allow reuse of elements

'''
    
    #Brute force
    def find_elements_sum_zero(a_list):
        output = []
        for i, element_1 in enumerate(a_list):
            for j, element_2 in enumerate(a_list[i:]):
                for k, element_3 in enumerate(a_list[j:]):
                    if element_1 + element_2 + element_3 == 0:
                        all_elements_that_sum_to_zero.append((element_1, element_2, element_3))
        return all_elements_that_sum_to_zero


    def find_elements_sum_zero(a_list):
        from itertools import combinations

        return [item for item in combinations(a_list, 3) if sum(item) == 0]

    def find_3_sumto_zero(list):
        
        #quick sort the list
        sorted_list = sorted (list)

        for index, current_element in enumerate(sorted_list):
            
            #set left and right indices
            left_i = index + 1
            right_i = len(sorted_list)

            while left_i < right_i:
                current_sum = current_element + sorted_list[left_i] + sorted_list[right_i]
                if current_sum == 0:
                    return current_element , sorted_list[left_i] , sorted_list[right_i]
                
                #this effectively makes it larger
                elif current_sum < 0:
                    left_i =- 1
                
                #this effectively makes it smaller
                else:
                    right_i =- 1

            return False

'''
1. **Largest Subsequence**

    Given a list of integers, find the consecutive subsequence with the largest sum.

    example: `[4, -6, 10, 5, -11, 12, -5] => (10, 5, -11, 12) = 16
'''
    def find_lrg_subseq(some_list_of_ints):

        lenght_of_list = len(some_list_of_ints)

        all_seq = []
        for n in range(lenght_of_list)[::-1]:
            sub_sequences = find_n_grams(n, some_list_of_ints)
            sums_of_seqs = map(lamda x: sum(x), sub_sequences)

            sums_of_seqs = [(sub_seq, sum(sub_seq)) for sub_seq in sub_sequences]

            all_seq = all_seq + sums_of_seqs

        #find out time complexity for max
        return max(all_seq, key=lamda x: x[1])[0]
        #return sorted(all_seq, key=lamda x: x[1])[0]

    #the sexy way
    def find_n_grams(n, some_list_of_ints):
        return zip(*[some_list_of_ints[index:] for index in range(n)])

    #the not so sexy way
    def find_n_grams(n, some_list_of_ints):
        ngrams = [some_list_of_ints[index:index + n] for index in range(len(some_list_of_ints) - n + 1)]
        return ngrams


    #how to extend this to triplets

1. **Phone Numberpad**

    Given a dictionary that shows the mapping of digits to numbers on a phone numberpad (e.g. ‘2’: [‘a’, ‘b’, ‘c’], ‘3’: [‘d’, ‘e’, ‘f’], etc.) and a string of digits, return all the possible letter combinations that correspond to the string of digits.

    Start by assuming that there are two digits in the string.
    
    example: `‘32’ => da, db, dc, ea, eb, ec, fa, fb, fc`
    
    Extension: Have your function also take a corpus of words and only return strings which are in your corpus.

    from itertools import product


    number_mapper = {
        0: 'o',
        1: 'abc',
        2: 'def',
        3: 'gjk',
        4: 'lmn',
        5: 'opl',
    }

    break_str = lambda x: [char for char in x]

    def number_pad(input_str):

        in_ = break_str(input_str)
        number_mapper_fmt = {str(key): value + str(key) \
                             for key, value in number_mapper.items()}
        number_mapper_fmt = {k : break_str(v) for k, v in number_mapper_fmt.items()}
        
        return list(product(*map(lambda x: number_mapper_fmt[x], in_)))

    def number_pad(input_str, corpus={}):

            in_ = break_str(input_str)
            number_mapper_fmt = {str(key): value + str(key) \
                                 for key, value in number_mapper.items()}
            number_mapper_fmt = {k : break_str(v) for k, v in number_mapper_fmt.items()}
            
            all_possibilites = list(product(*map(lambda x: number_mapper_fmt[x], in_)))

            all_possibilites = map(lambda x: ''.join(x), all_possibilites)

            all_words_in_corpus = [word for word in all_possibilites if corpus.get(word)]
            return all_words_in_corpus


1. **Matrix Diagonals**

    Given a matrix, print out the diagonals. 

    '''
    example input:
    [[1, 2, 8],
     [-4, 5, 2],
     [0, -4, -6],
     [-3, 3, 9]]
    example output:
    8
    2 2
    1 5 -6
    -4 -4 9
    0 3
    -3
    '''

1. **Even Odd Split**

    Given a list of integers, move all the odd numbers to the left and the even numbers to the right.

    Extension: Do it in-place, i.e., only use constant extra space.

    [1, 2, 3, 4, 5] -> [1, 3, 5, 2, 4]

    def integer_sorter(input_list):
        # make list about the same size
        output = [None * len(input_list)]
        back_stepper = len(input_list) - 1
        fwd_stepper = 0
        
        for index, integer in enumerate(input_list):
            # even? insert left side of the list
            if integer % 2 == 0:
                output[back_stepper]
                back_stepper =+ 1
            # else right side of the list
            else:
                output[fwd_stepper]
                fwd_stepper =+ 1

        return output
            
    def integer_sorter(input_list):
        return sorted(input_list, key=lambda x: x % 2)

    #* find the solution to this
    def integer_sorter(input_list):
        back_stepper = len(input_list) - 1
        fwd_stepper = 0
        
        while back_stepper > fwd_stepper:
            if input_list[back_stepper] % 2 != 0:
                #put it in the front
                back_stepper =- 1
            if input_list[fwd_stepper] % 2 == 0:
                #put it in the front
                fwd_stepper =+ 1

        return output

Give a list of strings, find the mapping from 1-26 for each string that maximize the value for each string. No distingulish between capital letter and lower case, other characters do not count.  



    




