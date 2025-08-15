#Remember how we can separate elements based on their placement in the code, ex. s = 'abcde' , s[0], or the index at the placement of 0 in the string is 'a'?
#Thus, s[-1] will be the last index in the string , so 'e' in this case.
#There is no such thing as a character in python, just a string

s = 'abcdefghijklmnopqrstuvwxyz'
print(s[0])

#slice
print(s[0:2]) #from index 0, up to (and not including) index 2. if you leave the index open and hanging, then it will go until the end of the string. ex: s[20:]

print(s[:]) #print from the start to the end

#NOW FOR THE MAGIC TWO, two colons mean that (up to (and not including)) and the second colon mean 'with a step size of', which says how many increments it will go up, like every odd number, or every even  number


# REMEMBER--> start:end:step