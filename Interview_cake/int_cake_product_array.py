'''
You have an array of integers, and for each index you want to find the product of every integer except the integer at that index.
Write a function that takes an array of integers and returns an array of the products.
'''

def prod_array():
	for i in range(len(array)):
   		newarray[i] = reduce(lambda x,y: x * y, map(lambda x: array[x], set(range(len(array))) - {i}))
   	return newarray


if __name__ == '__main__':
	array = [1, 7, 3, 4, 0]
	prod_array(array)	




