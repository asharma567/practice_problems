'''
This is a 2nd iteration, refactored into OOP style code 
It's a solution to the problem at the URL below
https://www.codeeval.com/browse/165/
'''

import sys
from collections import Counter


class Grouper():
    
    user_domain_dict = {}
    user_friends_dict = {}
    user_recommendations = {}

    def __init__(self, input_list):
        self.make_dicts(input_list)
        self.make_user_recommendations()

    def print_recs_std_out(self):
        #print and sort everything alphabetically
        users = self.user_recommendations.keys()
        for user in sorted(users):
            if self.user_recommendations[user]:
                out_str  = user + ':' + ','.join(sorted(self.user_recommendations[user]))
                print out_str.strip()

    def make_dicts(self, input_list):
        '''
        INPUT: list of user-by-user records (strings)
        OUTPUT: domains per user dict, list of friends per user dict
        '''    
        for record in input_list:
            user, friends, domains = record.split(':')

            #USER:DOMAINS
            self.user_domain_dict[user] = domains.split(',')

            #USER:FRIENDS
            self.user_friends_dict[user] = friends.split(',')

    def make_user_recommendations(self):
        '''
        INPUT: domains per user dict, list of friends per user dict
        OUTPUT: recommended domains per user dict
        '''
        weighted_domain_recs = {}
        
        for user in self.user_friends_dict:
            weighted_domain_recs = self.compose_groups(self.user_friends_dict[user])
            #filter groups where 50% or more of their friends participate.
            #NOTE: cannot recommend domain user already belongs to
            self.user_recommendations[user] = \
            [domains for domains, weight in weighted_domain_recs.iteritems() if weight >= .5 and \
            domains not in self.user_domain_dict[user]]

    def compose_groups(self, list_of_people):    
        '''
        INPUT: string of people
        OUTPUT: dictionary of composition of groups they're in involved
        eg Driving: .8
        '''
        unpack = lambda x: reduce(lambda z, y: z + y, x)    
        total_cnt = float(len(list_of_people))
        domain_user_Counter = Counter(unpack([self.user_domain_dict[user] for user in list_of_people]))
        
        return {domain: cnt / total_cnt for domain, cnt in domain_user_Counter.iteritems()}

    def get_user_friends_dict(self):
        return self.user_friends_dict

    def get_domain_dict(self):
        return self.user_domain_dict

    def get_user_recommendations(self):
        return self.user_recommendations

def main(filename):
    '''
    INPUT: file object -> parses list of lines similar BoW
    OUTPUT: None, prints to stdout the recommended domains user-by-user
    '''
    input_list = [line.strip() for line in filename]
    groups = Grouper(input_list)
    groups.print_recs_std_out()

if __name__ == '__main__':
    with open(sys.argv[1], 'r') as f:
        main(f)