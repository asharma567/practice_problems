import sys
from collections import Counter
#find friend-domain composition

def make_dicts(input_list):
    '''
    INPUT: list of user-by-user records (strings)
    OUTPUT: domains per user dict, list of friends per user dict
    '''

    user_domain_dict = {}
    user_friends_dict = {}
    for record in input_list:
        user, friends, domains = record.split(':')

        #USER:DOMAINS
        user_domain_dict[user] = domains.split(',')

        #USER:FRIENDS
        user_friends_dict[user] = friends.split(',')

    return user_domain_dict, user_friends_dict


def composition_groups(list_of_people, user_domain):    
    '''
    INPUT: string of people
    OUTPUT: dictionary of composition of groups they're in involved
    eg Driving: .8
    '''
    unpack = lambda x: reduce(lambda z, y: z + y, x)    
    total_cnt = float(len(list_of_people))
    domain_user_Counter = Counter(unpack([user_domain[user] for user in list_of_people]))
    
    return {domain: cnt / total_cnt for domain, cnt in domain_user_Counter.iteritems()}


def get_user_recommendations(user_domain_dict, user_friends_dict):
    '''
    INPUT: domains per user dict, list of friends per user dict
    OUTPUT: recommended domains per user dict
    '''
    user_recommendations = {}
    for user in user_friends_dict:
        weighted_domain_recs = composition_groups(user_friends_dict[user], user_domain_dict)
        
        #filter groups where 50% or more of their friends participate.
        #NOTE: cannot recommend domain user already belongs to
        user_recommendations[user] = [domains for domains, weight in weighted_domain_recs.iteritems() if weight >= .5] 
    
    return user_recommendations


def main(filename):
    '''
    INPUT: file object
    OUTPUT: None, prints to stdout the recommended domains user-by-user
    '''
    input_list = [line for line in filename]
    output_recs = get_user_recommendations(*make_dicts(input_list))

    #print and sort everything alphabetically
    users = output_recs.keys()
    for user in sorted(users):
        print user, ':', sorted(output_recs[user])



if __name__ == '__main__':
    with open(sys.argv[1], 'r') as f:
        main(f)
