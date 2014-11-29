"https://www.codeeval.com/open_challenges/152/"

'''
CHALLENGE DESCRIPTION:

You're responsible for providing a demographic report for your local school district based on age. To do this, you're going determine which 'category' each person fits into based on their age.
The person's age will determine which category they should be in:

If they're from 0 to 2 the child should be with parents print : 'Still in Mama's arms' 
If they're 3 or 4 and should be in preschool print : 'Preschool Maniac' 
If they're from 5 to 11 and should be in elementary school print : 'Elementary school' 
From 12 to 14: 'Middle school' 
From 15 to 18: 'High school' 
From 19 to 22: 'College'
From 23 to 65: 'Working for the man' 
From 66 to 100: 'The Golden Years' 
If the age of the person less than 0 or more than 100 - it might be an alien - print: "This program is for humans"
'''
import sys

def func(x):
    '''
    INPUT: string with an integer char
    OUTPUT: string as it pertains to the corresponding age range
    '''

    x = int(x)
    if 0 <= x <= 2: return "Still in Mama's arms"
    elif 3 <= x <= 4: return 'Preschool Maniac'
    elif 5 <= x <= 11: return 'Elementary school'
    elif 12 <= x <= 14: return 'Middle school'
    elif 15 <= x <= 18: return 'High school'
    elif 19 <= x <= 22: return 'College'
    elif 23 <= x <= 65: return 'Working for the man'
    elif 66 <= x <= 100: return 'The Golden Years'
    
    return 'This program is for humans'

if __name__ == '__main__':
    with open(sys.argv[1], 'r') as f:
        for line in f:
            print func(line.strip())