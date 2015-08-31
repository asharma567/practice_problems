#Egg

'''
A building has 100 floors. One of the floors is the highest floor an 
egg can be dropped from without breaking. If an egg is dropped from 
above that floor, it will break. If it is dropped from that floor or 
below, it will be completely undamaged and you can drop the egg again.
Given two eggs, find the highest floor an egg can be dropped from 
without breaking, with as few drops as possible.
'''

#one solution
def find_floor(egg, lower, upper):
    floors = range(lower, upper)
    for ith_floor in floors:
        if drop(ith_floor, egg) == 'break': return ith_floor - 1
    return None

for i in range(1,101, 25):
    highest_floor = find_floor(egg1) 

lis = range(1,111, 20)

def find_floor():
    for i in range(1,len(lis)):
        if drop(lis[i], egg) != 'break': continue
        ith = find_floor (egg, lis[i -1], lis[i])
        if ith: 
            return ith
        else:
            return lis[i]
    return None
len(lis)
lis

def find_floor(egg):
    floors = range(1,101)
    check_if_breaks = floors[len(floors) / 2]
    if check_if_breaks == 'break': #we know it's less than that.
    