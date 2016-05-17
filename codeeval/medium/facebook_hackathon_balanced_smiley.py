'''
https://www.codeeval.com/open_challenges/84/
BALANCED SMILEYS
CHALLENGE DESCRIPTION:

Credits: This problem appeared in the Facebook Hacker Cup 2013 Hackathon. 

Your friend John uses a lot of emoticons when you talk to him on Messenger. In addition to being a person who likes to express himself through emoticons, he hates unbalanced parenthesis so much that it makes him go :(. 

Sometimes he puts emoticons within parentheses, and you find it hard to tell if a parenthesis really is a parenthesis or part of an emoticon. A message has balanced parentheses if it consists of one of the following: 

- An empty string "" 
- One or more of the following characters: 'a' to 'z', ' ' (a space) or ':' (a colon) 
- An open parenthesis '(', followed by a message with balanced parentheses, followed by a close parenthesis ')'. 
- A message with balanced parentheses followed by another message with balanced parentheses. 
- A smiley face ":)" or a frowny face ":(" 
'''

import sys


def parenthesis_checker(line):

    parens_dict = {
    '(':')'
    }

    smiley_dict = {
    ':':['(',')']
    }

    seq_closed_parent_cnt = 0
    potential_smiley_cnt = 0 
    open_parent_cnt = 0 
    closed_parent_cnt = 0


    for i, char in enumerate(line):
        #check emoticon
        if potential_smiley_cnt:
            
            #check special case '(:)'
            if line[i - 2] + line[i - 1] + char == '(:)':
                if char in smiley_dict[':']: 
                    potential_smiley_cnt = 0
                    open_parent_cnt -= 1
                    closed_parent_cnt -= 1
            else:
                potential_smiley_cnt = 0
                continue

        if smiley_dict.get(char, None):
            potential_smiley_cnt = 1

        #check open parenthesis
        if parens_dict.get(char, None): 
            open_parent_cnt += 1

        #if there's an existing open parenthesis, 
        #check for an existing close
        if open_parent_cnt:
            if char == parens_dict['(']: seq_closed_parent_cnt += 1

        if char == parens_dict['(']: closed_parent_cnt += 1

    #CHECKS
    #do we have a closed parenthesis for every open?
    total_count = open_parent_cnt - closed_parent_cnt

    #Is it in sequence of openner then closer?
    sequential_total_count = open_parent_cnt - seq_closed_parent_cnt

    #check if imbalance: negatives implies more close parens than open
    if total_count != 0 or sequential_total_count != 0: 
        return False
    else:
        return True

if __name__ == '__main__':
    with open(sys.argv[1], 'r') as f:
        for line in f:
            print 'YES' if parenthesis_checker(line.strip()) else 'NO'
