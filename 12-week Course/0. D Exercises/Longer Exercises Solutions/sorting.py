from random import shuffle
import time

def bubbleSort(l):
    l = l[:]
    notsorted = 1
    while notsorted:
        notsorted = 0
        for i in range(1,len(l)):
            if l[i] < l[i-1]:
##                temp = l[i-1]
##                l[i-1] = l[i]
##                l[i] = temp
                l[i-1],l[i] = l[i],l[i-1]
                notsorted = 1
    return l

#print(bubbleSort([2,1,3,7,4,5,0.4]))

def linSort(l):
    oldl = l[:]
    newl = []
    while len(oldl) != 0:
        pos = oldl.index(min(oldl))
        newl.append(oldl.pop(pos))
    return newl

#print(linSort([2,1,3,7,4,5,0.4]))    

def isSorted(l):
    for i in range(1,len(l)):
        if l[i] < l[i-1]:
            return False
    return True

#print(isSorted([2,90,44]))
    
def bogoSort(l):
    while not isSorted(l):
        shuffle(l)
    return l

#print(bogoSort([2,4,3,1,3,5,7,7,3,56,76,2,5,6,2,4,6,3,67,3]))

def sort_timer(fun,l):
    start = time.time()
    fun(l)
    duration = time.time() - start
    return duration

l = [i for i in range(1000)]
shuffle(l)
print(sort_timer(bubbleSort, l))
print(sort_timer(linSort, l))
print(sort_timer(bogoSort, l))

