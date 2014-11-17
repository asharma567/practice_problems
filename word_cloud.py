'''
You want to build a word cloud, an infographic where the size of a word corresponds to how often it appears in the body of text.
To do this, you'll need data. Write code that takes a long string and builds its word cloud data in a hash map ↴ , where the keys are words and the values are the number of times the words occured.
Think about capitalized words. For example, look at these sentences:

'After beating the eggs, Dana read the next step:'
'Add milk and eggs, then add flour and sugar.'

What do we want to do with "After", "Dana", and "add"? In this example, your final hash should include one "add" with a value of 2. Make reasonable (not necessarily perfect) decisions about cases like "After" and "Dana".
Assume the input will only contain words and standard punctuation.
'''

from collections import Counter
import re
import string

#this one won't handle hyphenated words
d = Counter(re.findall(r'\w+[-\w+]', s2.lower()))

#punctuation removal
s2 = ''.join(char for char in s if char not in string.punctuation)

d = {}
for char in s2.split():
	if char not in string.punctuation:
	    if char in d: 
	        d[char] += 1
	    else:
	        d[char] = 1

def split_words(input_string):
	words = []
	current_word = ''
	for character in input_string:
	    if character == ' ':
	        words.append(current_word)
	    elif is_letter(character):
	        current_word += character
	return words


'''
Here are a few options:

Only make a word uppercase in our hash if it is always uppercase in the original string.
Make a word uppercase in our hash if it is ever uppercase in the original string.
Make a word uppercase in our hash if it is ever uppercase in the original string in a position that is not the first word of a sentence.
Use an API or other tool that identifies proper nouns.
Ignore case entirely and make every word lowercase.
'''