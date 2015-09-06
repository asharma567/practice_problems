'''
You are given several strings that may/may not be valid emails. 
You should write a regular expression that determines if the email id is a valid email id or not. 
You may assume all characters are from the english language.
'''

import sys
import re


def func(email_string):
    capture_email_regex_pattern = r'[a-zA-Z0-9]+@[a-zA-Z0-9]+.com'
    re_match = re.search(capture_email_regex_pattern, email_string.lower())
    if re_match is None: return False
    if re_match.group() == email_string: return True
    return False

if __name__ == '__main__':
    with open(sys.argv[1], 'r') as f:
        for string in f:
            print func(string)
 