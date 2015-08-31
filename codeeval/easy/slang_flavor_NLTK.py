'''
https://www.codeeval.com/open_challenges/174/submit/?lid=731009
'''



import sys
import nltk



def print_outcome(s):
    '''
    INPUT
    OUTPUT
    
    '''
    ending_punc = {'.', '!', '?'}
    ending_punc_ctr = 0
    position_ctr = 0

    lis = [
    ', yeah!', 
    ', this is crazy, I tell ya.',
    ', can U believe this?',
    ', eh?',
    ', aw yea.',
    ', yo.',
    '? No way!',
    '. Awesome!'
    ]
    output = []
    
    for sent in nltk.sent_tokenize(s):
        if sent[-1] in ending_punc: ending_punc_ctr += 1
        if ending_punc_ctr % 2 == 0:
            output.append(sent[:-1] + lis[position_ctr])
            position_ctr += 1
        else:
            output.append(sent)
    return ''.join(output)
    


if __name__ == '__main__':
    with open(sys.argv[1], 'r') as f:
        print print_outcome(f.read())
