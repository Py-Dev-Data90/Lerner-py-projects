#Strip returns something without spaces, remember, it does not affect name since strings are immutable, it returns a new string
#if we want to change a string, we have to reassign it a new value, such as x = 'potato'
#This is called method chaining, where you use more than one string method in a row!
name = input('Enter your name:').strip().capitalize()
print('Hello,' + name + '!')

# Indexes are the positions of characters in a string, starting from 0.
# For example, in the string "hello", the character 'h' is at index 0,
# 'e' is at index 1, and so on. You can use indexes to access specific
# characters like this: word[0] gives you 'h'. Negative indexes count
# from the end: word[-1] gives you the last character.
s = 'abcdefghijklmnopqrstuvwxyz'
print(s.index('o'))