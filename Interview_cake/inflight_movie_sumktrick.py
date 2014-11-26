
#Brute-force approach
from itertools import combinations

def movie_flight(movie_lengths, flight_length):
    #Quadratic: O(n^2)
    r = [two_movies for two_movies in combinations(movie_lengths, 2) if sum(two_movies) <= flight_length]
    return bool(len(r))


#Sum-k trick

def movie_flight(movie_lengths, flight_length):
    movie_lengths_set = set(movie_lengths)
    #Linear time: O(n)
    for movie in movie_lengths:
        check_membership = movie - flight_length
        if check_membership in movie_lengths_set: return True
    return False