s = 'abcdefghijklmnopqrstuvwxyz'
# The 'in' keyword is used to check if something exists inside a collection (like a list, string, or dictionary).
# Example: 'apple' in ['apple', 'banana', 'cherry'] returns True because 'apple' is in the list.

# It’s also used in loops to go through each item in a collection.
# Example: for fruit in ['apple', 'banana', 'cherry']: will loop through each fruit in the list.

# So 'in' is used for:
# 1. Membership testing → Is this item part of the group?
# 2. Iteration → Go through each item one by one.
#remember, it looks at the substring as a whole, not as individual elements
print('d' in s)
print('mno' in s)
#which is why this one below doesn't work
print('maq' in s)