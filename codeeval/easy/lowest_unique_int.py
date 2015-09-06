'''
https://www.codeeval.com/open_challenge_scores/?pkbid=103
'''
import sys
from collections import Counter

def player_with_lowest_unique(cards):
    cards = line.split()
    dict_ints = Counter(map(int, cards))
    lowest = min([key for key, value  in dict_ints.iteritems() if value == 1])
    winner = [player_num + 1 for player_num, card in enumerate(cards) if card == str(lowest)]

    if winner: return winner[0]
    return 0

if __name__ == '__main__':
    with open(sys.argv[1], 'r') as f:
        for line in f:
            print player_with_lowest_unique(line.strip())