'''
You rank players in the game from highest to lowest score. 
So far you're using an algorithm that sorts in O(nlg(n)) time, 
but players are complaining that their rankings aren't updated fast enough. 
You need a faster sorting algorithm.
'''





def sort_scores(unsorted_scores, max_score):
    
    ranked_score_dict = {}
    
    for score in unsorted_scores:
        if score in ranked_score_dict:
            ranked_score_dict[score] += 1
        else:
            ranked_score_dict[score] = 1
       
    sorted_scores = []
    
    for score, cnt in ranked_score_dict.iteritems():
        for time in xrange(cnt):
            sorted_scores.append(score)
    
    return sorted_scores
