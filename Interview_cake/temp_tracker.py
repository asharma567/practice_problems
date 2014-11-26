'''
You decide to test if your oddly-mathematical heating company is fulfilling its All-Time Max, Min, Mean and Mode Temperature Guarantee™.
Write a class TempTracker with these methods:
insert()—records a new temperature
get_max()—returns the highest temp we've seen so far
get_min()—returns the lowest temp we've seen so far
get_mean()—returns the mean ↴ of all temps we've seen so far
get_mode()—returns the mode ↴ of all temps we've seen so far
Notes:
We'll record our temperatures in Celsius, so we can assume they'll all be in the range 0..100.
Temperatures will be inserted as integers. get_mean() should return a float, but the rest can return ints.
Optimize for space and time. Favor speeding up the get_ functions over speeding up the insert function.
If there is more than one mode, return any of the modes.
'''



class TempTracker:
    
    #min and max methods
    max_temp = 100
    min_temp = None
    
    #mean method
    cumulative_cnt = 0
    cumulative_sum = 0
    
    #mode method
    max_occ = None
    mode_freq = 0
    mode_max = 0
    occurences_array = [0] * (max_temp + 1)
    
    def insert(self, newtemp):
        if not self.max_temp or self.max_temp < newtemp:
            self.max_temp = self.newtemp
        if not self.min_temp or self.min_temp > newtemp:
            self.min_temp = newtemp
        self.cumulative_cnt += 1
        self.cumulative_cnt += newtemp
        self.occurences_array[newtemp] += 1
        if not self.max_occ or self.max_occ < self.occurences_array[newtemp]:
            self.mode_freq = self.occurences_array[newtemp]
            self.mode_max = newtemp
            
    def get_max(self):
        return self.max_temp
    
    def get_min(self):
        return self.min_temp
    
    def get_mean(self):
        return self.cumulative_sum / float(self.cumulative_cnt)
    
    def get_mode(self):
        return self.mode_max