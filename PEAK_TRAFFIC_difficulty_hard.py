'''
https://www.codeeval.com/open_challenges/49/submit/?lid=640394
'''
from itertools import combinations
from itertools import chain
from collections import Counter
import sys
import time


start_time = time.time()
def elapsed():
    '''
    Tool used for time complexity enhancement
    Measures time by instatiating and storing a time.time() obj in start_time
    '''
    return time.time() - start_time

def sort_cliques_clique_level(lis):
    '''
    Sorts cliques within a list alphabetically ascending
    INPUT: unsorted list of cliques
    Note - Final step before cliques are displayed 
    '''
    return sorted(lis, key=lambda x:x[0])

def check_if_subclique(target_clique, comparison_clique):
    '''
    Checks if target_clique is a sub-clique of comparison_clique
    INPUT: potential sub-clique: target_clique, super-clique: comparison_clique
    OUTPUT: boolean {True, False} sub-clique or not
    '''
    if comparison_clique != target_clique:
        if [node for node in target_clique if node in comparison_clique] == target_clique: 
            return True
    return False

def remove_sub_cliques(cliques):
    '''
    Challenge states to only display all super-cliques
    Hence this removes all sub-cliques
    INPUT: list of all cliques within the network
    OUTPUT: all super-cliques i.e. max cliques
    '''

    non_repeats = []
    for clique in cliques:        
        flag = bool([clique for alt_clique in cliques if check_if_subclique(clique, alt_clique)])
        if flag: continue
        non_repeats.append(clique)
    return non_repeats

def print_cliques_with_email(cliques, email_domain):
    '''
    Iterates through nodes(users) within list of cliques and concats email domain names
    INPUT: list of cliques with nodes with no email domain
    OUTPUT: list of cliques with nodes with email domain
    NOTE: function to display final output to stdout
    '''
    for a_clique in cliques:
        print ', '.join([user + '@' + email_domain for user in a_clique])
    pass

def get_domain_name(line):
    '''
    Parses domain_name name
    INPUT: full user string 
    OUTPUT: email doman
    '''
    return line[0].split('@')[1]

def strip_domain_name(line, domain_name):
    '''
    Removes email_domain
    easier for network graph analysis
    '''
    return [j.replace('@' + domain_name,'') for j in line]

def find_edges(f):
    '''
    Finding the edges(connections) between nodes(users)
    INPUT: file with 3 columns {timestamp, user1 email, user2 email} space delimited
    OUTPUT: Counter dictionary with frequency of communication, email_domain
    '''
    user_edges = Counter()
    first_line = True
    for line in f:
        #getting the emails from the last two columns
        parsed_line = line.split()[-2:]

        #getting the domain name eg ajay@facebook.com -> facebook.com
        if first_line: 
            email_domain = get_domain_name(parsed_line)
            first_line = False 

        stripped_parsed_line = strip_domain_name(parsed_line, email_domain)

        #sorting so pair combinations are homogenous
        user_a, user_b = sorted((stripped_parsed_line[0], stripped_parsed_line[1]))

        #users are nodes
        user_edges[user_a + '-' + user_b] += 1
    return user_edges, email_domain

def find_cliques(edges):
    '''
    INPUT: All edges within the graph
    OUTPUT: All cliques
    '''
    cliques = {}
    for ctr, edge in enumerate(edges):
        target_node = edge.split('-')[0]
        
        #come up with better naming here
        new_lis = sorted([j.split('-')[1] for j in edges if target_node == j.split('-')[0]])
        
        #modularize
        if len(new_lis) > 1:
            #use Numpy array
            potential_edges = []
            for i, j in combinations(new_lis, 2):
                items = sorted([i, j])
                potential_edges.append(items[0] + '-' + items[1])

            combos_to_check = set(potential_edges)

            #clusters
            cliques_for_target_node = [i for i in combos_to_check if i in edges]

            if len(cliques_for_target_node) > 0: 
                #assignment to dict
                cliques[target_node] = cliques_for_target_node
    return cliques

def sort_nodes_intra_clique(cliques):
    '''
    INPUT: list of cliques
    OUTPUT: list of cliques with sorted nodes within the cliques
    '''
    #use numpy array
    output_cluster_list = []
    ctr = 0
    for key, clique in cliques.iteritems():
        output_cluster = sorted(set([key] + list(chain(*[i.split('-') for i in clique]))))
        ctr += 1
        output_cluster_list.append(output_cluster)
    return output_cluster_list


def main(f):
    '''
    INPUT: filename
    OUTPUT: prints to stdout the final result of max cliques within the network graph
    '''
    user_edges, email_domain = find_edges(f)
    final_cliques_set = find_cliques(user_edges)
       
    #preprocessing for output
    sorted_cliques_node_level = sort_nodes_intra_clique(final_cliques_set)
    output = sort_cliques_clique_level(remove_sub_cliques(sorted_cliques_node_level))
    
    #outputing sorted max cliques
    print_cliques_with_email(output, email_domain)

        
if __name__ == '__main__':
    with open(sys.argv[1], 'r') as filename:
        main(filename)
        