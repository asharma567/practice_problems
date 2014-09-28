
'''
A "concordance" is an alphabetical list of the words present in a text with a count of how
often each word appears and citations of where each word appears in the text (e.g., page
number). Write a program -- in the programming language of your choice -- that will
generate a concordance of an arbitrary text document written in English: the text can be
read from stdin, and the program should output the concordance to stdout or a file. For
each word, it should print the count and the sorted list of citations, in this case the
zero-indexed sentence number in which that word occurs. You may assume that the input
contains only spaces, newlines, standard English letters, and standard English punctuation
marks.

Below is an example of what your program would compute for the paragraph above. (The
particular formatting below isn't required, as long as you output the word, number of
occurrences, and list of sentence numbers.)


    a            {6:0,0,0,1,1,1}      of           {6:0,0,0,1,1,2}
    alphabetical {1:0}                often        {1:0}
    an           {2:0,1}              only         {1:3}
    and          {4:0,1,2,3}          or           {1:1}
    appears      {2:0,0}              output       {1:1}
    arbitrary    {1:1}                page         {1:0}
    assume       {1:3}                present      {1:0}
    be           {1:1}                print        {1:2}
    can          {1:1}                program      {2:1,1}
    case         {1:2}                programming  {1:1}
    choice       {1:1}                punctuation  {1:3}
    citations    {2:0,2}              read         {1:1}
    concordance  {3:0,1,1}            sentence     {1:2}
    contains     {1:3}                should       {2:1,2}
    count        {2:0,2}              sorted       {1:2}
    document     {1:1}                spaces       {1:3}
    e.g.         {1:0}                standard     {2:3,3}
    each         {3:0,0,2}            stdin        {1:1}
    english      {3:1,3,3}            stdout       {1:1}
    file         {1:1}                text         {4:0,0,1,1}
    for          {1:2}                that         {3:1,2,3}
    from         {1:1}                the          {10:0,0,1,1,1,1,2,2,2,3}
    generate     {1:1}                this         {1:2}
    how          {1:0}                to           {1:1}
    in           {6:0,0,1,1,2,2}      where        {1:0}
    input        {1:3}                which        {1:2}
    is           {1:0}                will         {1:1}
    it           {1:2}                with         {1:0}
    language     {1:1}                word         {4:0,0,2,2}
    letters      {1:3}                words        {1:0}
    list         {2:0,2}              write        {1:1}
    marks        {1:3}                written      {1:1}
    may          {1:3}                you          {1:3}
    newlines     {1:3}                your         {1:1}
    number       {2:0,2}              zero-indexed {1:2}
    occurs       {1:2}        
'''

import pprint
import sys
from collections import defaultdict
import re

def parse_and_dict(filename):
	'''
	INPUT: Filename
	OUTPUT: Dictionary with counters
	'''
	list_d = defaultdict(list)
	line_number = 0 
	with open(filename) as f:    
	    for line in f:
	        [list_d[word].append(line_number) for word in re.findall(r"\w+'\w+|\w+", line)]
	        line_number += 1

	return {word:{len(line_list):line_list} for word, line_list in list_d.iteritems()}


#combine everythign here
if __name__ == '__main__': 
	pprint.pprint(parse_and_dict(sys.argv[1]))