'''
Your program should accept a path to a file as its first argument. 
The file contains multiple lines. 
The first line indicates the number of lines you should output, the other lines are of different 
length and are presented randomly. You may assume that the input file is 
formatted correctly and the number in the first line is a valid positive integer.
'''
import sys

def main():
	with open(sys.argv[1], 'r') as f:
			text_list = f.read().split('\n')
			n = int(text_list[0])
			lis2 = [(phrase, len(phrase)) for phrase in text_list]
			output = sorted(lis2, key=lambda x:x[1], reverse=True)[:n]
			print '\n'.join([word[0] for word in output])


if __name__ == '__main__':
	main()
	