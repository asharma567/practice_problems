#Write a program to determine the sum of the first 1000 prime numbers.

def is_prime(num):
    if num == 1: return False 
    for i in xrange(2, num**0.5):
        if num % i == 0: return False 
    return True

if __name__ == '__main__':
    
    index = 0
    ctr = 0
    sum_of_prime_numbers = 0
    while(ctr <= 1000):
        if is_prime(index):
            sum_of_prime_numbers += index
            ctr += 1
        index += 1

    print sum_of_prime_numbers
