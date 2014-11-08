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
    return time.time() - start_time

def sort_cliques_clique_level(lis):
    return sorted(lis, key=lambda x:x[0])

def check_if_subclique(target_clique, comparison_clique):
    if comparison_clique != target_clique:
        if [node for node in target_clique if node in comparison_clique] == target_clique: 
            return True
    return False

def remove_sub_cliques(cliques):
    #use numpy array here
    non_repeats = []
    for clique in cliques:        
        flag = bool([clique for alt_clique in cliques if check_if_subclique(clique, alt_clique)])
        if flag: continue
        non_repeats.append(clique)
    return non_repeats

def print_cliques_with_email(cliques, email_domain):
    for a_clique in cliques:
        print ', '.join([user + '@' + email_domain for user in a_clique])
    pass

def get_domain_name(line):
    return line[0].split('@')[1]

def strip_domain_name(line, domain_name):
    return [j.replace('@' + domain_name,'') for j in line]

def find_edges(f):
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
    #use numpy array
    output_cluster_list = []
    ctr = 0
    for key, clique in cliques.iteritems():
        output_cluster = sorted(set([key] + list(chain(*[i.split('-') for i in clique]))))
        ctr += 1
        output_cluster_list.append(output_cluster)
    return output_cluster_list

input = 'PEAK_TRAFFIC_input2.txt'
alpha_numeric = lambda x: (int(x.partition(' ')[0]) if x[0].isdigit() else float('inf'), x)


def main(f):
    user_edges, email_domain = find_edges(f)
    final_cliques_set = find_cliques(user_edges)
       
    #preprocessing for output
    sorted_cliques_node_level = sort_nodes_intra_clique(final_cliques_set)
    output = sort_cliques_clique_level(remove_sub_cliques(sorted_cliques_node_level))
    
    #outputing sorted max cliques
    print_cliques_with_email(output, email_domain)

        
if __name__ == '__main__':
    with open(sys.argv[1], 'r') as filename:
    # with open(input, 'r') as filename:
        main(filename)
        print >> sys.stderr, elapsed()