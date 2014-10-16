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

d = Counter(re.findall(r'\w+', s2.lower()))

#punctuation removal
s2 = ''.join(char for char in s if char not in string.punctuation)

d = {}
for char in s2.split():
    if char in d: 
        d[char] += 1
    else:
        d[char] = 1


