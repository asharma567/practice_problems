'''
Write a program to determine the biggest prime palindrome under 1000.
'''
def is_prime(num):
    for i in xrange(2, num**0.5):
        if num % i == 0: return False
    return True

def max_pal(): 
    return max([i for i in xrange(0,1000) if str(i)[::-1] == str(i) and is_prime(i)])

if __name__ == '__main__':
    print max_pal()
