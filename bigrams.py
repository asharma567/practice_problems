def create_bigram(input_string):
    #bigrams of a string will be 1 less than total length
    bigram_array = [None] * (len(input_string) - 1)
    for index in xrange(1, len(input_string)):
        trailing_index = index - 1
        bigram_array[trailing_index] = input_string[index] + input_string[trailing_index]
    return set(bigram_array)