'''
READ MORE
https://www.codeeval.com/open_challenges/167/
'''
import sys


def sentence_trimmer(line):

    #there must be other ways to read in a sentence... ?, !, etc.
    # final_filtered_list = re.split('\n', file_name)
    
    # final_filtered_list = [str_ele.strip('\n') for str_ele in final_filtered_list][:-1]
    sent = line.strip()
    
    if len(sent) <= 55:
        print sent
    else:
        first_trimmed = sent[:40]

        # check if there are spaces
        if ' ' in first_trimmed:

            # find the last space
            last_space = max([position for position, char in enumerate(first_trimmed) if char == ' '])
            print first_trimmed[:last_space] + '... <Read More>'


if __name__ == '__main__':
    with open(sys.argv[1], 'r') as f:
        for line in f:
            sentence_trimmer(line)



