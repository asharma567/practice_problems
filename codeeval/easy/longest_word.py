'''
https://www.codeeval.com/open_challenges/111/
'''

import sys

def find_longest_word_greedy(sent):
    #Greedy: O(n)
    if sent == '' : return None
    longest_word = None
    for word in sent.split():
        if not longest_word or longest_word < len(word):
            longest_word = word
            
    return longest_word

def find_longest_word_sort(sent):
    #O(nlogn)
    return sorted(sent.split(), key=lambda x:len(x), reverse=True)[0]

def find_longest_word_dict(sent):
    from collections import defaultdict
    sent_dict= defaultdict(list)

    if sent == '' : return None
    for word in sent.split():
        print word
        sent_dict[len(word)].append(word)
    
    return sent_dict[max(sent_dict)][0]

def find_longest_word_max(sent):
    if sent == '' : return None
    return max(line.split(), key=lambda x: len(x))

if __name__ == '__main__':
    with open(sys.argv[1], 'r') as f:
        for line in f:
            print find_longest_word_max(line.strip())