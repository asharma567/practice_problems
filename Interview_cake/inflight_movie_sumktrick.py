
#Brute-force approach
from itertools import combinations

def movie_flight(movie_lengths, flight_length):
    #Quadratic: O(n^2)
    r = [two_movies for two_movies in combinations(movie_lengths, 2) if sum(two_movies) <= flight_length]
    return bool(len(r))



def movie_flight(movie_lengths, flight_length):
    min_time = None
    min_time2 = None
    
    for i, movie in enumerate(movie_lengths):
        movies_seen = {}
        
        if min_time or min_time > curr_time:
            min_time = curr_time
            movies_seen = movie

        if min_time2 > curr_time and curr_time > min_time and movie not in movies_seen:
            min_time2 = curr_time
            
    if not min_time2: return False
    return (min_time + min_time2) <= flight_length


def get_two_movies_to_fill_flight(movie_lengths, flight_length):
	# movie lengths we've seen so far
	# keys are the lengths, values are a boolean True
	movie_lengths_seen_hash = {}

	for first_movie_length in movie_lengths:

	    matching_second_movie_length = flight_length - first_movie_length
	    if matching_second_movie_length in movie_lengths_seen_hash:
	        return True

	    movie_lengths_seen_hash[first_movie_length] = True

	# we never found a match, so return False
	return False