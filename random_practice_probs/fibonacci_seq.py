'''
Generate fibonacci sequence 
'''

# Exponential O(2^N)
# --
def fib(n):
	if n == 0 or n == 1: return n
	return fib(n - 2) + fib(n - 1)

# Linear O(N) iteratively
# --
def fib(n):
   fib_values = [0, 1]
   for i in range(2, n + 1):
      fib_values.append(fib_values[i - 1] + fib_values[i - 2])
   return fib_values[n]

# Linear O(N) recursively 
# --
def fib(n, results = {}):
	if n == 0 or n == 1: 
		results[n] = n
		return n
	elif n not in results:
		results[n] = fib(n - 1) + fib(n - 2)
	return results[n]

def fib_most_efficient(n, pre_computed={1:1, 0:0}):
    if n not in pre_computed:
        pre_computed[n] = fib_most_efficient(n-1) + fib_most_efficient(n-2)
    return pre_computed[n]

def fib_generator():
    a, b = 1, 1
    while True: # First iteration:
        yield a # yield 1 to start with and then
        a, b = b, a + b 

fib = fib_generator()
for _ in range(10):
   print fib.next()