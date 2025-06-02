#Pythonic vs. Non-Pythonic Code!
#not Pythonic!
x = None
if x == None:
    print('Yes, x is equal to None!')

#in this case, we should be using 'is', since we are trying to compare with a singleton value that only exists once in the whole system. Is doesn't check if the values are equal, it says are these two things pointing to the same value in memory

x = None
if x is None:
    print('Yes, x is None!')