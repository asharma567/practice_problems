

def prod_array():
	for i in range(len(array)):
   		newarray[i] = reduce(lambda x,y: x * y, map(lambda x: array[x], set(range(len(array))) - {i}))
   	return newarray


if __name__ == '__main__':
	array = [1, 7, 3, 4, 0]
	prod_array(array)	




	